import os
import csv

csvpath = 'election_data.csv';

#lists
candidate_names = []
candidate = []
candidate_votes = []
candidate_percent = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')   
    header = next(csvreader)
    #print(header)

    total_votes = 0
    candidate_total = 0

    for row in csvreader:
        total_votes += 1
        
        candidate_names.append(row[2])

    for name in set(candidate_names):    
        candidate.append(name)
        candidate_total = candidate_names.count(name)
        candidate_votes.append(candidate_total)
        percent = (candidate_total/total_votes) * 100
        candidate_percent.append(round(percent))

    winner_count = max(candidate_votes)
    winner_name = candidate[candidate_votes.index(winner_count)]


    print("Election Results")
    print("------------------------")
    print("Total Votes: " + str(total_votes))
    print("------------------------")
    for row in range(len(candidate)):
        print(candidate[row] + ":  " + str(candidate_percent[row]) + "%  " + "(" + str(candidate_votes[row]) + ")")
    print("------------------------")   
    print("Winner: " + str(winner_name))
    print("------------------------")        

    #text file printing

    results = os.path.join('election_results.txt')

    with open (results, "w") as txtfile:

        txtfile.write("Election Results")    
        txtfile.write("\n------------------------")
        txtfile.write(f"\nTotal Votes: {total_votes}")
        txtfile.write("\n------------------------")
        for row in range(len(candidate)):
            txtfile.write(f"\n{candidate[row]}: {candidate_percent[row]}% {candidate_votes[row]}")
        txtfile.write("\n------------------------")   
        txtfile.write(f"\nWinner: {winner_name}")
        txtfile.write("\n------------------------")   