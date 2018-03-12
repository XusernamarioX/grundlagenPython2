# Variable

aktion = input("Welche Aktion willst du? (+/-/*/:)")
print("Aktion ", aktion, " wird ausgeführt...")

if(aktion == "*"):
    print("Multiplikation wird ausgeführt...")
    zahl = input("Welche Zahl wählst du?")
    zahl = int(zahl)
    zahl2 = input("Welche Zahl wählst du?")
    zahl2 = int(zahl2)
    summe = zahl * zahl2
    print("Ergebnis von ", zahl," * ", zahl2, " = ", summe)

if(aktion == "+"):
    print("Addition wird ausgeführt...")
    zahl = input("Welche Zahl wählst du?")
    zahl = int(zahl)
    zahl2 = input("Welche Zahl wählst du?")
    zahl2 = int(zahl2)
    summe = zahl + zahl2
    print("Ergebnis von ", zahl, " + ", zahl2, " = ", summe)

if(aktion == "-"):
    print("Minus wird ausgeführt...")
    zahl = input("Welche Zahl wählst du?")
    zahl = int(zahl)
    zahl2 = input("Welche Zahl wählst du?")
    zahl2 = int(zahl2)
    summe = zahl - zahl2
    print("Ergebnis von ", zahl, " - ",zahl2 ," = ", summe)

if(aktion == ":"):
    print("Division wird ausgeführt...")
    zahl = input("Welche Zahl wählst du?")
    zahl = int(zahl)
    zahl2 = input("Welche Zahl wählst du?")
    zahl2 = int(zahl2)
    summe = zahl/zahl2
    print("Ergebnis von ", zahl," / ", zahl2, " = ", summe)
