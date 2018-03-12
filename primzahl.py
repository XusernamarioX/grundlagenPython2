# primzahlen
# Funktion: check if given numbers is prime

def isPrime(n):
    # Logik einbauen
    if(n <= 1):
        return False

    for p in range(2,n):
        if(n % p == 0):
            return False


    return True

print("Primzahlen-Checker")
z = input("Bitte die Zahl eingeben:")
z = int(z)

if(isPrime(z)):
    print(z," ist eine Primzahl")
else:
    print(z," ist keine Primzahl")
