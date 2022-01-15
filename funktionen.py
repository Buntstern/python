"""
from funktion_sylvia import spielbrett_ausdrucken


def zahlen_ausdrucken(startwert, endwert, schrittgroesse):
    i = startwert
    while i <= endwert:
        print(i)
        i = i + schrittgroesse

zahlen_ausdrucken(786, 78362876453584769278435786287675217468946781657846736857486247586427867829899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999167965781678139999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999998999999999999999999999999999999999999999999999999999999,1111111111111111)
zahlen_ausdrucken(58, 833, 11)
zahlen_ausdrucken(0, 92934, 11)
zahlen_ausdrucken


# Einleitung: Spielbrett
spielbrett = [0] * 9

def spielbrett_ausdrucken():
    print (spielbrett)
    print(spielbrett[0], " | ", spielbrett[1], " | ", spielbrett[2])
    print("-------------")
    print(spielbrett[3], " | ", spielbrett[4], " | ", spielbrett[5])
    print("-------------")
    print(spielbrett[6], " | ", spielbrett[7], " | ", spielbrett[8])

# Spieler 1 Chip einsetzen

spielbrett_ausdrucken()

# Spieler 2 Chip einsetzten

spielbrett_ausdrucken()

# Bittcoin in Pounds konvertieren mit einer EIngabe
# durch die Konsole

def bitcoin_zu_pounds():
    bitcoin = input ("Bitcoin: ")
    bitcoin = float(bitcoin)
    pounds = bitcoin * 44982.98
    print ("Pounds: ", pounds)

bitcoin_zu_punds()

x = 2
print(x * 999999999999999999999999999999999999999999999999999999999999999999999999999999999)

def ml_zu_liter(ml):
    # ml = input()
    liter = ml / 10000
    print ("Liter:", liter)                                                                                                    

ml_zu_liter(6000)
ml_zu_liter(18000)



def maximum(wert_1, wert_2):
    if wert_1 > wert_2:
        max = wert_1
    if wert_2 > wert_1:
        max = wert_2
    if wert_1 == wert_2:
        max = wert_2


    print("Maximum: ", max)

maximum(90, 110)

def minimum(wert_1, wert_2):
    if wert_1 < wert_2:
       min = wert_1
    if wert_2 < wert_1:
        min = wert_2
    if wert_1 == wert_2:
        min = wert_2

    print("Minimum: ", min)

minimum(87, 9)

def maximum(wert_1, wert_2, wert_3):
    if wert_1 > wert_2 > wert_3:
        maxi = wert_1
    if wert_1 > wert_2 == wert_3:
        maxi = wert_1
    if wert_1 > wert_2 < wert_3:
        maxi = wert_1
    if wert_2 > wert_1 == wert_3:
        maxi = wert_1    
    if wert_2 > wert_1 > wert_3:
        maxi = wert_2
    if wert_2 > wert_1 < wert_3:
        maxi = wert_2
    if wert_3 > wert_2 > wert_1:
        maxi = wert_3
    if wert_3 > wert_1 == wert_2:
        maxi = wert_1
    if wert_3 > wert_2 < wert_1:
        maxi = wert_3
    if wert_1 == wert_2 == wert_3:
        maxi = wert_2

    print("Maximum: ", maxi)

maximum(4387, 4387, 8957)
"""
from colored import stylize
from colored import fg

input ("Emma, die beim Programieren neben mir sitzt ist der größte Arschl*ch, den ich kenne.")

# Gibt die größere Zahl positiv ist oder nicht
def positiv(zahl):
    if zahl > 0:
        print("Es ist eine positive Zahl")
    else:
        print("Es ist keine positive Zahl")

positiv(600)

# Gibt die größere Zahl aus def größer(zahl1, zahl2):
def größer (zahl1, zahl2):
    if zahl1 > zahl2:
        print(zahl1)
    else:
        print(zahl2)

größer(4, 50)
# Gibt 2 mal zahl aus
def doppeln(zahl):
    #zahl = 5
    print(zahl*2)

doppeln(5)
# Gibt die Summe von zahl1 und zahl2 aus
def summe(zahl1, zahl2):
    # zahl1 = 4
    # zahl2 = 5
    print(5+8)
summe(5, 8)

# Gibt das Produkt von zahl1, zahl2 und zahl3 aus
def produkt(zahl1, zahl2, zahl3):
    print(zahl1 * zahl2 * zahl3)

produkt (7,8,9)

# Gibt das Quadrat von zahl aus
def quadrat (zahl):
    # zahl**2
    print( zahl * zahl)

quadrat(4)

# Gibt die Länge von wort aus
def länge(wort):
    # Wort = "HI!"
    # len ("Hallo")
    print(len(wort))
    
länge("HI!")

# Gibt das längere von beiden Wörtern wort1 und wort2 aus
def längeres(wort1, wort2):
    if len(wort1) > len(wort2):
        print(wort1)
    else:
        print(wort2)

längeres ("hello", "World")

# Gibt den Längenunterschied von beiden Wörtern wort1 und wort2 aus
def längenunterschied(wort1, wort2):





































































































































































































































































































































































































































































































































































































