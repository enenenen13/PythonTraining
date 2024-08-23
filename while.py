from random import randint
eingabe = 'j'

while eingabe == 'j':
    zahl = randint(1, 6)
    print ('würfel: ', zahl)
    eingabe = input('noch einmal? (j/n)')
print('auf wiedersehen')