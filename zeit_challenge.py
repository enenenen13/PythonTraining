from time import localtime
zeit = localtime()
stunde = zeit.tm_hour
if 3 <= stunde < 11:
    print('guten morgen')
else:
    print('guten abend')