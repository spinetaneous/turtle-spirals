"""
programs from "Teach Your Kids to Code" by Bryson Payne
"""

import turtle

# create turtle. mine is named timmy
timmy = turtle.Pen()
timmy.shape("turtle")

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

def flower():
    # 18 curves for the petals
    for _ in range(18):
        # draw half of petal curve
        for _ in range(40):
            timmy.pencolor("red")
            timmy.forward(1)
            timmy.left(1)
        # draw yellow center
        for _ in range(20):
            timmy.color("yellow")
            timmy.forward(1)
            timmy.left(1)
        # draw other half of petal curve
        for _ in range(40):
            timmy.pencolor("red")
            timmy.forward(1)
            timmy.left(1)
        # turn to draw new petal curve
        timmy.left(120)

# running the program right now won't draw anything
# you have to call the functions to draw something!
# example:
# flower()

turtle.done() # wait for the user to close the window
