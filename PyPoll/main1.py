#pypoll working file
import os
import csv

a_file = "Resources/election_data.csv"
csvpath= os.path.join(a_file)

candidate_dict = {}
vote_count=[]

#opening csv and using csv.reader to read in data row by row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip header row for read in of data
    header_row = next(csvreader)

    #iterate through csv and create dictionary with candidate and increment value, total for each. Also add list containing all votes for later count
    for ID, county, candidate in csvreader:
        if candidate not in candidate_dict:
            candidate_dict[candidate] = 0
        candidate_dict[candidate] += 1    
        vote_count.append(candidate)
        


#print to terminal results 
print(f'\nElection Results\n-------------------------\nTotal Votes: {len(vote_count)}\n-------------------------')
   
# sorting by total votes and printing results. iterate through sorted dictionary items in descending order(reverse=True) by number of votes (list[1])
for candidate, votes in sorted(candidate_dict.items(), key=lambda list: list[1], reverse=True):
    
    #calculate percent of vote for each candidate
    percent = round((votes/len(vote_count))*100,3)
    print(f'{candidate}: {"%.3f"%percent}% ({votes})') 
    #find max votes to display winner
    elect_winner=max(candidate_dict, key=lambda key: candidate_dict[key])   
print(f'-------------------------')
print(f'The winner is {elect_winner}')
print(f'-------------------------')



#output the results to a text file in the analysis folder

output_summary_file = os.path.join("analysis","election_results.txt")
with open(output_summary_file, "w", newline="") as datafile:

    datafile.write('Election Results')

    datafile.write(f'\n-------------------------\nTotal Votes: {len(vote_count)}\n-------------------------\n')

    # sorting by total votes and printing results
    for candidate, votes in sorted(candidate_dict.items(), key=lambda list: list[1], reverse=True):
    
        #calculate percent of vote for each candidate
        percent = round((votes/len(vote_count))*100,3)
        datafile.write(f'{candidate}: {"%.3f"%percent}% ({votes})\n') 
        #find max votes to display winner
        elect_winner=max(candidate_dict, key=lambda key: candidate_dict[key])   
    
    datafile.write(f'-------------------------\nThe winner is: {elect_winner}\n-------------------------')

