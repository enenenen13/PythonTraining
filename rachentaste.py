from random import randint
a = randint(1, 20)
b = randint(1, 20)

while True:

    print('wie viel ist', a, 'plus', b, '?')
    ergebnis = int(input('ergebnis: '))


    if ergebnis == a + b:
        print('korrekt!')
        break
    else:
        print('falsch')

