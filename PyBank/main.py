# Import modules
import csv
import os

# Path to CSV file
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

# Declare lists and variables 
date = []
profit_losses = []
change = 0
previous_date = 0
total_change = 0
averagechange = 0
biggest_change = 0
lowest_change = 0
highest_date = ""
lowest_date = ""

# Read in CSV file
with open(budget_csv, 'r') as csvfile:

    # Split data with comma delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip .CSV header
    header = next(csvreader)

    # Print output header
    print("Financial Analysis")
    print("----------------------------")

    # Loop through rows
    for rows in csvreader:

        # Append date library with row values in first .csv columm
        date.append(rows[0])

        # Append profit_losses library with integer row values in second .csv column 
        profit_losses.append(int(rows[1]))

        # Condition for first previous date
        if previous_date == 0:
          # First previous date is row 2
          previous_date = int(rows[1])

        else:
          # Set variable for profit/loss change after first calculation
          change = int(rows[1]) - previous_date

          # Set previous date as next date
          previous_date = int(rows[1])

          # Set variable to hold total profit/loss change
          total_change = total_change + change 

          # Condition for highest change
          if change > biggest_change:
            # Set variable to hold highest change
            biggest_change = change
            # Set varibale to hold date of highest change
            highest_date = rows[0]

          # Condition for lowest change
          if change < lowest_change:
            # Set variable to hold lowest change
            lowest_change = change
            # Set varibale to hold date of lowest change
            lowest_date = rows[0]
                
    # Create variable for sum of profit_losses library
    total = sum(profit_losses)

    # Create variable for length of date library
    length = len(date)

    # Set variable to calcualte average change in profit/loss out of 85 changes (length - 1)
    averagechange = total_change / (length - 1)
    # Format average to 2 decimal places
    averagechange = format(averagechange, '.2f')

    # Print total months
    print(f"Total Months: {length}")

    # Print total amount 
    print(f"Total: ${total}")

    # Print average change
    print(f"Average Change: ${averagechange}")

    # Print Greatest Increase
    print(f"Greatest Increase in Profits: {highest_date} (${biggest_change})")

    # Print Greatest Decrease
    print(f"Greatest Decrease in Profits: {lowest_date} (${lowest_change})")

# Set variable for text file
textfile = os.path.join(".", "Analysis", "analysis.txt")

# Open the text file
with open(textfile, "w") as datafile:

    # Save output strings as variable
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {length}\n"
        f"Total: ${total}\n"
        f"Average Change: ${averagechange}\n"
        f"Greatest Increase in Profits: {highest_date} (${biggest_change})\n"
        f"Greatest Decrease in Profits: {lowest_date} (${lowest_change})")


    # Write the output to analysis.txt
    datafile.write(output)