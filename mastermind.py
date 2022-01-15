
import random

while True:
    zufallszahl = random.randint(1000, 9999)
    liste_der_passwort_ziffern = [int(i) for i in str(zufallszahl)]
    leange_liste_der_ziffern =len(liste_der_ziffern)

    leange_set_der_ziffern = len(set(liste_der_ziffern))

    if leange_liste_der_ziffern == leange_set_der_ziffern:
        print("keine duplizierte Elemente")
        # Hiermit wird die Schleife beendet
        break
    else:
        print("duplizierte Element(e)")

zettel = input()
print("Du bist auf dem Richtigen Weg!!!🤩👍")
print("NIMM MAL AB, JUNGE!!!!😵👎")








































