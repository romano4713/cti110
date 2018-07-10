# CTI-110 
# P4LAB - Nested Loop
# Omar Roman
# 6/29/2018
#

import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("SnowFlake")

# assign a name to your turtle
roman = turtle.Turtle()

colors = ("blue", "white", "purple", "red")

# function that draws the snowflake
def snowflake():
    roman.penup()
    roman.forward(90)
    roman.left(45)
    roman.pendown()

    for i in range(8):
        roman.color(random.choice(colors))
        branch()
        roman.left(45)

# create one branch of the snowflake
def branch():
    for i in range(3):
        for i in range(3):
            roman.forward(30)
            roman.backward(30)
            roman.right(45)
        roman.left(90)
        roman.backward(30)
        roman.left(45)
    roman.right(90)
    roman.forward(90)

snowflake()

# leave the window open until you click to close
wn.mainloop()
