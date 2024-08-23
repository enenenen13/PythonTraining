from farb_challenge_hilfe import stern
from  turtle import *
from random import randint

bgcolor(0, 0, 0.3)

for x in range(5):
    for y in range(5):
        up()
        goto(x*150-300, y*125-250)
        down()
        stern(randint(8, 30))
        right(6)



input()