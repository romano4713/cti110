# CTI-110 
# P4T1 - Turtle Graphics
# Omar Roman
# 6/27/2018
#

import turtle             
win = turtle.Screen()   
win.bgcolor("blue")   
win.title("Intials")

t = turtle.Turtle() 
t.shape("turtle")
t.color("black")
t.pensize(5)


def my_Initials():
    t.circle(45)
    t.penup()
    t.forward(65)
    t.pendown()
    t.left(90)
    t.forward(85)
    t.right(90)
    t.circle(-27, 180)
    t.left(130)
    t.forward(40)
    
my_Initials()

# Wait for user to close window.
win.mainloop()
