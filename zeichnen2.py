from turtle import *

def quadrat(a):
    for i in range(4):
        forward(a)
        right(90)

quadrat(80)
quadrat(40)
quadrat(20)
input()