import os 
import csv

#Paths to directories
electionpath = os.path.join("Resources","election_data.csv")
save_path = os.path.join("Analysis")

#Opening file
with open(electionpath) as electionfile:
    
    #Read the File
    electionreader = csv.reader(electionfile, delimiter = ',')

    #Skip Header
    next(electionreader)
    
    #defining variables
    total_votes = int()
    candidates = []
    candidate_votes = []
    vote_count = {}
    election_winner = ""

    
    #Looping through file to populate variables above
    for row in electionreader:
        #Count total votes in file
        total_votes += 1
        #Creating list of contained with all vote results
        candidate_votes.append(row[2])
        #Find unique candidates
        if row[2] in candidates:
            continue
        else:
            candidates.insert(0,row[2])

    #Counting votes for each candidate in the candidate_votes list  
    vote_count[candidates[0]] = candidate_votes.count(candidates[0])
    vote_count[candidates[1]] = candidate_votes.count(candidates[1])
    vote_count[candidates[2]] = candidate_votes.count(candidates[2])
    
    #Calculating election winner
    election_winner = max(vote_count, key = vote_count.get)

#Printing results of election
print("Election Results") 
print("---"*7)
print(f"Total Votes: {total_votes}")
print("---"*7)
for i in range(len(vote_count)):
    print(f"{candidates[i]} {round(vote_count[candidates[i]]/total_votes*100,3)}% ({vote_count[candidates[i]]})")
print("---"*7)
print(f"Winner: {election_winner}")
print("---"*7)

with open(os.path.join("Analysis", "Election_Results.txt"), "w") as f:
    print("Election Results", file = f) 
    print("---"*7, file = f)
    print(f"Total Votes: {total_votes}", file = f)
    print("---"*7, file = f)
    for i in range(len(vote_count)):
        print(f"{candidates[i]} {round(vote_count[candidates[i]]/total_votes*100,3)}% ({vote_count[candidates[i]]})", file = f)
    print("---"*7, file = f)
    print(f"Winner: {election_winner}", file = f)
    print("---"*7, file = f)



   
        
    

        
        