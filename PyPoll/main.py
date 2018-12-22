#Poll
#by Caroline Miller

#first import the csv into the environment
voter_id = []
county = []
candidate = []

import csv
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #remove the headers
    next(csvreader, None)

    for row in csvreader:

    #convert columns into lists so they can be manipulated
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    
    #find total number of votes by counting how long the voter id column is, store as var to print later
    total_votes = len(voter_id)

    #get unique values of candidates with set function, store as var to print later
    candidate_names = set(candidate)

    #find out volume of votes for each candidate
    khan_volume = candidate.count("Khan")
    correy_volume = candidate.count("Correy")
    li_volume = candidate.count("Li")
    otooley_volume = candidate.count("O'Tooley")

    #percentage of votes each candidate won
     #round percentage so there's three decimal places
    k_percentage = (khan_volume/len(candidate)) * 100
    khan_percentage = round(k_percentage, 3)

    c_percentage = (correy_volume/len(candidate)) * 100
    correy_percentage = round(c_percentage, 3)

    l_percentage = (li_volume/len(candidate)) * 100
    li_percentage = round(l_percentage, 3)

    o_percentage = (otooley_volume/len(candidate)) * 100
    otooley_percentage = round(o_percentage, 3)

    #find winner of election by making list of all vote counts then running an if statement
    candidate_votes = [khan_volume, correy_volume, li_volume, otooley_volume]

    if max(candidate_votes) == khan_volume:
        winner = "Khan"
    elif max(candidate_votes) == correy_volume:
        winner = "Correy"
    elif max(candidate_votes) == li_volume:
        winner = "Li"
    else:
        winner = "O'Tooley"


    #print results

    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + str(total_votes))
    print('-------------------------')
    print('Khan: ' + str(khan_percentage) +  '%' + ' (' + str(khan_volume) + ')')
    print('Correy: ' + str(correy_percentage) +  '%' + ' (' + str(correy_volume) + ')')
    print('Li: ' + str(li_percentage) + '%' + ' (' + str(li_volume) + ')')
    print("O'Tooley: " + str(otooley_percentage) + '%' + ' (' + str(otooley_volume) + ')')
    print('-------------------------')
    print('Winner: ' + winner)

    #copy path
    #export as text file