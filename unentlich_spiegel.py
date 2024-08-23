from turtle import *

speed(0)

def spierale(a):
    if a < 5:
        return
    else:
        forward(a)
        right(90)
        spierale(0.9*a)

spierale(200)
hideturtle()
input()