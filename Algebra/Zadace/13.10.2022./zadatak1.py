"""
Zadatak 1:

Traziti od korisnika unos 10 brojeva (brojevi se ne smiju ponavljati). i spremit brojeve u listu. Po zavrsetku unosa, u drugu listu spremiti kvadrate inicijalno unesenih brojeva, sortirane)
"""

brojevi = []
brojeviKvadrat = []
UNOS = 10

for i in range(UNOS):
    while True:
        try:
            pomocna = int(input(f"Unesi {i + 1}. cijeli broj: "))
            if pomocna not in brojevi:
                brojevi.append(pomocna)
                break
            else:
                print("Uneseni broj se vec nalazi na listi. Pokusaj ponovno!")
        except:
            print("Uneseno nije cijeli broj. Pokusaj ponovno!")

for broj in brojevi:
    brojeviKvadrat.append(broj * broj)

brojeviKvadrat.sort()
print(f"Sortirana lista kvadrata unesenih brojeva je {brojeviKvadrat}")