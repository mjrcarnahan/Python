import os
import csv

election_csv = os.path.join('03-Python','Homework','Instructions','PyPoll','Resources','election_data.csv')


# Lists to store data

voterid = []
candidate = []
khan_total = 0
correy_total = 0
li_total = 0 
otooley_total = 0

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in csvreader:
        # Add date
        voterid.append(row[0])
	    # Add profit/loss
        candidate.append(row[2])
        # calculate total votes
        totalvotes = int(len(voterid))
        
    print(type(candidate))
    print(candidate[1])
    for i in range(len(candidate)):
        if (candidate[i] == "Khan"):
            khan_total = khan_total + 1
        elif (candidate[i] == "Correy"):
            correy_total = correy_total + 1
        elif (candidate[i] == "Li"):
            li_total = li_total + 1
        elif (candidate[i] == "O'Tooley"):
            otooley_total = otooley_total + 1

    totals = []
    totals.append(khan_total)
    totals.append(correy_total)
    totals.append(li_total)
    totals.append(otooley_total)

    percentages = []
    percentages = [x / totalvotes for x in totals]
    percentages = [i*100 for i in percentages]
    percentages = [round(i, 2) for i in percentages]    
    

    # create dictionary
    candidates_total = {
    "Khan": [percentages[0], totals[0]],
    "Correy": [percentages[1], totals[1]],
    "Li": [percentages[2], totals[2]],
    "O'Tooley": [percentages[3], totals[3]],
    }

    #start printing
    print("Election Results")
    print("--------------------------")
    print("Total Votes: " + str(totalvotes))
    print("--------------------------")

    # Find winner
    listofTuples = sorted(candidates_total.items() , reverse=True, key=lambda x: x[1])
    for elem in listofTuples:
        print(elem[0] , ":" , elem[1])

    print("--------------------------")
    print("Winner: " + listofTuples[0][0])
    print("--------------------------")