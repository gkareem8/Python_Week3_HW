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
candidate_vote = {}

# Open and read the csv
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row) 
        total_votes += 1 #total votes
        candidate= row[2] 

        #count votes for each candidate 
        if candidate in candidate_vote:
            candidate_vote [candidate] += 1 
        else:
            candidate_vote [candidate] = 1

    # caluclate the percentage of each candidates per vote count
    candidate_percentage = {candidate:(votes/ total_votes)*100 for candidate, votes in candidate_vote.items()}

    # determine the winner 
    winner = ""
    winning_count = 0
    for candidate, votes in candidate_vote.items():
        if votes > winning_count:
            winning_count = votes
            winner = candidate 

#output summary 
output =f'''
Election Results 
--------------------------
Total_votes: {total_votes}
'''

#add each candidate's results to the output 
for candidate, votes in candidate_vote.items():
    percentage = candidate_percentage[candidate]
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"

output += f"--------------------------\n"
output += f"Winner: {winner}\n"
output += f"--------------------------\n"


#print the output 
print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)