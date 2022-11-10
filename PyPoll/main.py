# Import modules
import csv
import os

# Path to CSV file
election_csv = os.path.join(".", "Resources", "election_data.csv")

# Declare variables
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

    for rows in csvreader:

        totalvoters.append(rows[0])

        if rows[2] not in unique_list:

            unique_list.append(rows[2])
            
        if rows[2] == unique_list[0]:

            candidate1count = (candidate1count + 1)

        elif rows[2] == unique_list[1]:

            candidate2count = (candidate2count + 1)

        elif rows[2] == unique_list[2]:

            candidate3count = (candidate3count + 1)

        if candidate1count > candidate2count and candidate1count > candidate3count:

            winner = unique_list[0]
        
        elif candidate2count > candidate1count and candidate2count > candidate3count:

            winner = unique_list[1]

        elif candidate3count > candidate2count and candidate3count > candidate1count:

            winner = unique_list[2]

    voteramount = len(totalvoters)

    percent_cand1 = (candidate1count / voteramount) * 100
    percent_cand1 = format(percent_cand1, '.3f')

    percent_cand2 = (candidate2count / voteramount) * 100
    percent_cand2 = format(percent_cand2, '.3f')

    percent_cand3 = (candidate3count / voteramount) * 100
    percent_cand3 = format(percent_cand3, '.3f')

    # Print total months
    print(f"Total Votes: {voteramount}")

    print("-------------------------")

    print(f"{unique_list[0]}: {percent_cand1}% ({candidate1count})")

    print(f"{unique_list[1]}: {percent_cand2}% ({candidate2count})")

    print(f"{unique_list[2]}: {percent_cand3}% ({candidate3count})")

    print("-------------------------")

    print(f"Winner: {winner}")

    print("-------------------------")

    textfile = os.path.join(".", "Analysis", "analysis.txt")

    with open(textfile, "w") as datafile:

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

        datafile.write(output)




