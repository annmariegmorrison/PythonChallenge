import csv
import os

PollData = os.path.join("Resources", "election_data.csv")

with open(PollData) as (ElectionData):
    Reader = csv.reader(ElectionData)

    Header = next(Reader)

    # INITIALIZE VARIABLES

    Candidates = []
    NumberOfVotes = []
    PercentOfVotes = []
    TotalVotes = 0
    Votes = 0

    # LOOP THROUGH ALL THE DATASET

    for row in Reader:

        # COUNT TOTAL NUMBER OF VOTES CAST
        TotalVotes = TotalVotes + 1

        # LIST OF CANDIDATES OF CANIDATES WHO RECEIVED VOTES AND NUMBER OF VOTES

        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            NumberOfVotes.append(1)
        else:
            index = Candidates.index(row[2])
            NumberOfVotes[index] = NumberOfVotes[index] + 1

    # PERCENTAGE  OF VOTES

    for votes in NumberOfVotes:
        percentage = (votes/TotalVotes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        PercentOfVotes.append(percentage)

    # WINNER OF ELECTION
    Winner = max(NumberOfVotes)
    index = NumberOfVotes.index(Winner)
    WinningCandidate = Candidates[index]


    # PRINT

    print(f"Election Results: \n ---- \n Total Votes: {TotalVotes}")
    for i in range(len(Candidates)):
        print(
            f"{Candidates[i]}: {str(PercentOfVotes[i])} ({str(NumberOfVotes[i])})")
    print(f"\n -----")
    print(f"Winner: {WinningCandidate}")

# WRITE

printout = f"Election Results: \n ---- \n Total Votes: {TotalVotes}"
for i in range(len(Candidates)):
    printout = printout + f"{Candidates[i]}: + {str(PercentOfVotes[i])} + ({str(NumberOfVotes[i])})"
    printout = printout + f"\n ----- \n"
printout = printout + f"Winner: {WinningCandidate}"
print(printout)


#Exporting a text file
#Specifying the file to write to
final = os.path.join('Analysis','PyPoll.txt')
with open(final, "w") as txt:
    txt.write(printout)
    
 



