import os
import csv

# Path to collect data from the Resources folder
main_csv = os.path.join( 'Resources','election_data.csv')
# print (main_csv)
totalvotes = 0 
total_votes = []
khanvotes = 0 
correyvotes = 0
livotes = 0 
otooleyvotes = 0
khan = []
correy= []
li= []
otooley=[]
candidate = []


# Read in the CSV file
with open(main_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    header = next(csvreader)

    for col in csvreader:
        totalvotes = totalvotes + 1 
        total_votes.append(int(col[0]))
        candidate.append(col[2])
        if col[2] == "Khan":
            khan.append(candidate)   
            khanvotes = len(khan)
        elif col[2] == "Correy":
            correy.append(candidate)
            correyvotes = len(correy)    
        elif col[2] == "Li":
            li.append(candidate)
            livotes = len(li)
        else: 
            otooley.append(candidate)
            otooleyvotes = len(otooley)      
    print(len(total_votes))
    print(f"Election Reults")
    print(f"---------------")
    print(f"Total Votes: {len(total_votes)}")
    print(f"---------------")
    # print(khanvotes,correyvotes,livotes,otooleyvotes)           
    # finding candidate maximum vote 
    highestvote = max(khanvotes,correyvotes,livotes,otooleyvotes)
    # print(highestvote)
    if highestvote == khanvotes:
       winner = "Khan"
    elif highestvote == correyvotes:
       winner = "Correy" 
    elif highestvote == livotes:
       winner = "li"
    else: 
        winner = "otooley"
    
    
#calculating percent

    khanpercent = khanvotes / totalvotes
    correypercent = correyvotes / totalvotes
    lipercent = livotes / totalvotes
    otooleypercent = otooleyvotes / totalvotes

    print(f"Khan: {khanpercent: .3%} ({khanvotes})") 
    print(f"Correy: {correypercent: .3%} ({correyvotes})") 
    print(f"Li: {lipercent: .3%} ({livotes})") 
    print(f"O'Tooley: {otooleypercent: .3%} ({otooleyvotes})") 
    print(f"---------------")  
    print(f"Winner: {winner}")
        



