# CTI-110 
# P2HW2 - Tip Tax Total 
# Omar Roman
# 6/11/2018
#

# How much did the food cost.
foodCost = float (input ('Enter the charge for the food: '))

# Calculate the sales tax.
salesTax = foodCost * 0.07
print ('The salesTax is $', format (salesTax, ',.2f'))

# Calculate the subtotal.
subTotal = foodCost + salesTax

# Calculate the tip amount.
tipAmount = subTotal * 0.18
print ('The tipAmount is $', format (tipAmount, ',.2f'))

# Calculate the total cost.
totalCost = foodCost + salesTax + tipAmount
print ('The totalCost is $', format (totalCost, ',.2f'))


