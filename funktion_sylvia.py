# Einleitung: Spielbrett
spielbrett = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def spielbrett_ausdrucken():
    print(spielbrett[0], " | ", spielbrett[1], " | ", spielbrett[2])
    print ("-------------")
    print(spielbrett[3], " | ", spielbrett[4], " | ", spielbrett[5] )
    print ("-------------")
    print(spielbrett[6], " | ", spielbrett[7], " | ", spielbrett[8] )
"""
while True:
    spielbrett_ausdrucken()
    spielbrett_ausdrucken()
    spielbrett_ausdrucken()
"""


# Euro in Yen konvertieren mit Eingabe
# durch die Konsole
def euro_zu_yen():
    euro = input("Euro: ")
    euro = float(euro)
    yen = euro * 132.59
    print ("Yen: ", yen)

euro_zu_yen()

def yen_zu_Euro():
    yen = input ("Yen: ")
    yen = float(yen)
    euro = yen * 0.0075
    print ("Euro: ", euro)

yen_zu_Euro()

def euro_zu_bitcoin():
    euro = input("Euro: ")
    euro = float(euro)
    bitcoin = euro * 51664.98
    print ("Bitcoin: ", bitcoin)

euro_zu_bitcoin()

def bitcoin_zu_Euro():
    bitcoin = input ("Bitcoin: ")
    bitcoin = float(bitcoin)
    euro = bitcoin * 0.000019
    print ("Euro: ", euro)

bitcoin_zu_Euro()


def cm_zu_km():
    cm = input ("cm: ")
    cm = float(cm)
    km = cm * 100000
    print ("km: ", km)

cm_zu_km()

print()
input("drhiuurbqtzuvwbiutzcib: ")
def meter_zu_mm(meter):
    mm = meter * 1000

    print("mm: ", mm )
meter_zu_mm(6)

print()
input("drhiuurbqtzuvwbiutzcib: ")
def meter_zu_mm(meter):
    mm = meter * 1000

    print("mm: ", mm )
meter_zu_mm(6)
