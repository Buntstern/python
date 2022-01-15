import random
print("Wilkommen zum Zahlenraten, suche die geheime Zahl. Es gibt Zahlen von 1 bis 10000. Schafst du es 100 Zahlen zu erraten?")

geheimzahl = random. randint (1,100)
gefunden = False

runde = 0

while gefunden == False:
    runde = runde + 1


    eingabe = input ("Runde " + str (runde) + ": Was ist deiner meinung die geheime Zahl? ")

    if geheimzahl == int (eingabe) :
        print ("Du hast es geschaft! Herzlichen Glückwunsch! :) ")
        gefunden = True
    if geheimzahl != int (eingabe) :
       print ("Du hast es leider nicht gefunden! :( ")
       
    if geheimzahl < int (eingabe):
        print ("Die Zahl muss kleiner werden!!! ")
    if geheimzahl > int (eingabe):
        print ("Die Zahl muss größer werden !!!! ")

print ("Das Spiel ist nun Vorbei")