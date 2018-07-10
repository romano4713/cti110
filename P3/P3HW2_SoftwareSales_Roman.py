# CTI-110 
# P3HW2 - SoftwareSales_Roman
# Omar Roman
# 6/22/2018
#


def main():
    
    # How many packages bought.
    quantity = int (input ('Enter the quantity purchased: '))

    packagePrice = 99

    
    # Determine the amount of discount.
    if quantity < 10:
        discount = 0
    elif quantity < 20:
        discount = 0.1
    elif quantity < 50:
        discount = 0.2
    elif quantity < 100:
        discount = 0.3
    else:
        discount = 0.4

    subTotal = quantity * packagePrice

    # Display the amount of discount.
    discountAmount = discount * subTotal
    print ()
    print ("Amount of discount: $" + format (discountAmount, ",.2f"))

    # Display the total purchase cost with discount applied.
    total = subTotal - discountAmount
    print ()
    print ("Total amount after discount: $" + format (total, ",.2f"))

main()
