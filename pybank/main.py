#Procedural thinking
'''
OBJECTIVE
1) calculate total number of months in the dataset
2) calculate net profit/loss for the whole period
3) calculate greatest profit increase
3a) also grabbing the corresponding date
4) calculate the greatest profit decrease
4) also grabbing the corresponding date
5) calculate average change per month

DATAFRAME
The dataset is from a csv file
there are 2 columns in the dataset
column 0: date 
column 1: profit/loss 
the datatypes are all strings for both columns

VARIABLES
totalMonths = stores number of months(which is the number of rows in the dataset) (integer)
greatestIncrease = stores the greatest increase in profits (integer)
dateOfGreatestIncrease = stores the date with the greatest increase of profit (string)
greatestDecrease = stores the greatest decrease in profits (integer)
dateOfGreatestDecrease = stores the date with the greatest decrease of profit (string)
averageChange = stores the average change/month (total revenue / total months)
totalRevenue = stores the total revenue for the dataset 

CONDITIONALS
First need to open,read, and store the csv file as a variable

For loop that will loop over the rows in the dataset:
-add each value from index 1 to totalRevenue
-count the number of rows to find the totalMonths
-calculates averageChange = totalRevenue/totalMonths

    if statement that compares the current value and checks if it is smaller/larger than the greatestDecrease/greatestIncrease
    -updates the current value of greatestIncrease/greatestDecrease to the current value
    -updates the current value of dateOfGreatestIncrease/dateOfGreatestDecrease with current date value

'''

import csv
#************************MAY NEED TO CHANGE THE PATH SO IT WORKS WHEREVER ASK ALBERT***************
path = '/Users/linh/Documents/GT/Homework/HW3/PyBank/budget_data.csv'
with open (path, newline = '') as f:
    reader = csv.reader(f, delimiter = ",")
    data = list(reader)
    data.pop(0)
    
    #variables
    totalMonths = (len(data))
    revList = []
    totalRev=0
    greatestI = 0
    dateI = ""
    greatestD = 0
    dateD = ""
    averageChange = 0
    
    #Conditionals
    #goes through rows in the data
    for row in data:
        #for each row, go to row 1 and append the integer value to revList
        revList.append(int(row[1]))

        #from the revList add the value into the profitloss variable
        totalRev = sum(revList)

        #averageChange is profitloss / totalMonths
        averageChange = totalRev/totalMonths

        #finding the greatest profit value and the corresponding date
        if int(row[1]) > greatestI:
            greatestI = int(row[1])
            dateI = row[0]

        #finding the least profit value and the corresponding date
        if int(row[1]) < greatestD:
            greatestD = int(row[1])
            dateD = row[0]


    print('Financial analysis')
    print('-------------------------------')
    print('Total Months: ' +str(totalMonths))
    print('Total Revenue: $' + str(totalRev))
    print('Average change: $'+ '{:.2f}'.format(averageChange))
    print('Greatest Increase in Profit: ' + str(dateI)+ '($'+str(greatestI)+')')
    print('Greatest Decrease in Profit: ' + str(dateD)+ '($'+str(greatestD)+')')
    print('-------------------------------')
    #NEED TO ASK HOW TO EXPORT TXT FILE