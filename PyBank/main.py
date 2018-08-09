#import os and write csv path
from statistics import mean
import os
csvpath = os.path.join("budget_data.csv") 

#Improved Reading using CSV module
import csv
with open(csvpath, newline='') as csvfile:

# CSV reader delimiter and varaiable
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

#list creation, places to store csv "rows" (They are columns!)
    dates = []
    revenues = []

#run for loop for every row
    for x in csvlist:
        dates.append(x[0])
        revenues.append(int(x[1]))
    
#create a list for revenue change
    revchange = []

#run loop through revenues list to find the change revenues from month
    revchange = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
#variables
    total_revenue = sum(revenues)
    max_change = max(revchange)
    big_loss = min(revchange)
    avg_change = mean(revchange)
    total_month = len(dates)
    max_month = None
    loss_month = None

# external rev value, maybe none to start
# for row in csvlist:
# if none
# set external revenue val
# skip rest of loop, go to next iteration
# if diff == big loss
# store current rev val in external rev val
    
#for loop to find corresponding date 
    initial_val = None
    for row in csvlist:
        if initial_val is None:
            initial_val = int(row[1])
            continue
        if int(row[1]) - initial_val == big_loss:
            loss_month = row[0]
        initial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            max_month = row[0]
        initial_val2 = int(row[1])
    

    print("Financial Analysis")
    print ("----------------------------------------------------")
    print(f"Total Months:{total_month}")
    print (f"Total Net Amount: $ {total_revenue}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {max_month}  ${max_change}")
    print(f"Greatest Decrease in Profits: {loss_month}  ${big_loss}")
