import os
import csv

# Read and store data from file
def fetchBudgetData(inputFile):
  # store budget data retrieved from csv file
  electionData = []
  with open(inputFile, mode="r") as datafile:
    # Create a CSV reader object
    csvReader = csv.reader(datafile, delimiter=',')
    
    # Skip the header row
    next(csvReader)
    
    # store each row to an array (budgetData)
    for row in csvReader:
      electionData.append(row)
    
  return electionData

# Write output to file and terminal
def writeOutputToTerminalAndFile(outputFile, resultsToPrint):
  # Open the text file in write mode
  with open(outputFile, "w") as textFile:
    # Iterate through the array and write each element to the file
    for result in resultsToPrint:
        print(result)
        textFile.write(f"{result}\n")

# generate dict of election result {candidate: votes}
def getElectionDataResult(electionData):
  electionDataDict = {}

  for vote in electionData:
    candidateName = vote[2]
    if candidateName in electionDataDict:
      # Candidate found in dict so just add vote
      electionDataDict[candidateName] += 1
    else:
      # Candidate not found in dict so create first vote for candidate
      electionDataDict[candidateName] = 1
  
  return electionDataDict

def main(inputFile, outputFile):
  # store results to be printed/stored
  resultsToPrint = []
  electionData = fetchBudgetData(inputFile)
  resultsToPrint.append("Election Results")
  resultsToPrint.append("-------------------------")
  # The total number of votes cast
  totalVotes = len(electionData)
  resultsToPrint.append("Total Votes: " + str(totalVotes))

  resultsToPrint.append("-------------------------")

  electionDataResult = getElectionDataResult(electionData)
  highestVotes = 0
  winner = ""

  # Generate election result per candidate
  for candidate in electionDataResult:
    # total vote secured by candidate
    votes = electionDataResult[candidate]
    # percentage of votes received by candidate
    percentageOfVotes = (votes / totalVotes) * 100
    # format result to 3 decimal places
    formatedPercentageOfVotes = format(percentageOfVotes, ".3f")
    resultsToPrint.append(candidate + ": " + formatedPercentageOfVotes + "% (" + str(votes) + ")")
    if votes > highestVotes:
      highestVotes = votes
      winner = candidate

  resultsToPrint.append("-------------------------")
  resultsToPrint.append("Winner: " + winner)
  resultsToPrint.append("-------------------------")

  writeOutputToTerminalAndFile(outputFile, resultsToPrint)

# path to the input csv file
inputFile = os.path.join('Resources', 'election_data.csv')
# path to the output text file
outputFile = "./analysis/output.txt"
outputFile = os.path.join('analysis', 'output.txt')
main(inputFile, outputFile)