#Add our dependency
import csv

#Assign a variable to load a file from a path
file_to_load = "/Users/avawolfe/desktop/GW/Election_Analysis/Resources/election_results.csv"

#Assign a variable to save the file to a path
file_to_save = "/Users/avawolfe/desktop/GW/Election_Analysis/analysis/election_analysis.txt"

#1 Initialize a total vote counter
total_votes = 0

#Candidate options and candidate votes
candidate_options=[]
#Declare the empty dictionary
candidate_votes={}

#Winning candidate and Winning Count tracker
winning_candidate = ""
winning_count =0
winning_percentage =0

#Open the election results and read the file
with open(file_to_load) as election_data: 
    file_reader = csv.reader(election_data)

    #Read the header row
    headers= next(file_reader)

    #Print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes +=1

        #Print candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add candidate name to the list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        
        #Add a vote to that candidates's count
        candidate_votes[candidate_name] +=1

#Determine the percentage of votes for each candidate by looping through the counts
#1 Iterate through the candidate list
for candidate_name in candidate_votes:
    #2 retrieve the vote count of a candidate
    votes= candidate_votes[candidate_name]
    #3 calculate the percentage of votes
    vote_percentage= float(votes)/ float(total_votes)*100
    
    #to do: print out each candidate's name, vote count and votes to the terminal
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        # if true then set winning_count = votes and winning_percentage= vote_percentage
        winning_count= votes
        winning_percentage = vote_percentage
        # And, set the winning_candidate equal to the candidate's name
        winning_candidate=candidate_name
winning_candidate_summary = (
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------\n")
print(winning_candidate_summary)