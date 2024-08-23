Spieler1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

def zeichneSpielfeld(sf):
    buchstaben = "  "
    for i in range(0,8):
        buchstaben = buchstaben + chr(65+i)
    print(buchstaben)

    z = 1
    for line in sf:
        anzeige = str(z)+" "
        for position in line:
            if position == 0:
                anzeige = anzeige + "."
            else:
                anzeige = anzeige + "X"
        print(anzeige)
        z=z+1


def get_zeile_spalte(pos):
    zeile = pos[0]
    spalte = pos[1].upper()
    return zeile, spalte

def ist_gueltige_eingabe(pos):
    if pos is None:
        return False
    pos = pos.strip()

    if len(pos) != 2:
        return False

    zeile,spalte = get_zeile_spalte(pos)
    if zeile < "1" or zeile >"8":
        return False
    if spalte < "A" or spalte > "H":
        return False

    return True

def get_zelle(sf, zeile, spalte):
    zeile = int(zeile) - 1
    spalte = ord(spalte)-65
    return sf[zeile][spalte]

def set_zelle(sf, zeile, spalte, wert):
    zeile = int(zeile) - 1
    spalte = ord(spalte)-65
    sf[zeile][spalte] = wert

def ist_platz_frei(sf, pos):
    if not ist_gueltige_eingabe(pos):
        return False
    zeile, spalte = get_zeile_spalte(pos)

    if  get_zelle(sf, zeile, spalte)== 0:
        return True
    else:
        return False






rest_schiffe = 8

while rest_schiffe > 0:
    zeichneSpielfeld(Spieler1)
    print("Restliche Schiffe:", rest_schiffe)
    pos = input("Koordinaten neues Schiff:")
    if ist_platz_frei(Spieler1, pos):
        rest_schiffe = rest_schiffe - 1
        zeile, spalte = get_zeile_spalte(pos)
        set_zelle(Spieler1, zeile, spalte, 1)

