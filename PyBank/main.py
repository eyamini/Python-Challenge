import os
import csv

csvpath = 'budget_data.csv';

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    header = next(csvreader)
    total = 0
    months = 0

    for row in csvreader:
        total += int(row[1])
        months += 1
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(total))
    #print("Average Change: $" + str(total))
    #print("Greatest Increase in Profits: " + str(total))
    #print("Greatest Decrease in Profits: " + str(total))
        
    

    

