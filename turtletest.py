"""
programs from "Teach Your Kids to Code" by Bryson Payne
"""

import turtle

# create turtle. mine is named timmy
timmy = turtle.Pen()

def square_spiral():
    for num in range(100):
        timmy.forward(num)
        timmy.left(90)

def tilted_square_spiral():
    for num in range(100):
        timmy.forward(num)
        timmy.left(91) # how does changing the angle change the spiral?

def circle_spiral():
    for num in range(100):
        timmy.circle(num)
        timmy.left(91)

def color_square_spiral():
    # add colors!
    # this one is more complicated; involves modulo + array
    colors = ["red", "yellow", "blue", "green"]
    for num in range(100):
        timmy.pencolor(colors[num % 4])
        timmy.forward(num)
        timmy.left(91)

# running the program right now won't draw anything
# you have to call the functions to draw something!
turtle.done() # wait for the user to close the window
