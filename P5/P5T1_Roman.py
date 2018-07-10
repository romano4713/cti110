# CTI-110 
# P5T1 - Kilometer Converter
# Omar Roman
# 7/5/2018
#

# conversion_Factor = 0.6214

def main():
    # Get the distance in kilometers.
    km = float (input ("Enter the distance in kilometers: "))

    # Display the distance converted to miles.
    show_miles(km)
    


def show_miles(km):

    # Calculate the miles.
    miles = km * 0.6214

    # Display the miles.
    print (km, 'kilometers equals', miles, 'miles.')
    
main()
