from turtle import *

pensize(3)
pencolor('brown')

def baum(x):
    if x < 5:
        return
    else:
        forward(x)
        left(30)
        baum(0.5*x)
        right(60)
        baum(0.5*x)
        left(30)
        back(x)

left(90)
speed(0)
baum(100)
hideturtle()
input()