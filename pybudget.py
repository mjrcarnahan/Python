import os
import csv

budget_csv = os.path.join('03-Python','Homework','Instructions','PyBank','Resources','budget_data.csv')

def sortSecond(val):
    return val[1]

# Lists to store data

date = []
profit = []
change_list = []

 # Read the header row first 
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        # Add date
        date.append(row[0])
	    # Add profit/loss
        profit.append(row[1])
        total = sum(int(i) for i in profit)
        months = int(len(date))
        
        #print(months)
        #print(total)
        
    profit_list = [int(i) for i in profit] 
    #print("************************")
    
    for i in range(1,len(profit_list)):
        change = profit_list[i] - profit_list[i-1]
        change_list.append(change)
        #print(change) 
    
    total_change = sum(int(i) for i in change_list)
    #print(total_change)
    average_change = total_change/int(len(profit_list)-1)
    average_change = round(average_change, 2)
    #print(average_change)

    change_list.insert(0,0)
    #dollar = "$"
    #change_list = [dollar.format(x) + str(x) for x in change_list]

    zip_descend = zip(date,change_list)
    zip_descend = list(zip_descend)
    zip_descend.sort(key = sortSecond)
    greatest_decrease = zip_descend[0]
    #print(greatest_decrease)

    zip_ascend = zip(date,change_list)
    zip_ascend = list(zip_ascend)
    zip_ascend.sort(key = sortSecond, reverse=True)
    greatest_increase = zip_ascend[0]
    #print(greatest_increase)

   
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months: " + str(months))
    print("Average Change: $" + str(average_change))    
    print("Greatest Increase in Profits: " + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(greatest_decrease))

    