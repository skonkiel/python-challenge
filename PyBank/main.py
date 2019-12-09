import csv

with open("./budget_data.csv", 'r') as inputfile:
    reader = csv.reader(inputfile, delimiter=',')

    # Skip header in file
    csv_header = next(reader)

    monthCount = 0
    profit_loss_list = [] 
    avg_profit = 0
    increase = 0
    inc_month = ""
    decrease = 0
    dec_month = ""

    for row in reader:
        m = row[0]
        p_l = int(row[1])

        # The total number of months included in the dataset
        monthCount += 1
        profit_loss_list.append(p_l) # Adding that month's p/l to a list 

        # The greatest increase in profits (date and amount) over the entire period
        # Compare each new addition to the last added value; if greater than x (stored), make x
        if increase < p_l:
            increase = p_l
            inc_month = m
        # The greatest decrease in losses (date and amount) over the entire period
        elif decrease > p_l:
            decrease = p_l
            dec_month = m
        else:
            pass



        
 
       
            

    # The average of the changes in "Profit/Losses" over the entire period
    # To calculate: Get first value of profit_loss_list, subtract from last value, divide by monthCount
    start_val = profit_loss_list[0]
    end_val = profit_loss_list[-1]
    net_profit = end_val - start_val
    avg_profit = (end_val - start_val) / monthCount

    decrease = str(decrease)
    increase = str(increase)

    # Print to terminal
    print("Financial analysis")
    print("------------------")
    print("Months: " + str(monthCount))
    print("Net total amount of profit/loss over entire period: $" + str(net_profit))
    print("Average profit / loss over entire period (profit/loss per month): $" + str(avg_profit))
    print("Greatest increase: " + inc_month + ", $" + increase)
    print("Greatest decrease: " + dec_month + ", $" + decrease)

    # Print to text file

    with open('./analysis.txt', 'w') as writefile:
        writefile.write("Financial analysis\n")
        writefile.write("------------------\n")
        writefile.write("Months: " + str(monthCount) + "\n")
        writefile.write("Net total amount of profit/loss over entire period: $" + str(net_profit) + "\n")
        writefile.write("Average profit / loss over entire period (profit/loss per month): $" + str(avg_profit) + "\n")
        writefile.write("Greatest increase: " + inc_month + ", $" + increase + "\n")
        writefile.write("Greatest decrease: " + dec_month + ", $" + decrease)
        writefile.close()