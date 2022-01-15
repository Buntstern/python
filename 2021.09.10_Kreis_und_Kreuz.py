from colored import stylize
from colored import fg

print (stylize("Alöle, und viel Spaß on the game!", fg (78)))

pos1 = "1"
pos2 = "2"
pos3 = "3"
pos4 = "4"
pos5 = "5"
pos6 = "6"
pos7 = "7"
pos8 = "8"
pos9 = "9"

runde = 0 
while runde < 10:
    reihe1 = pos1 + " | " + pos2 + " | " + pos3
    reihe2 = pos4 + " | " + pos5 + " | " + pos6
    reihe3 = pos7 + " | " + pos8 + " | " + pos9
    trennreihe = "---------"

    print (reihe1)
    print (trennreihe)
    print (reihe2)
    print (trennreihe)
    print (reihe3)
    
    runde = runde +1

    spieler1 = input (stylize("Runde " + str(runde) + "! In welcher Position möchtest du dein X setzen Spieler1? ", fg (87)))
    if spieler1 == "1":
        pos1 = "X"
    if spieler1 == "2":
        pos2 = "X"
    if spieler1 == "3":
        pos3 = "X"
    if spieler1 == "4":
        pos4 = "X"
    if spieler1 == "5":
        pos5 = "X"
    if spieler1 == "6":
        pos6 = "X"
    if spieler1 == "7":
        pos7 = "X"
    if spieler1 == "8":
        pos8 = "X"
    if spieler1 == "9":
        pos9 = "X"
    
    if pos1 == "X" and pos2 == "X" and pos3 == "X":
        print ("Spieler1, du hast gewonnen!")
        break
    if pos4 == "X" and pos5 == "X" and pos6 == "X":
        print ("Spieler1, du hast gewonnen!")
        break
    if pos7 == "X" and pos8== "X" and pos9 == "X":
        print ("Spieler1, du hast gewonnen!")
        break
    if pos1 == "X" and pos5 == "X" and pos9 == "X":
        print ("Spieler1, du hast gewonnen!")
        break
    if pos3 == "X" and pos5 == "X" and pos7 == "X":
        print ("Spieler1, du hast gewonnen!")
        break
    if pos1 == "X" and pos4 == "X" and pos7 == "X":
        print ("Spieler1, du hast gewonnen!")
        break
    if pos2 == "X" and pos5 == "X" and pos8 == "X":
        print ("Spieler1, du hast gewonnen!")
        break
    if pos3 == "X" and pos6 == "X" and pos9 == "X":
        print ("Spieler1, du hast gewonnen!")
        break

    reihe1 = pos1 + " | " + pos2 + " | " + pos3
    reihe2 = pos4 + " | " + pos5 + " | " + pos6
    reihe3 = pos7 + " | " + pos8 + " | " + pos9
    trennreihe = "---------"

    print (reihe1)
    print (trennreihe)
    print (reihe2)
    print (trennreihe)
    print (reihe3)

    spieler2 = input (stylize("Runde " + str(runde) + "!In welcher Position möchtest du dein O setzen Spieler2? ", fg (87)))
    if spieler2 == "1":
        pos1 = "0"
    if spieler2 == "2":
        pos2 = "0"
    if spieler2 == "3":
        pos3 = "0"
    if spieler2 == "4":
        pos4 = "0"
    if spieler2 == "5":
        pos5 = "0"
    if spieler2 == "6":
        pos6 = "0"
    if spieler2 == "7":
        pos7 = "0"
    if spieler2 == "8":
        pos8 = "0"
    if spieler2 == "9":
        pos9 = "0"


    if pos1 == "0" and pos2 == "0" and pos3 == "0":
        print ("Spieler2, du hast gewonnen!")
        break
    if pos4 == "0" and pos5 == "0" and pos6 == "0":
        print ("Spieler2, du hast gewonnen!")
        break
    if pos7 == "0" and pos8 == "0" and pos9 == "0":
        print ("Spieler2, du hast gewonnen!")
        break
    if pos1 == "0" and pos5 == "0" and pos9 == "0":
        print ("Spieler2, du hast gewonnen!")
        break
    if pos3 == "0" and pos5 == "0" and pos7 == "0":
        print ("Spieler2, du hast gewonnen!")
        break
    if pos1 == "0" and pos4 == "0" and pos7 == "0":
        print ("Spieler2, du hast gewonnen!")
        break
    if pos2 == "0" and pos5 == "0" and pos8 == "0":
        print ("Spieler2, du hast gewonnen!")
        break
    if pos3 == "0" and pos6 == "0" and pos9 == "0":
        print ("Spieler2, du hast gewonnen!")
        break