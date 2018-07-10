# CTI-110 
# P4HW3 - Factorial
# Omar Roman
# 6/28/2018
#

def Factorial():

    number = int (input ('Enter a nonnegative integer? '))

    while number < 1:
        number = int (input ('Enter a nonnegative integer? '))
        
    factorial = 1

    # Calculate the Factorial.
    for n in range (1, number + 1):
        factorial = factorial * n
        
    # Display Factorial.
    print("\nThe factorial of", number, "is", factorial )
    
Factorial()
