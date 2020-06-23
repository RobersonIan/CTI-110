# Calculates your total profit
# 6/23/2020
# CTI-110 P2T1 - Sales Prediction
# Ian Roberson
#


#Declare variables/get total sales
totalSales = float(input('Enter the projected profits: '))
profitPrecent = 0.23

#Calculations
totalProfit = totalSales * profitPrecent

#Display
print('The profit is: $', format(totalProfit, ',.2f'))
