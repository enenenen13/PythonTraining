from farb_challenge_hilfe import *
from turtle import *



def quadratspirale(a):
    if a < 10:
        return
    else:
        quadrat(a)
        right(10)
        pencolor(1-a/200,a/200,0)
        quadratspirale(0.961*a)

quadratspirale(150)

input()