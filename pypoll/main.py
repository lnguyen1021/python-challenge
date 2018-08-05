'''
OBJECTIVE
1) calculate the total number of votes
2) make a list of all candidates in dataset
3) count number of votes per candidate
4) calculate the percentages of votes for each candidate
5) print out candidate based on popular vote

DATAFRAME
data is from a csv file
there are 3 columns
column 0: Voter ID (unique values)
column 1: County
column 2: Candidate that they voted for

VARIABLES:
totalVotes = stores the total number of votes
candidateDictionary = stores the candidates name(key) and the number of votes(value)
percentVotes = stores the percentages of votes per candidate (vote of candidate/totalVotes)

CONDITIONALS
First need to open and read the file

For loop that will loop through the file and create a nested list 
[['voter id','county','candidate'],['voter id','county','candidate'], .....]
totalVotes = count the number of votes (since there is a unique id for everyone should be the # of rows in the dataset)

For loop that creates another list of just the candidates and sorts this list
candidateList = [['candidate1'],['candidate1'],['candidate1'],...,['candidate2'],['candidate2']...]

somehow create a dicitonary from the candidateList and count the number of times the candidate's name shows up

from the dictionary: take each value from each candidate and divide that value by the totalVotes
store the value in a list called percentVotes

'''
import os
import csv
#File should be stored in the same folder
path = ('election_data.csv')

with open (path, newline = '') as f:
    reader = csv.reader(f, delimiter = ",")
    data = list(reader)
    data.pop(0)
    from operator import itemgetter
    #sort data set based on index 2 or the 3rd column using the itemgetter function
    data.sort(key = itemgetter(2))
    
    #storing the total number of votes
    totalVotes = len(data)

    #make a list of candidates by only appending the candidates column
    candidateList = []
    for x in data:
        candidateList.append(x[2])
    
    #make a dictionary of candidate names and counts the number of times candidate's name appears in the candidateList
    candidateDict = {}
    for candidate in candidateList:
        #from the candidateList if the candidate is not in the candidateDict. add candidate to the dictionary, assigns the value 0
        #if they are then add 1 to the value every time they come up in the candidateList
        if candidate not in candidateDict:
            candidateDict[candidate] = 0
        candidateDict[candidate]+=1
    
    #from the candidateDict create a new list (valueL) with the value pair 
    valuesL = list(candidateDict.values())
    
    #using the valuesL. loop through each value and divides it by the totalVotes and appends those values to the percentageVote list
    percentageVote = []
    for v in valuesL:
        percentageVote.append((v/totalVotes)*100)
    #formatting the percentageVote list to only two decimals using list comprehension
    percentageVote =["%.2f"%x for x in percentageVote]
    
    #creates a list of tuples with (_candidateName_,_numberOfVotes_,percentageOfVotes) using zip then typecasts to list
    candidateTups = list(zip(candidateDict, valuesL, percentageVote))
    
    #since i sorted the data in the beginning i dont have to worry about the values in each list getting mixed up
    #the all the lists that are returned stay in the same order
    
    
    #prints the candidate with the most number of votes based on index 1(numberOfVotes)
    winner = (max(candidateTups,key =lambda x:x[1]))

    print('Election Results')
    print('-------------------------')
    print('Total Votes: '+ str(totalVotes))
    print('-------------------------')
    print('Candidate: '+candidateTups[0][0]+' | '+ str(candidateTups[0][2])+('% ')+ '('+(str(candidateTups[0][1]))+')')
    print('Candidate: '+candidateTups[1][0]+' | '+ str(candidateTups[1][2])+('% ')+ '('+(str(candidateTups[1][1]))+')')
    print('Candidate: '+candidateTups[2][0]+' | '+ str(candidateTups[2][2])+('% ')+ '('+(str(candidateTups[2][1]))+')')
    print('Candidate: '+candidateTups[3][0]+' | '+ str(candidateTups[3][2])+('% ')+ '('+(str(candidateTups[3][1]))+')')
    print('-------------------------')
    print('Winner of the Election: '+ str(winner[0]))

    #printing answers to a file called pollscript.txt
    file = open('pollscript.txt','w')
    file.write('Election Results \n')
    file.write('------------------------------- \n')
    file.write('Total Votes: '+ str(totalVotes)+'\n')
    file.write('------------------------------- \n')
    file.write('Candidate: '+candidateTups[0][0]+' | '+ str(candidateTups[0][2])+('% ')+ '('+(str(candidateTups[0][1]))+')'+'\n')
    file.write('Candidate: '+candidateTups[1][0]+' | '+ str(candidateTups[1][2])+('% ')+ '('+(str(candidateTups[1][1]))+')'+'\n')
    file.write('Candidate: '+candidateTups[2][0]+' | '+ str(candidateTups[2][2])+('% ')+ '('+(str(candidateTups[2][1]))+')'+'\n')
    file.write('Candidate: '+candidateTups[3][0]+' | '+ str(candidateTups[3][2])+('% ')+ '('+(str(candidateTups[3][1]))+')'+'\n')
    file.write('-------------------------------\n')
    file.write('Winner of the Election: '+ str(winner[0]))
    file.close()