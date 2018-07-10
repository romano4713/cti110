# CTI-110 
# P4T2 - Bug Collector
# Omar Roman
# 6/28/2018
#

def bugCollector():

    total = 0
    
    # Get the bugs collected for each day.
    for day in range(1, 8):
        print("Enter the bugs collected on day", day)
        bugs = int(input())
        total += bugs
    # Display the total bugs.
    print ('You collected a total of', total, 'bugs')        
    
bugCollector()
