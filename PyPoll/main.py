import csv
from collections import defaultdict

with open("./election_data.csv", 'r') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    # Skip header in file
    csv_header = next(reader)
    # ['Voter ID', 'County', 'Candidate']

    results = []
    total_votes = 0

    k = {'name': 'Khan', 'votes': 0}
    l = {'name' : 'Li', 'votes': 0}
    c = {'name': 'Correy', 'votes': 0}
    o = {'name': "O\'Tooley", 'votes': 0}

    # Count votes for each candidate
    for row in reader:
        if row[2] == "Khan":
            k['votes'] += 1
            total_votes += 1
        elif row[2] == "Li":
            l['votes'] += 1
            total_votes += 1
        elif row[2] == "Correy":
            c['votes'] += 1
            total_votes += 1
        elif row[2] == "O\'Tooley":
            o['votes'] += 1
            total_votes += 1
        else: 
            pass

    # Append each dict to a list, to loop through dicts
    results.append(k)
    results.append(l)
    results.append(c)
    results.append(o)
    
    # Tally percentage of vote for each candidate
    for d in results:
        d['pct'] = (d['votes'] / total_votes)
        d['pct'] = "%.3f%%" % (d['pct'] * 100)
        # Code adapted from a solution suggested here: https://stackoverflow.com/questions/5306756/how-to-print-a-percentage-value-in-python
        d['pct'] = str(d['pct'])
    
    # print(results)

    sorted_results = []
    sorted_results = sorted(results, key = lambda i: i['votes'], reverse=True) # Adapted from https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/

    # Print to terminal
    print("Election results")
    print("------------------") 

    # Print total votes

    print("Total Votes: " + str(total_votes))
    print("------------------") 

    # Print the results, formatted
    for d in sorted_results:
        print(d['name'] + ': ' + d['pct'] + ' (' + str(d['votes']) + ')')


    print("------------------") 
    print("Winner: " + sorted_results[0]['name'])
    print("------------------") 
 
# Print to text file

with open('./analysis.txt', 'w') as writefile:
    writefile.write("Election results\n")
    writefile.write("------------------\n")
    writefile.write("Total Votes: " + str(total_votes) + "\n")
    writefile.write("------------------\n")

    for d in sorted_results:
        writefile.write(d['name'] + ': ' + d['pct'] + ' (' + str(d['votes']) + ')\n')

    writefile.write("------------------\n") 
    writefile.write("Winner: " + sorted_results[0]['name'] + "\n")
    writefile.write("------------------\n") 

    writefile.close()