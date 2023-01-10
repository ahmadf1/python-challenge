import os
import csv
import operator
import sys

votes =[]
count = 0
peopleVotes = {}
winner = 0

def setPeopleVotes(key):
    if key not in peopleVotes.keys():
        peopleVotes[key] = 1
    else:
        total = peopleVotes[key] + 1
        peopleVotes[key] = total
    #print(str(key), ": " + "(" + str(peopleVotes[key]) + ")")


csvpath = os.path.join("..", "Resources", "election_data.csv")
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #count = sum(1 for row in csvreader) - 1
    
    next(csvreader)
    for x in csvreader:
        #if x[0] == "Ballot ID":
        #    continue

        count += 1
        setPeopleVotes(x[2])
       
    print("Election Results")
    print("-----------------------------------------------------------")

    print("Total Votes : ", str(count))
    print("-----------------------------------------------------------")

    for x in peopleVotes.keys():
        
        percentVotes = peopleVotes[x] * 100/count
        print(str(x), ": " + "%.3f ." % percentVotes +"(" + str(peopleVotes[x]) + ")")
    
    print("-----------------------------------------------------------")
    winner = max(peopleVotes, key=lambda key: peopleVotes[key])
    print("Winner: ", winner)
    print("-----------------------------------------------------------")
    
    
    stdoutOrigin=sys.stdout 
    sys.stdout = open("out.txt", "w")
    sys.stdout.close()
    sys.stdout=stdoutOrigin

    