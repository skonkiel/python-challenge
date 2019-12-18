import csv
from statistics import mean
from collections import OrderedDict

with open("./budget_data.csv", 'r') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    # Skip header in file
    csv_header = next(reader)

    # Initialize dict and list for all profits/losses
    data = {}
    p_l = []

    # Create a dict to hold month/profit+loss pairs
    for row in reader:
        data[row[0]] = int(row[1]) 
        p_l.append(int(row[1]))
    
    # The total number of months included in the dataset
    num_months = str(len(data))

    # The average of the changes in "Profit/Losses" over the entire period
    changes = []
    changeMonth = []

    prevMonth = 0
    month = 0

    for x in data:
        month = data[x]
        c = month - prevMonth
        changes.append(c)
        changeMonth.append(x)
        prevMonth = month
    
    changes.pop(0) # Remove the first value because it doesn't count towards average we want to find
    changeMonth.pop(0)

    # Get the average changes over time
    change_avg = mean(changes)
    change_avg = round(change_avg, 2)

    # The net total amount of "Profit/Losses" over the entire period
    net_profit = sum(p_l)
    # print(net_profit)

    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
    # to find greateast increase and decrease, take change and find max/min
    increase = max(changes)
    decrease = min(changes)

    # look for index of increaase and decrease, then match each against list of months  
    in_i = changes.index(increase)
    in_d = changes.index(decrease)

    inc_month = changeMonth[in_i] # Have to add one to each of these indices, as `changes` is one value less than `months`
    dec_month = changeMonth[in_d]        

    print(inc_month, dec_month)   

    # Ready vars for printing
    decrease = str(decrease)
    increase = str(increase)
    monthCount = str(num_months)
    avg_profit = str(change_avg)
    net_profit = str(net_profit)

    # # Print to terminal
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + monthCount)
    print("Total: $" + net_profit)
    print("Average Change: $" + avg_profit)
    print("Greatest Increase in profits: " + inc_month + " ($" + increase + ")")
    print("Greatest Decrease in profits: " + dec_month + " ($" + decrease + ")")

    # # Print to text file

    with open('./analysis.txt', 'w') as writefile:
        writefile.write("Financial Analysis\n")
        writefile.write("------------------\n")
        writefile.write("Total Months: " + monthCount + "\n")
        writefile.write("Total: $" + net_profit + "\n")
        writefile.write("Average Change: $" + avg_profit + "\n")
        writefile.write("Greatest Increase in profits: " + inc_month + " ($" + increase + ")\n")
        writefile.write("Greatest Decrease in profits: " + dec_month + " ($" + decrease + ")")
        writefile.close()