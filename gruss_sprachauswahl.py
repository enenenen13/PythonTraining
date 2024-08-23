print('''wähle eine sprache aus
(f)ranzösisch
(e)nglisch
(d)eutsch''')
sprache = input('auswahl: ')
if sprache == 'e':
    gruß = 'how do you do?'
elif sprache == 'f':
    gruß = 'bonyour!'
else:
    gruß = 'guten tag!'
print(gruß)