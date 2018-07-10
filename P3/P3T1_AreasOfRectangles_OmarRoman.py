# CTI-110 
# P3T1 - Areas of Rectangles
# Omar Roman
# 6/20/2018
#

# Get the dimensions of rectangle 1.
length1 = int (input ('Enter the length of rectangle 1: '))
width1 = int (input ('Enter the width of rectangle 1: '))

# Get the dimensions of rectangle 2.
length2 = int (input ('Enter the length of rectangle 2: '))
width2 = int (input ('Enter the width of rectangle 2: '))

# Calculate the areas of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Determine which had the greater area.
if area1 > area2:
    print ('The first rectangle has the larger area.')
elif area2 > area1:
    print ('The second rectangle has the larger area.')
else:
    print ('Both rectangles have equal area.')


