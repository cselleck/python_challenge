#import packages
import csv
import os

#read data
#csvpath = os.path.join('budget_data_files', 'budget_data.csv')
with open('budget_data.csv') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  #skip the header
  next(csvreader, None)


  #Initialize Variables
  line = next(csvreader,None)
  months=0
  revenue=0
  max_month = line[0]
  min_month = line[0]
  revenue = float(line[1])
  min_revenue = revenue
  max_revenue = revenue
  previous_revenue = revenue
  month_counter = 1
  sum_revenue = float(line[1])
  sum_revenue_change = 0
  row_count = 1


# Start a loop to run calculations on the list
  for line in csvreader:

      #Get the revenue
      revenue = float(line[1])
      
      #add 1 to the row count
      row_count= row_count + 1

      # Add to sum of revenue for data set
      sum_revenue = sum_revenue + revenue

      # Find change in revenue between this month and last month
      revenue_change = revenue - previous_revenue

      # Add change in revenue to net change in revenue for data set
      sum_revenue_change = sum_revenue_change + revenue_change

      # Check to see if max and min need to be updated
      if revenue_change > max_revenue:
          max_month = line[0]
          max_revenue = revenue_change
          
      if revenue_change < min_revenue:
            min_month = line[0]
            min_revenue = revenue_change
           
        # Set previous revenue to current revenue for the next iteration
      previous_revenue = revenue
      
      # Finish calculations
average_revenue = sum_revenue/row_count
average_revenue_change = sum_revenue_change/(row_count-1)

# Round decimal
sum_revenue = int(sum_revenue)
average_revenue_change = int(average_revenue_change)
max_revenue = int(max_revenue)
min_revenue = int(min_revenue)


# Specify the file to write to
output_path = os.path.join("PyBank.txt")

# opens the output destination in write mode and prints the summary
with open(output_path, 'w') as writefile:

    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(row_count) + '\n')
    writefile.writelines('Total Revenue: $' + str(sum_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_revenue_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + max_month + ' ($' + str(max_revenue) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + min_month + ' ($' + str(min_revenue) + ')')

#opens the output file in r mode and prints to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())




