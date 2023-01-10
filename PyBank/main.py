import os
import csv

months =[]
profitLoss =[]
change =[]
count = 0
sumOfAvg = 0
sum = 0
previousValue = 0

csvpath = os.path.join("..", "Resources", "budget_data.csv")
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    for x in csvreader:
        if csvreader.line_num > 2:
            changeValue = int(x[1])-previousValue
            change.append(changeValue)
            sumOfAvg = sumOfAvg + changeValue

        if x[0] not in months:
            months.append(x[0])
            count += 1
            sum = sum + int(x[1])

        profitLoss.append(x[1])
        previousValue = int(x[1])
            
    print("Total Months : ", str(count))
    print("Sum : ", str(sum))
    minChange = min(change)
    maxChange = max(change)
    print("Min : ", str(minChange))
    print("Max : ", str(maxChange))
    average = sumOfAvg  / (count - 1)
    print("Average : ", str(average))
    

    

        
    
    
