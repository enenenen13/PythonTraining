

print('Sind die Nadeln (e)inzeln',
      'oder in kleinen (b)ündeln? ')
antwort = input('antwort (e/b): ')
if antwort == 'e':
    print('sitzen die Nadeln (d)irekt am zweig oder'
          'sitzen sie auf kleinen verholzten (s)tielen?')
    antwort = input('antwort (d/s):')
    if antwort == 'd':
        baum = 'Tanne'
    else:
        baum = 'Fichte'
else:
    print('sind die nadeln länger als 4 cm?')
    antwort = input('antwort (j/n): ')
    if antwort == 'j':
        baum = 'kiefer'
    else:
        baum = 'lärche'

ergebnis = 'es handelt sich um eine ' + baum +'.'
print(ergebnis)