def berechne_fallhöhe(t):
    g = 9.81
    s = 0.5*g*t**2
    return s

while True:
    fallzeit = float(input('fallzeit in sekunden'))
    fallhöhe = berechne_fallhöhe(fallzeit)
    print('fallhöhe:', fallhöhe, 'm')