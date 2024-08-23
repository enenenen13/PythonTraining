from turtle import *
from farb_challenge_hilfe import stern
from random import randint

bgcolor(0, 0, 0.3)

for i in range(25):
    up()
    goto(randint(-300, 300), randint(-250, 250))
    down()
    stern(randint(10, 50))


input()