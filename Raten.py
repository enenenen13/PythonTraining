import random
import sys

while True:
    versuche = 0
    computer = random.randrange(1,100)
    spieler = -1
    while spieler != computer:
        spieler = input("Dein Tipp:")
        versuche = versuche + 1
        spieler = int(spieler)
        if spieler < computer:
            print ("zu klein")
        if spieler > computer:
            print ("zu gross")

    print("Erraten!")
    print ("versuche" ,versuche)
    nocheinmal = input ("Noch einmal (J/N)?")
    if nocheinmal == "N" or nocheinmal=="n":
        break



