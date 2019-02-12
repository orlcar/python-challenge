# PyBank

import os
import csv

# Specify file to read
csvPath = os.path.join("Resources", "budget_data.csv")

#  Read the file
with open(csvPath, newline = '') as cvsFile:
    csvReader = csv.reader(cvsFile, delimiter=',')
    next(csvReader)

    net_amount = 0
    max_increase = 0
    max_decrease = 0
    total_months = 0
    max_increase_month = ""
    max_decrease_month = ""

    for row in csvReader:        

        # Variable for profits/losses
        value = int(row[1])

        # Get the total number of months included in the dataset
        total_months += 1

        # Get the net total amount of "Profit/Losses" over the entire period
        net_amount += value

        # Get the greatest increase in profits over the entire period
        max_increase = max(max_increase, value)

        # Get month for greatest increase in profits
        if value == max_increase:
            max_increase_month = row[0]

        # Get the greatest decrease in losses over the entire period
        max_decrease = min(max_decrease, value)
        
        # Get month for greatest decrease in losses
        if value == max_decrease:
            max_decrease_month = row[0]
    
    # Get the average of the changes in "Profit/Losses" over the entire period
    average_change = net_amount/total_months

    # Print the analysis to the terminal

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}") 
    print(f"Total: ${net_amount}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest increase in profits: {max_increase_month} (${max_increase})")
    print(f"Greatest decrease in profits: {max_decrease_month} (${max_decrease})")

# ---- Export a text file with the results ----

# Specify file to write
output_path = os.path.join("budget_results.txt")

# Open the file using "write" mode and specify the variable to hold the contents
with open(output_path, "w") as textFile:
    print("Financial Analysis", file=textFile)
    print("----------------------------", file=textFile)
    print(f"Total Months: {total_months}", file=textFile)
    print(f"Total: ${net_amount}", file=textFile)
    print(f"Average Change: ${average_change:.2f}", file=textFile)
    print(f"Greatest increase in profits: {max_increase_month} (${max_increase})", file=textFile)
    print(f"Greatest decrease in profits: {max_decrease_month} (${max_decrease})", file=textFile)