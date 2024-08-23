MENÜ = '''
berechnung des volumens
(p)yramiede
(w)ürfel
(e)nde'''

def berechne_würfel():
    a = float(input('seitenlänge: '))
    v = a**3
    print('volumen des würfels: ',
          round(v))

def berechne_pyramide():
    a = float(input('seitenlänge: '))
    h = float(input('höhe: '))
    v = 1/3 * a**2 * h
    print('volumen der pyramide: ',
          round(v))


eingabe = 'x'
while eingabe != 'e':
    print(MENÜ)
    eingabe = input('bitte wähle: ')
    if eingabe == 'p':
        berechne_pyramide()
    if eingabe == 'w':
        berechne_würfel()
print('auf wiedersehen')