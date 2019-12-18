import csv
from collections import defaultdict

with open("./election_data.csv", 'r') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    # Skip header in file
    csv_header = next(reader)
    
    vote = {}
    pct_vote = {}
    total_votes = 0
    master = {}
  
    # Tally votes for each candidate
    for row in reader:
        candidate = row[2]
        if candidate in vote:
            vote[candidate] += 1
        else:
            vote[candidate] = 1
    
#     vote = {k: v for k, v in sorted(vote.items(), key=lambda item: item[1], reverse=True)} # Adapted from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    
    # Get the votes for each candidate, tally total votes
    for c in vote:
        total_votes += vote[c]

    # Get pct votes for each candidate
    for c in vote:
        pct = 0
        pct = vote[c] / total_votes
        pct = "%.3f%%" % (pct * 100)
        # Code adapted from a solution suggested here: https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python
        pct_vote[c] = str(pct)
        c = str(c) 

#     # Print to terminal
#     print("Election results")
#     print("------------------") 

#     # Print total votes

#     print("Total Votes: " + str(total_votes))
#     print("------------------") 

    winner = ""
    comparison = 0

#     # Combine the dicts into one, print candidate totals

    # final_tally = {}

    for same in vote.keys() & pct_vote.keys():
        name = same
        pct_name = pct_vote[same]
        vote_name = vote[same]
        # print(name + ": " + pct_name + " (" + str(vote_name) + ")")    
        if vote_name > comparison:
            comparison = vote_name
            winner = name
        else:
            pass

    # final_tally = {k: v for k, v in sorted(final_tally.items(), key=lambda item: item[1], reverse=True)} # Adapted from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
    

#     print("------------------") 
#     print("Winner: " + winner)
#     print("------------------") 
 
#    # Print to text file

#     # with open('./analysis.txt', 'w') as writefile:
#     #     writefile.write("Election results\n")
#     #     writefile.write("------------------\n")
#     #     writefile.write("Total Votes: " + str(total_votes) + "\n")
#     #     writefile.write("------------------\n")

#     #     for same in vote.keys() & pct_vote.keys():
#     #         name = same
#     #         pct_name = pct_vote[same]
#     #         vote_name = vote[same]
#     #         writefile.write(name + ": " + pct_name + " (" + str(vote_name) + ")\n")    
#     #         if vote_name > comparison:
#     #             comparison = vote_name
#     #             winner = name
#     #         else:
#     #             pass

#     #     writefile.write("------------------\n") 
#     #     writefile.write("Winner: " + winner + "\n")
#     #     writefile.write("------------------\n") 

#     #     writefile.close()