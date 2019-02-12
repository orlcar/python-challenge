# PyPoll

import os
import csv

# Specify file to read
csvPath = os.path.join("Resources", "election_data.csv")

#  Read the file
with open(csvPath, newline = '') as cvsFile:
    csvReader = csv.reader(cvsFile, delimiter=',')
    next(csvReader)

    total_votes = 0
    candidates = dict()

    # Go through the file
    for row in csvReader:

            # Count the number of votes
            total_votes += 1
            
            # Find and append unique candidates to dictionary
            if row[2] not in candidates:
                candidates[row[2]] = 1
            else:
                candidates[row[2]] += 1

    # Function to calculate percentage of votes won
    def percentage_votes(candidate):

        percent_won = (candidate / total_votes) * 100
        return percent_won

    # Get the winner of the election based on popular vote
    winner = max(candidates, key=candidates.get)

    # Print the analysis to the terminal

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for key, value, in candidates.items():
      print(f"{key}: {percentage_votes(value):.3f}% ({value})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")


# ---- Export a text file with the results ----

# Specify file to write
output_path = os.path.join("election_results.txt")

# Open the file using "write" mode and specifiy the variable to hold the contents
with open(output_path, "w") as textFile:

    print("Election Results", file=textFile)
    print("-------------------------", file=textFile)
    print(f"Total Votes: {total_votes}", file=textFile)
    print("-------------------------", file=textFile)
    for key, value, in candidates.items():
      print(f"{key}: {percentage_votes(value):.3f}% ({value})", file=textFile)
    print("-------------------------", file=textFile)
    print(f"Winner: {winner}", file=textFile)
    print("-------------------------", file=textFile)