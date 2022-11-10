# Import modules
import csv
import os

# Path to CSV file
election_csv = os.path.join(".", "Resources", "election_data.csv")

# Declare variables and lists
totalvoters = []
unique_list = []
candidate1count = 0
candidate2count = 0
candidate3count = 0

# Read in CSV file
with open(election_csv, 'r') as csvfile:

    # Split data with comma delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip .CSV header
    header = next(csvreader)

    # Print output header
    print("Election Results")
    print("-------------------------")

    # Loop through rows
    for rows in csvreader:

        # Append values first column rows to totalvoters
        totalvoters.append(rows[0])

        # Condition to find new candidate
        if rows[2] not in unique_list:

            # Append new candidates to unique_list
            unique_list.append(rows[2])

        # Condition to compare the third column with the first candidate    
        if rows[2] == unique_list[0]:

            # Create variable to hold vote count per candidate
            candidate1count = (candidate1count + 1)

        elif rows[2] == unique_list[1]:

            candidate2count = (candidate2count + 1)

        elif rows[2] == unique_list[2]:

            candidate3count = (candidate3count + 1)

        # Condition to designate winner as candidate with most votes
        if candidate1count > candidate2count and candidate1count > candidate3count:

            winner = unique_list[0]
        
        elif candidate2count > candidate1count and candidate2count > candidate3count:

            winner = unique_list[1]

        elif candidate3count > candidate2count and candidate3count > candidate1count:

            winner = unique_list[2]

    # Create variable to hold total election voters
    voteramount = len(totalvoters)

    # Create variables to calculate percentage of total votes, format to 3 decimal places
    percent_cand1 = (candidate1count / voteramount) * 100
    percent_cand1 = format(percent_cand1, '.3f')

    percent_cand2 = (candidate2count / voteramount) * 100
    percent_cand2 = format(percent_cand2, '.3f')

    percent_cand3 = (candidate3count / voteramount) * 100
    percent_cand3 = format(percent_cand3, '.3f')

    # Print total months
    print(f"Total Votes: {voteramount}")

    print("-------------------------")

    # Print candidate list with percentages and voter counts
    print(f"{unique_list[0]}: {percent_cand1}% ({candidate1count})")

    print(f"{unique_list[1]}: {percent_cand2}% ({candidate2count})")

    print(f"{unique_list[2]}: {percent_cand3}% ({candidate3count})")

    print("-------------------------")

    # Print election winner
    print(f"Winner: {winner}")

    print("-------------------------")

    # Set variable for text file
    textfile = os.path.join(".", "Analysis", "analysis.txt")

    # Open the text file
    with open(textfile, "w") as datafile:

        # Save output strings as variable
        output = (
            f"Election Results\n"
            f"-------------------------\n"
            f"Total Votes: {voteramount}\n"
            f"-------------------------\n"
            f"{unique_list[0]}: {percent_cand1}% ({candidate1count})\n"
            f"{unique_list[1]}: {percent_cand2}% ({candidate2count})\n"
            f"{unique_list[2]}: {percent_cand3}% ({candidate3count})\n"
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"-------------------------")

        # Write the output to analysis.txt
        datafile.write(output)
