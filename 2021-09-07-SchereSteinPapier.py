import random 
from colored import stylize
from colored import fg

# Begrüßung
print (stylize("Alola! Und herzlich willkommen zu dieser Schere Stein Paüier Runde!!! Du wirst warscheinlich eh verlieren ;) Du brauchst seeeeeeeeeeeeeeher viel Glück, um eine Chance zu haben! Viel Kleeblatt Glück! ;) ", fg 
(48)))

# Nach dem Namen fragen
name = input ("Wie willst du dich nennen,?! ")
print ("Herzlich wilkommen " + str(name) + "! Schön. das du dabei bist!")

nochmal = "Ja"

while nochmal == "Ja":

    # der computer wählt zufllig Schere oder Stein oder Papier
    computerwahl = random.choice(["Schere", "Stein", "Papier"])

    # der spieler wählt
    spielerwahl = input (stylize("Was ist deine Wahl??? ", fg (46)))

    #äauswertung
    if computerwahl == "Schere" and spielerwahl == "Schere":
        print (stylize("Computer wählt Schere: Unentschieden!",fg (46)))
        continue
    if computerwahl == "Schere" and spielerwahl == "Stein":
        print (stylize("Computer wählt Schere: " + str(name) + " gewinnt!", fg (46)))
    if computerwahl == "Schere"and spielerwahl == "Papier":
        print (stylize("Computer wählt Schrere: juckt mich nicht, das " + str(name) + " verloren hat!", fg (46)))
    if computerwahl == "Stein"and spielerwahl == "Schere":
        print (stylize("Computer wählt Stein: Gib dir mehr mühe, der Computer hat gewonnen!", fg (46)))
    if computerwahl == "Stein"and spielerwahl == "Stein":
        print (stylize("Computer wählt Stein: Es ist unendschieden!", fg (46)))
        continue
    if computerwahl == "Stein"and spielerwahl == "Papier":
        print (stylize("Computer wählt Stein: Du bist gewinner!", fg (46)))
    if computerwahl == "Papier"and spielerwahl == "Schere":
        print (stylize("Computer wählt Papier: " + str(name) + " hat gewonnen.", fg (46)))
    if computerwahl == "Papier"and spielerwahl == "Stein":
        print (stylize("Computer wählt Papier: Warum gewinnt der Computer gegen dich?", fg (46)))
    if computerwahl == "Papier"and spielerwahl == "Papier":
        print (stylize("Computer wählt Papier: Es ist unendschieden! Gib dir mehr mühe!", fg (46)))
        continue

    nochmal = input (stylize("Haste lust noch mal zu spielen? ", fg (100)))

print (stylize("Auf wiedersehen " + str(name) + "! Schön das du dabei warst Klugscheißer!", fg (50)))

