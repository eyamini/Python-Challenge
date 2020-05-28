import os
import csv

csvpath = 'budget_data.csv';

profits = []
month_change = []
date = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    header = next(csvreader)
    #print(header)

    total = 0
    months = 0
    profit = 0
    profit_change = 0

    for row in csvreader:
        total += int(row[1])
        months += 1

        date.append(row[0])
        profits.append(row[1])
        month_profit = int(row[1])
        month_difference = month_profit - profit
        month_change.append(month_difference)
        month_total = sum(month_change)

        profit_change = profit_change + month_difference
        profit = month_profit

        average_change = month_total/months

        greatest_increase = max(month_change)
        greatest_decrease = min(month_change)

        max_date = date[month_change.index(greatest_increase)]
        min_date = date[month_change.index(greatest_decrease)]

    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(total))
    print("Average Change: $" + str(int(average_change)))
    print("Greatest Increase in Profits: " + str(max_date) + "  $" + "(" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(min_date) + "  $" + "(" + str(greatest_decrease) + ")")


