# CTI-110 
# P4T1 - Turtle Graphics
# Omar Roman
# 6/27/2018
#

import turtle
win = turtle.Screen()
win.bgcolor("blue")
win.title("Triangle & Square")


t = turtle.Turtle()
t.color("black")
t.pensize(5)



def Triangle_Square():
    # Draws the triangle.
    for triangle in [0,1,2]:
        t.forward(150)
        t.left(120)

    # Turns turtle 90 degrees so they dont overlap.
    t.right(90)

    # Draws the square.
    for square in range(4):
        t.forward(150)
        t.left(90)
        
Triangle_Square()

# Wait for user to close window
win.mainloop()
