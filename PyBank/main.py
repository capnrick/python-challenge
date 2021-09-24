#pybank working file
import os
import csv


a_file = "Resources/budget_data.csv"
csvpath= os.path.join(a_file)
total_rows = 0
total = 0
top_increase=["",0]
top_decrease=["",9999999999]


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header_row = next(csvreader)
    
    row_zero = next(csvreader)

    #previous_PL_value=int(row[1])

    for row in csvreader:
        #print rows to screen
        print(row)
        #increment counter each time to count number of rows(months)
        total_rows=total_rows+1
        
        
        previou_PL_value=int(row[1])
        #loop through rows and add the second column's values up to get a total 
        total += int(row[1])


         #The greatest increase in profits (date and amount) over the entire period  
        #only do the first comparison
        net_change = int(row[1]) - int(row_zero[1])
        #if net change()> top increase, then net change equal to top increase
        
        

        
            

    #print the total number of months included in the dataset
    print (total_rows)   

    #print the total of all added up profit/loss
    print(f'The total amount of Profit/Loss is {total}')




#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    average_PL = total/total_rows
    print (average_PL)


#The greatest decrease in profits (date and amount) over the entire period
#in addition, your final script should both print the analysis to the terminal and export a text file with the results.


# Specify the file to write to
output_path = os.path.join("analysis/results.txt")


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:
    months=str(total_rows)
    average=str(average_PL)
    totals=str(total)
    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    #file.write(['First Name', 'Last Name', 'SSN'])
    file.write("Financial Analysis \n")
    file.write("---------------------------- \n")
    file.write("Total Months: ")
    file.write(months)
    file.write ("\n")
    file.write("Total: $")
    file.write(totals)
    file.write ("\n")
    file.write("Average Change: $")
    file.write(average)
   

#sample output
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
