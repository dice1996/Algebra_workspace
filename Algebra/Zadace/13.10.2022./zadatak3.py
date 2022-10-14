"""
Zadatak 8:
Unijeti 10 brojeva u listu. Pronadi 2 najveci u listi (hint: negativan index)
"""
lista = []
UNOS = 10

for i in range(UNOS):
    while True:
        try:
            pomocna = int(input(f"Unesi {i + 1} cijeli broj: "))
            lista.append(pomocna)
            break
        except:
            print("Uneseno nije cijeli broj. Pokusaj ponovno!")

lista.sort(reverse=True)
print(f"Prvi najveci uneseni broj je {lista[0]}; Drugi najveci uneseni broj je {lista[1]}")