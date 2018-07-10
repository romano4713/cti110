# CTI-110 
# P4LAB - Nested Loop
# Omar Roman
# 6/29/2018
#

import turtle
win = turtle.Screen()
win.bgcolor("blue")
win.title("SnowFlake")

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.pensize(5)

def polygon():
        
    for i in range(4):
        t.forward(150)
        t.left(90)
        
polygon()

t.penup()
t.forward(75)
t.right(90)
t.forward(75)
t.pensize(1)
t.pendown()

def snowFlake():
    # Create a loop to draw a snowflake.
    t.pensize(1)
    for i in range(6):
        t.left(90)
        t.forward(50)
        t.forward(-20)
        t.left(20)
        t.forward(15)
        t.forward(-15)
        t.right(40)
        t.forward(15)
        t.forward(-15)
        t.left(20)
        t.forward(-30)
        t.right(30)
            
snowFlake()

# Lifts pen to move to another side of polygon.
t.penup()
t.forward(-300)
t.pendown()

snowFlake()

# Lifts pen to move to another side of polygon.
t.penup()
t.forward(150)
t.right(90)
t.forward(150)
t.pendown()

snowFlake()

# Lifts pen to move to another side of polygon.
t.penup()
t.forward(-300)
t.pendown()

snowFlake()

# Wait for user to close window.
win.mainloop()
