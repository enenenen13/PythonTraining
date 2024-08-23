def anrede ():
    global brief
    print('screibe eine anrede (z.b liebe nadja) ')
    anrede = input('anrede: ')
    brief += anrede + '!\n'

def ortsangabe():
    global brief
    print('wo machst du urlaub')
    ort = input('ort: ')
    brief += 'ich bin gerade in ' + ort + '.'

def wetter():
    global brief
    print('wie ist das wetter')
    print('(s)onnig')
    print('(r)egnerrisch')
    print('(k)ühl')
    auswahl = input('auswahl')
    if auswahl in 'sS':
        brief += 'den ganzen Tag scheint die sonne.\n'
    elif auswahl in 'rR':
        brief += 'leider regnet es den ganzen tag.'
    elif auswahl in 'kK':
        brief += 'es ist zimlich kühl hier.'

def schluss():
    global brief
    name = input('dein name: ')
    brief += 'viele grüße \n' + name

brief = ''
anrede()
ortsangabe()
wetter()
schluss()
print('hier ist der Brief:\n')
print(brief)