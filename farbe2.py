from turtle import *

def quadrat(a, farbe):
    fillcolor(farbe)
    begin_fill()
    for i in range(4):
        forward(a)
        right(90)
    end_fill()

speed(0)
bgcolor(0.6, 0.6, 0.6)
for i in [100, 80, 60, 40, 20]:
    quadrat(i, (i/100, 1-i/100, i/100))
hideturtle()
input()