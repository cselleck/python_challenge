<<<<<<< HEAD
#import packages
import csv
import os

#read data

with open('election_data.csv') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  
  #skip the header
  next(csvreader)



#initialize variables
  cand_votes = {}
  cand_percent= {}
  votes_cast=0
  winner_votes = 0
  winner=""



#assign a dictionary for the results

  results = {}
  cand_list = []

  #start the iteration
  for row in csvreader:
      votes_cast = votes_cast + 1
      name= row[2]
      if not name in cand_list:
        cand_list.append(name)
        results[name] = 1
      else: 
        results[name] = results[name] + 1

# calculate vote percentage and identify winner
for person, vote_count in results.items():
    cand_percent[person] = '{0:.0%}'.format(vote_count / votes_cast)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

# print out results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {votes_cast}")
print("----------------------------")
for person, vote_count in results.items():
    print(f"{person}: {cand_percent[person]} ({vote_count})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#print to file

output_path = os.path.join("PyPoll.txt")

with open(output_path,'w') as text:
    text.write("----------------------------" + "\n")
    text.write(f"Total Votes: {votes_cast}" + "\n")
    text.write("----------------------------" + "\n")
    for person, vote_count in results.items():
        text.write(f"{person}: {cand_percent[person]} ({vote_count})" + "\n")
    text.write("----------------------------" + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write("----------------------------" + "\n")


=======
#import packages
import csv
import os

#read data

with open('election_data.csv') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  
  #skip the header
  next(csvreader)



#initialize variables
  cand_votes = {}
  cand_percent= {}
  votes_cast=0
  winner_votes = 0
  winner=""



#assign a dictionary for the results

  results = {}
  cand_list = []

  #start the iteration
  for row in csvreader:
      votes_cast = votes_cast + 1
      name= row[2]
      if not name in cand_list:
        cand_list.append(name)
        results[name] = 1
      else: 
        results[name] = results[name] + 1

# calculate vote percentage and identify winner
for person, vote_count in results.items():
    cand_percent[person] = '{0:.0%}'.format(vote_count / votes_cast)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

# print out results
print("Election Results")
print("----------------------------")
print(f"Total Votes: {votes_cast}")
print("----------------------------")
for person, vote_count in results.items():
    print(f"{person}: {cand_percent[person]} ({vote_count})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#print to file

output_path = os.path.join("PyPoll.txt")

with open(output_path,'w') as text:
    text.write("----------------------------" + "\n")
    text.write(f"Total Votes: {votes_cast}" + "\n")
    text.write("----------------------------" + "\n")
    for person, vote_count in results.items():
        text.write(f"{person}: {cand_percent[person]} ({vote_count})" + "\n")
    text.write("----------------------------" + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write("----------------------------" + "\n")


>>>>>>> c47309594e78456ef878e0723d42465cbd96e705
