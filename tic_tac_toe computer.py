import random

spielbrett = [0] * 9


print(spielbrett)


def spielbrett_ausdrucken():
    print(spielbrett[0], " | ", spielbrett[1], " | ", spielbrett[2])
    print("-------------")
    print(spielbrett[3], " | ", spielbrett[4], " | ", spielbrett[5])
    print("-------------")
    print(spielbrett[6], " | ", spielbrett[7], " | ", spielbrett[8])

#spielbrett[4] = 1

#spielbrett[7] = 2

spieler = 1

for i in range(9):
    gueltige_eingabe = False
    while gueltige_eingabe == False:
        if spieler == 1:
            feld = input("In welches Feld möchten Sie denn ein Chip einsetzen?: ")
            feld = int(feld)
            feld = feld - 1
            # Ist das Feld leer?
            if spielbrett[feld] == 0:
                spielbrett[feld] = spieler
                gueltige_eingabe = True
        # Computer
        else:
            zufallszahl = random.randite(0, 8)
            spielbrett[zufallszahl] = 2

     # 1. Zeile
    if spielbrett[0] == spielbrett[1] and spielbrett[1] == spielbrett[2] and spielbrett[0] != 0:
        print("Spieler ", spielbrett[1],": Gewonnen!")
        quit()
    # 2. Zeile
    if spielbrett[3] == spielbrett[4] and spielbrett[4] == spielbrett[5] and spielbrett[3] != 0:
        print("Spieler ", spielbrett[3],": Gewonnen!")
        quit()
    # 3. Zeile
    if spielbrett[0] == spielbrett[1] and spielbrett[1] == spielbrett[2] and spielbrett[0] != 0:
        print("Spieler ", spielbrett[1],": Gewonnen!")
        quit()
    # 1. Spalte
    if spielbrett[0] == spielbrett[3] and spielbrett[3] == spielbrett[6] and spielbrett[0] != 0:
        print("Spieler ", spielbrett[0],": Gewonnen!")
        quit()
    # 2. Spalte
    if spielbrett[0] == spielbrett[3] and spielbrett[3] == spielbrett[6] and spielbrett[0] != 0:
        print("Spieler ", spielbrett[0],": Gewonnen!")
        quit()
    # 3. Spalte
    if spielbrett[0] == spielbrett[3] and spielbrett[3] == spielbrett[6] and spielbrett[0] != 0:
        print("Spieler ", spielbrett[0],": Gewonnen!")
        quit()
    # 1. Diagonale
    if spielbrett[0] == spielbrett[4] and spielbrett[4] == spielbrett[8] and spielbrett[8] != 0:
        print("Spieler ", spielbrett[0], ": Gewonnen")
        quit()
    # 2. Diagonale
    if spielbrett[2] == spielbrett[4] and spielbrett[4] == spielbrett[6] and spielbrett[6] != 0:
        print("Spieler ", spielbrett[2], ": Gewonnen")
        quit()
    spielbrett_ausdrucken()

    if spieler == 1:
        spieler = 2
    else:
        spieler = 1
    

