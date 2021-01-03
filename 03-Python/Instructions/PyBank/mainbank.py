import os
import csv

# Path to collect data from the Resources folder
main_csv = os.path.join( 'Resources', 'budget_data.csv')
# print (main_csv)
total_months = 0
total_budget = 0 
total_PL = []
PLchanges = []
date =[]

# Read in the CSV file
with open(main_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    header = next(csvreader)
    # print(header)   
    # print(main_csv)
    
       # Loop through the data
    for col in csvreader:
        total_months = total_months + 1
        total_budget = total_budget + int(col[1])
        total_PL.append(col[1])
        date.append(col[0])

    print(total_months)
    print(total_budget)
    # print(PLchanges)
    for indexnum in range(1,len(total_PL)):   
        PLchanges.append(int(total_PL[indexnum])-int(total_PL[indexnum-1]))
    # print(indexnum) 
    # print(PLchanges)
    # print(len(total_PL))

    averagechange = round(sum(PLchanges)/len(PLchanges),2)
    print(averagechange)
    greatestincrease = max(PLchanges)
    greatestdecrease = min(PLchanges)
    increasedate = date[PLchanges.index(greatestincrease)+1]
    decreasedate = date[PLchanges.index(greatestdecrease)+1]
    print(increasedate)
    print(greatestincrease)
    print(decreasedate)
    print(greatestdecrease)
outputfile = os.path.join( 'analysis', 'analysis.txt')
file=open(outputfile,"w") 
file.write(f"Financial Analysis\n")
file.write(f"------------------\n")
file.write(f"Total Months:{total_months}\n")
file.write(f"Total:{total_budget}\n")
file.write(f"Average Change:{averagechange}\n")
file.write(f"Greatest Increase:{increasedate}({greatestincrease})\n")
file.write(f"Greatest decrease:{decreasedate}({greatestdecrease})\n")









