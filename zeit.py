from time import localtime,sleep
while True:
    sleep(1)
    zeit = localtime()

    stunde = zeit.tm_hour
    minute = zeit.tm_min
    sekunde = zeit.tm_sec
    jahr = zeit.tm_year
    monat = zeit.tm_mon
    wtag = zeit.tm_wday
    if wtag == 0:
        tag = 'Montag'
    elif wtag == 1:
        tag = 'Dienstag'
    elif wtag == 2:
        tag = 'Mittwoch'
    elif wtag == 3:
        tag = 'Donnerstag'
    elif wtag == 4:
        tag = 'Freitag'
    elif wtag == 5:
        tag = 'Samstag'
    elif wtag == 6:
        tag = 'Sonntag'

    print('jahr', jahr, 'monat', monat, 'tag: ', tag , 'uhrzeit: ', stunde, 'uhr', minute, 'sekunde', sekunde )