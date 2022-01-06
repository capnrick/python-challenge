#pypoll working file
import os
import csv


a_file = "Resources/election_data.csv"
csvpath= os.path.join(a_file)


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
      
    #header row is not being read
    header_row = next(csvreader)



    #intialize arrays for columns in csv in order Voter ID,County,Candidate
    
    voter_id=[]
  
    county=[]
    candidates=[]
    correy=[]
    khan=[]
    li=[]
    otooley=[]


    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])




    num_votes=len(voter_id)
    print (num_votes)
    remainder_candidates=0
    for candidate in candidates:
        if candidate=='Khan':
            khan.append(candidate)

        else:

            remainder_candidates=remainder_candidates+1
            
    num_khan_votes=len(khan)
    print(num_khan_votes)

    print(remainder_candidates)