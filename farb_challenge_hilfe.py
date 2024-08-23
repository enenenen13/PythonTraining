from turtle import *
speed(0)
def stern (l=100):
    right(-78)
    fillcolor('yellow')
    begin_fill()
    for i in range(5):
        forward(l)
        right(150)
        forward(l)
        left(78)
    end_fill()

def sechseck (l=100):
    fillcolor('red')
    begin_fill()
    for i in range(6):
        forward(l)
        right(60)
    end_fill()

def kstern (l=100):
    fillcolor(0, 0.7, 1)
    for i in range(6):
        begin_fill()
        for ii in range(3):
            forward(l)
            left(120)
        end_fill()
        forward(l)
        right(60)

def quadrat(a=100):
    for i in range(4):
        forward(a)
        right(90)

