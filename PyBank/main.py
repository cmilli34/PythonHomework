#Bank 
#by Caroline Miller

#first import the csv file into the environment
import csv

date = []
profit = []
change_profit = []
with open('budget_data2.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #remove the headers
    next(csvreader, None)

    for row in csvreader:

        date.append(row[0])
        
        profit.append(int(row[1]))

    #then, find a way to sum the time elapsed in months for the date column and store it as a variable to print later
    mymonth = set(date)
    total_months = len(mymonth)

    #loop that adds up each value in the profit column w a counter
    sum_profit = sum(profit)

    #sum of the change of profit divided by length of change of profit
    for i in range(0, len(profit) -1):
        change_profit.append(int(profit[i+1]) - int(profit[i]))
    avg_profit_change = sum(change_profit)/len(change_profit)
    #round average to two decimal places
    avg_profit_change = round(avg_profit_change, 2)

    #find max for CHANGE IN REVENUE, store as var to print later
    max_profit = max(change_profit)
    max_date = date[change_profit.index(max_profit) + 1]
    print(max_date)
    #find min for change of profits, store as var to print later
    min_profit = min(change_profit)
    min_date = date[change_profit.index(min_profit) + 1]

#print every single variable with the format asked (below)

print("Financial Analysis")
print('----------------------------')
print('Total Months: ' + str(total_months))
print('Total: $' + str(sum_profit))
print('Average  Change: $' + str(avg_profit_change))
print('Greatest Increase in Profits: ' + max_date + ' $' +str(max_profit))
print('Greatest Decrease in Profits: ' + min_date + ' $' + str(min_profit))

#put path
#write file as a text
#to set directory: cd Documents/Github/PythonHomework/PyBank python main.py

path = '/Users/carolinemiller/Documents/Github/PythonHomework/PyBank/bankresults.txt'

with open(path, "w", newline = '') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write('----------------------------\n')
    txtfile.write('Total Months: ' + str(total_months) + '\n')
    txtfile.write('Average  Change: $' + str(avg_profit_change) + '\n')
    txtfile.write('Greatest Increase in Profits: ' + max_date + ' $' +str(max_profit) + '\n')
    txtfile.write('Greatest Decrease in Profits: ' + min_date + ' $' + str(min_profit) + '\n')