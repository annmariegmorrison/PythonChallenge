import csv
import os

BudgetData = os.path.join("Resources", "budget_data.csv")

with open(BudgetData) as (BankData):
    Reader = csv.reader(BankData)

    Header = next(Reader)

    # INITIALIZE VARIABLES
    NumberOfMonths = 0
    TotalRevenue = 0
    Revenue = []
    PreviousRevenue = None
    MonthOfChange = []
    RevenueChangeList = []
    GreatestDecrease = 0
    GreatestIncrease = 0
    RevenueChange = 0
    RevenueAverage = 0

    # LOOP THROUGH ALL DATASET
    for row in Reader:

        # COUNT TOTAL MONTHS IN DATA SET
        NumberOfMonths = NumberOfMonths + 1

        # CALCULATE TOTAL REVENUE
        TotalRevenue = TotalRevenue + int(row[1])

        # CALCULATE THE AVERAGE OF CHANGES IN PROFITS/LOSES

        if PreviousRevenue == None:
            PreviousRevenue = int(row[1])

        else:
            RevenueChange = int(row[1]) - PreviousRevenue
            RevenueChangeList.append(RevenueChange)
            PreviousRevenue = int(row[1])

        # GREATEST INCREASE IN PROFIT
        if RevenueChange > GreatestIncrease:
            GreatestIncrease = RevenueChange

         # GREATEST DECREASE IN PROFIT
        if RevenueChange < GreatestDecrease:
            GreatestDecrease = RevenueChange

    # CALCULATE THE AVERAGE CHANGE
    RevenueAverage = sum(RevenueChangeList)/len(RevenueChangeList)

    # PRINT

    print(f"Financial Analysis: \n ---- \n Total Months:{NumberOfMonths}")
    print(f"Total Revenue: Total Revenue: {TotalRevenue}")
    print(f"Average Revenue Change: {RevenueAverage}")
    print(f"Greatest Increase in Profit: {GreatestIncrease}")
    print(f"Greatest Decrease in Profit: {GreatestDecrease}")

 # WRITE
printout = (f"Financial Analysis: \n ---- \n Total Months:{NumberOfMonths}\n"
            f"Total Revenue: Total Revenue: {TotalRevenue}\n"
            f"Average Revenue Change: {RevenueAverage}\n"
            f"Greatest Increase in Profit: {GreatestIncrease}\n"
            f"Greatest Decrease in Profit: {GreatestDecrease}")
print(printout)

with open(final, "w") as txt:
    txt.write(printout)
