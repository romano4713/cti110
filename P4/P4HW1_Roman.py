# CTI-110 
# P4HW1 - Distance Traveled
# Omar Roman
# 6/28/2018
#

def distanceTraveled():

    # Enter the speed of the vehicle.
    speed = int (input ('What is the speed of the vehilce in mph? '))

    print ("")
    
    # Enter the time time traveled.
    time = int (input ('How many hours has it traveled? '))

    # Create the Header
    print (" Hour : Distance Traveled ")
    print ("---------------------------")
    print ("")

    # Calculate the distance.
    for currentHour in range( 1, time + 1 ):
        distance = speed * currentHour
        
        # Display in table.
        print ("", currentHour, " " * 2, ':', "", distance)        
    
distanceTraveled()
