#Bank 

#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#first import the csv file into the environment
import os
import csv
import pandas as pd

with open('budget_data.csv', newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:

#then, find a way to sum the time elapsed in months for the date column and store it as a variable to print later
#make a sum function for all of the data in the profit column and store in var to print later
#avg function just like above, again stored as a variable
#find max for profits, store as var to print later
#find min for profits, store as var to print later
#print every single variable with the format asked
#write file as a .txt