# CTI-110 
# P2T1 - Sales Prediction 
# Omar Roman
# 6/11/2018
#

# Get the projected total sales.
totalSales = float (input ('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
annualProfit = totalSales * 0.23

# Display the profit.
print ('The annualProfit is $', format (annualProfit, ',.2f'))
