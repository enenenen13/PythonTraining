import sys

z1 = input("Zahl 1:")
z2 = input ("Zahl 2:")
z1 = int(z1)
z2 = int(z2)
rz = input ("RZ:")
if z2 == 0 and rz == "/":
    print ("geht nicht")
    sys.exit()
if z1 == 9 and z2 == 9 and rz == "*":
    print ("90 richtig")
    sys.exit()

if rz == "-":
    print(z1 - z2)
if rz == "+":
    print(z1 + z2)
if rz == "/":
    print(z1 / z2)
if rz == "*":
    print(z1 * z2)