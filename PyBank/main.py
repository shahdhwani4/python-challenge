import os
import csv

# Read and store data from file
def fetchBudgetData(inputFile):
  # store budget data retrieved from csv file
  budgetData = []
  with open(inputFile, mode="r") as datafile:
    # Create a CSV reader object
    csvReader = csv.reader(datafile, delimiter=',')
    
    # Skip the header row
    next(csvReader)
    
    # store each row to an array (budgetData)
    for row in csvReader:
      budgetData.append(row)
    
  return budgetData

# Calculate the total number of months included in the dataset
def calculateTotalNumberOfMonths(budgetData):
  return "Total Months: " + str(len(budgetData))

# Calculate the net total amount of "Profit/Losses" over the entire period
def calculateTotal(budgetData):
  total = 0
  for monthData in budgetData:
    total = total + int(monthData[1])

  return "Total: " + str(total)

# Compute monthly changes in Profit/Losses
def computeMonthlyChanges(budgetData):
  monthlyChanges = []

  for index, monthData in enumerate(budgetData):
    if index > 0:
      currentMonthNet = int(monthData[1])
      previousMonthNet = int(budgetData[index - 1][1])
      monthlyChange = currentMonthNet - previousMonthNet
      monthlyChanges.append([monthData[0], monthlyChange])
   
  return monthlyChanges

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
def calculateAverageChange(monthlyChanges):
  totalChange = 0
  totalNumberOfMonthsForAvg = len(monthlyChanges)

  for monthlyChange in monthlyChanges:
    totalChange += monthlyChange[1]
  
  avg = format(totalChange / totalNumberOfMonthsForAvg, ".2f")  
  return "Average change: " + avg

# The greatest increase in profits (date and amount) over the entire period
def calculateGreatestIncreaseInProfits(monthlyChanges):
  greatestIncrease = monthlyChanges[0]

  for monthlyChange in monthlyChanges:
    currentMonthChange = monthlyChange[1]
    greatestIncreaseChange = greatestIncrease[1]
    # Check if current month change is greatest increase in profit
    if currentMonthChange > greatestIncreaseChange:
      greatestIncrease = monthlyChange
  
  return "Greatest Increase in Profits: " + greatestIncrease[0] + " (" + str(greatestIncrease[1]) + ")"

# The greatest decrease in profits (date and amount) over the entire period
def calculateGreatestDecreaseInProfits(monthlyChanges):
  greatestDecrease = monthlyChanges[0]

  for monthlyChange in monthlyChanges:
    currentMonthChange = monthlyChange[1]
    greatestDecreaseChange = greatestDecrease[1]
    # Check if current month change is greatest decrease in profit
    if currentMonthChange < greatestDecreaseChange:
      greatestDecrease = monthlyChange
  
  return "Greatest Decrease in Profits: " + greatestDecrease[0] + " (" + str(greatestDecrease[1]) + ")"

# Write output to file and terminal
def writeOutputToTerminalAndFile(outputFile, resultsToPrint):
  # Open the text file in write mode
  with open(outputFile, "w") as textFile:
    # Iterate through the array and write each element to the file
    for result in resultsToPrint:
        print(result)
        textFile.write(f"{result}\n")

# main function to run the python script
def main(inputFile, outputFile):
   # store results to be printed/stored
   resultsToPrint = []
   budgetData = fetchBudgetData(inputFile)
   resultsToPrint.append("Financial Analysis")
   resultsToPrint.append("--------------------------------------------------------")
   resultsToPrint.append(calculateTotalNumberOfMonths(budgetData))
   resultsToPrint.append(calculateTotal(budgetData))
   monthlyChanges = computeMonthlyChanges(budgetData)
   resultsToPrint.append(calculateAverageChange(monthlyChanges))
   resultsToPrint.append(calculateGreatestIncreaseInProfits(monthlyChanges))
   resultsToPrint.append(calculateGreatestDecreaseInProfits(monthlyChanges))

   writeOutputToTerminalAndFile(outputFile, resultsToPrint)

# path to the input csv file
inputFile = os.path.join('Resources', 'budget_data.csv')
print(inputFile)
# path to the output text file
outputFile = os.path.join('analysis', 'output.txt')
main(inputFile, outputFile)