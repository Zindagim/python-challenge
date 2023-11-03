# Modules
import os
import csv

votes_list=[0]
county_list=[1]

# Set path for file
csvpath = os.path.join( "Resources", "election_data.csv")
# Open the CSV using the UTF-8 encoding
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    print(len(list(csvreader)))
    county_list.append(len[1])

    
   
    



   