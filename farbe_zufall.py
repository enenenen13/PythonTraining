from turtle import *
from random import randint, random


def quadrat(a, farbe):
    fillcolor(farbe)
    begin_fill()
    for i in range(4):
        forward(a)
        right(90)
    end_fill()

speed(0)
hideturtle()
up()
for i in range (300):
    x = randint(-200, 200)
    y = randint(-200, 200)
    goto(x, y)
    rot = random()
    gruen = random()
    blau = random()
    groese = randint(10, 50)
    quadrat(groese,(rot, gruen, blau))
input()