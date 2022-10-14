"""
Zadatak 10:
Unos 20 brojeva. Nakon unosa na pocetak liste sortirati neparne od najmanjeg do najveceg i nakon toga parne od najveceg do najmanjeg.
"""

brojevi =[]
par = []
nepar = []
UNOS = 20

for i in range(UNOS):
    while True:
        try:
            pomocna = int(input(f"Unesi {i + 1} cijeli broj: "))
            if pomocna not in par and pomocna not in nepar:
                if pomocna%2 == 0:
                    par.append(pomocna)  
                else:
                    nepar.append(pomocna)
                break
            else:
                print("Uneseni broj se vec nalazi na listi. Pokusaj ponovno!")
        except:
            print("Uneseno nije cijeli broj. Pokusaj ponovno!")

nepar.sort()
par.sort(reverse=True)

brojevi = nepar + par
print(brojevi)