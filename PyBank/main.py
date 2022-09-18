
import os 
import csv

#Paths to directories
budgetpath = os.path.join("Resources","budget_data.csv")
save_path = os.path.join("Analysis")

with open(budgetpath, encoding= "utf8") as budgetfile:
    #Defining variables for use
    month_count = 0
    net_profit = 0
    max_profit = 0
    min_profit = 0
    min_month = ""
    max_month = ""
    monthlychanges = []
    monthlychanges_difference = []
    averagemonthlychanges = 0

    #Reading the file
    budgetreader = csv.reader(budgetfile, delimiter =",")

    #Skipping Headers
    next(budgetreader)
    
    #Loop through the file and read data

    for row in budgetreader:
    
        #Counting how many rows/months there are
        month_count += 1

        #Converting string type column to integer type 
        row[1] = int(row[1])

        #Storing the profit/losses in a list
        monthlychanges.append(row[1])

        #Summing up profits to calcualate net profit
        net_profit += row[1]

        #Conditionals to test for maximum profit and which month it occured
        if max_profit < row[1]:
            max_profit = row[1]
            max_month  = row[0]

        #Conditionals to test for minimum profit and which month it occured
        if min_profit > row[1]:
            min_profit = row[1]
            min_month  = row[0]
    
    #Loop through monthlychanges and capture the differences of the elements inside 
    for profit in range(1,len(monthlychanges)):
        monthlychanges_difference.append(monthlychanges[profit]-monthlychanges[profit-1])
    
    #Sum the total of the differences between the monthly changes and divide by the total month count
    averagemonthlychanges = sum(monthlychanges_difference)/len(monthlychanges)

#Output to terminal and write file to folder    
print("Financial Analysis")
print("---"*7)
print(f"Total Months: {month_count}")
print(f"Total: {net_profit}")    
print(f"Average Change: {averagemonthlychanges}")
print(f"Greatest Increase in Profits: {max_month} ({max_profit})")
print(f"Greatest Increase in Profits: {min_month} ({min_profit})")
print("---"*7)

with open(os.path.join("Analysis", "Financial_Analysis.txt"), "w") as f:
    print("Financial Analysis", file = f)
    print("---"*7, file = f)
    print(f"Total Months: {month_count}", file = f)
    print(f"Total: {net_profit}", file = f)    
    print(f"Average Change: {averagemonthlychanges}", file = f)
    print(f"Greatest Increase in Profits: {max_month} ({max_profit})", file = f)
    print(f"Greatest Increase in Profits: {min_month} ({min_profit})", file = f)
    print("---"*7, file = f)