# CTI-110 
# P3HW1 - Age Classifier
# Omar Roman
# 6/22/2018
#



# Get the age of the person.
userAge = int (input ('Enter the persons age: '))

def main(userAge):

    if userAge <= 1:
        print ('The person is an infant.')
    elif userAge < 13:
        print ('The person is a child.')
    elif userAge < 20:
        print ('The person is a teenager.')
    else:
        print ('The person is an adult.')

main(userAge)




