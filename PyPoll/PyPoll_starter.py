# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_names = []
vote_count = []


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        current_name = row[2]

        # If the candidate is not already in the candidate list, add them
        name_in_list = True
        for name in candidate_names:
            if current_name == name:
                name_in_list = False
        if name_in_list:
            candidate_names.append(current_name)
            vote_count.append(0)
        # Add a vote to the candidate's count
        vote_count[candidate_names.index(current_name)] = vote_count[candidate_names.index(current_name)] + 1
    print()


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    total_print = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
    print(total_print)

    # Write the total vote count to the text file
    txt_file.write(total_print)

    # Loop through the candidates to determine vote percentages and identify the winner
    for name in candidate_names:
        current_name = name
        # Get the vote count and calculate the percentage
        current_count = vote_count[candidate_names.index(current_name)]
        current_percent = current_count/total_votes
        # Update the winning candidate if this one has more votes
        if current_count > winning_count:
            winning_candidate = name
            winning_count = current_count

        # Print and save each candidate's vote count and percentage
        output = f"""{current_name}: {current_percent:.3%} ({current_count})"""
        print(output+"\n")
        txt_file.write(output+"\n")


    # Generate and print the winning candidate summary
    winning_print = f"""-------------------------
Winner: {winning_candidate}
-------------------------"""
    print(winning_print)
    # Save the winning candidate summary to the text file
    txt_file.write(winning_print)
