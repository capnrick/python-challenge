#pybank working file
import os
import csv


a_file = "Resources/budget_data.csv"
csvpath= os.path.join(a_file)
total_rows = 0
total = 0
profit_loss=[]
date_list=[]


#open the csv file and begin reading in files
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #header row is not being read
    header_row = next(csvreader)
    

    #loop through csvfile to obtain number of months and to add up all values
    for row in csvreader:
        #print rows to screen to verify data is being read
        print(row)
               
        #store values into array called profit_lossand date_list, start at second row to skip header
        date_list.append(row[0])
        profit_loss.append(row[1])
        

        #add up all the values in the profit and loss columns and save net total  to variable 'total'
        #same as writing total= total + int(row[1])
        total+= int(row[1])
    
    #calculate and print the total number of months included in the dataset and net profit/loss
    total_rows=len(profit_loss)
    print(f'The total number of months is {total_rows}') 
    print(f'The total net amount of Profit/Loss over the entire period is ${total}')

    sum_changes=0
    greatest_increase=0
    greatest_decrease=0
    #Calculate the changes in Profit/Losses" over the entire period, then find the average of those changes
    for month in range(1,total_rows):
        
       

        #find the change in pnl from month to month
        monthly_change = int(profit_loss[month])-int(profit_loss[month-1])
        #print(monthly_change)
    
        sum_changes +=monthly_change

        #average of all monthly changes
        average_changes=(sum_changes/(total_rows-1))
        

    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period

        if(monthly_change > greatest_increase):
            greatest_increase=monthly_change
            greatest_increase_month=date_list[month]
        elif (monthly_change < greatest_decrease):
            greatest_decrease=monthly_change
            greatest_decrease_month=date_list[month]    


   
          
print(f'The average of the changes in Profit/Loss is ${round(average_changes,2)}')
print(f"Greatest Increase in Profits:{greatest_increase_month} ${greatest_increase}")
print(f"Greatest Decrease in Profits:{greatest_decrease_month} ${greatest_decrease}")
#in addition, your final script should both print the analysis to the terminal and export a text file with the results.




#-------writing to the results to a text file--------------------------------
# Specify the file to write to
output_path = os.path.join("analysis/results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:
    months=str(total_rows)
    average=str(round(average_changes,2))
    totals=str(total)
    greatest_increase=str(greatest_increase)
    greatest_decrease=str(greatest_decrease)

#write stored variables to file to be called results.txt
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
    file.write ("\n")
    file.write("Greatest Increase in Profits:")
    file.write(greatest_increase_month)
    file.write(" $")
    file.write(greatest_increase)
    file.write ("\n")
    file.write("Greatest Decrease in Profits:")
    file.write(greatest_decrease_month)
    file.write(" $")
    file.write(greatest_decrease)
    
   

#sample output
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
