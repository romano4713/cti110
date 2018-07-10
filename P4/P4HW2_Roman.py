# CTI-110 
# P4HW2 - Running Total
# Omar Roman
# 6/28/2018
#

def runningTotal():

    total = 0

    number = float( input("\nEnter a number? "))
                            

    # Create while loop for positive number, Ends when negative number is enetered    
    while number > -1:
        total = total + number
        number = float( input("\nEnter a number? "))

        
        
    # Display runningTotal.
    print ("\nTotal: ", total)
    
runningTotal()
