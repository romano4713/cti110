# CTI-110 
# P5HW2 - Random Number Guessing Game
# Omar Roman
# 7/6/2018
#

# use the random module
import random

def main():

    # variable required by assignment
    secret_Number = random.randint(1, 100)

    # use a variable to control the loop
    again = 'y'

    while again == 'y' or again == 'Y':
        choice = int(input("Enter a Secret Number: "))
        if choice < secret_Number:
            print ("Too Low, Try Agsin" )
        elif choice > secret_Number:
            print ("Too High, Try Again" )
        elif choice == secret_Number:
            again = input('\nYou Got It, Play again? (y = yes): ')

main()
