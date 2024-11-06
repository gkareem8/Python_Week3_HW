# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
last_month_profit=0
curr_month_profit=0
total_change=0

max_month = ""
min_month = ""
greatest_increase = 0
greatest_decrease = 0

# Open and read the csv
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_months+=1
        total_net+=int(row[1])

        # check if first row - skip first row
        if total_months==1:
            last_month_profit=int(row[1]) 
        else:
            #get change 
            curr_month_profit = int(row[1])
            change = curr_month_profit - last_month_profit
            total_change +=change

            # reset
            last_month_profit= curr_month_profit

            # Update greatest increase
            if change > greatest_increase:
                greatest_increase = change
                max_month = row[0]

            # Update greatest decrease
            if change < greatest_decrease:
                greatest_decrease = change
                min_month = row[0]

#output summary 
output=f'''
Total Months: {total_months}
Total: ${total_net}
Average Change: ${total_change / (total_months - 1)}
Greatest increase in profits: {max_month} (${greatest_increase})
Greatest decrease in profits: {min_month} (${greatest_decrease})
'''

# Print the output
print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
