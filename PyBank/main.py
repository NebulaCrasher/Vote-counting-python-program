import os 
import csv

budgetpath = os.path.join("Resources", "budget_data.csv")

with open(budgetpath, encoding= "utf8") as budgetfile:
    month_count = 0
    net_profit = 0
    max_profit = 0
    min_profit = 0
    min_month = ""
    max_month = ""
    budgetreader = csv.reader(budgetfile, delimiter =",")
    next(budgetreader)
    #Converting string type column to integer type 
    for row in budgetreader:
        month_count += 1
        row[1] = int(row[1])
        net_profit += row[1]
        if max_profit < row[1]:
            max_profit = row[1]
            max_month = row[0]
        if min_profit > row[1]:
            min_profit = row[1]
            min_month = row[0]
    print(month_count)
    
    
