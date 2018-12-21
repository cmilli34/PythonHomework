#Bank 

#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#first import the csv file into the environment
import csv
import pandas as pd
import math
import datetime


with open('budget_data.csv', newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:

        Date = row[0]
        print(Date)

        Profit = row[1]
        print(Profit)

#then, find a way to sum the time elapsed in months for the date column and store it as a variable to print later
        #datetime stuff
#for loop that adds up each value in the profit column w a counter
        rowcoutner = 0
        print(sum_profit)
#build an average function
#avg function just like above, again stored as a 
        #avg_profit = sum_profit/len(Profit)
        #print(avg_profit)
#find max for profits, store as var to print later
        #max_profit = max(Profit)
        #print(max_profit)
#find min for profits, store as var to print later
        #min_profit = min(Profit)
        #print(min_profit)
#print every single variable with the format asked (below)
  #Financial Analysis
  #print('----------------------------')
  # print('Total Months: ' + months)
  # print('Total: ' + sum_profit)
  # print('Average  Change: ' + avg_profit)
  # print('Greatest Increase in Profits: ' + max_profit)
  # print('Greatest Decrease in Profits: ' + min_profit)

#write file as a text
# to set directory: cd Documents/Github/PythonHomework/PyBank
