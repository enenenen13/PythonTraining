from turtle import *

def quadrat(a, farbe):
    fillcolor(farbe)
    begin_fill()
    for i in range(4):
        forward(a)
        right(90)
    end_fill()

quadrat(40, 'blue')
forward(40)
quadrat(80, 'yellow')
input()