# CTI-110 
# P5T2 - Feet to Inches
# Omar Roman
# 7/5/2018
#

inches_per_foot = 12

def main():
    # Get a number of feet.
    feet = int (input ('Enter a number of feet: '))

    # Convert to inches.
    print (feet, 'feet equals', feet_to_inches(feet), 'inches.')    

def feet_to_inches(feet):
    return feet * inches_per_foot

    
main()
