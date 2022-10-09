"""
Zadaci za vjezbu:

u zadatku 1:
uz 2 broja (ograditi s try-except)
dodati 3 varijablu gdje od korisnika trazimo matematicku operaciju (+, -, * ili /)
ako je korisnik za operaciju odabrao nesto 5 (krivi unos) javiti mu porukom o tome (npr. niste unijeli dobru operaciju)
ako je matematicka operacija valjana, iskoristiti tu operaciju nad 2 broja 
---------------------------------------------------------------------
molim samo da kolege koji riješe, da ne podjele odma rjesenje nego da eventualno pomogu kolegama s razmisljanjem
mozete i meni poslati rjesenje ako ste na tragu, pa prokomentiramo privatno
oba zadatka mozete rijesiti sa stvarima koje smo ucili
"""
#ZADATAK 1 - KALKULATOR
print(
""" 
  _  __     _ _          _       _                     _   ___  
 | |/ /__ _| | | ___   _| | __ _| |_ ___  _ __  __   _/ | / _ \ 
 | ' // _` | | |/ / | | | |/ _` | __/ _ \| '__| \ \ / / || | | |
 | . \ (_| | |   <| |_| | | (_| | || (_) | |     \ V /| || |_| |
 |_|\_\__,_|_|_|\__\__,_|_|\__,_|\__\___/|_|      \_/ |_(_)___/ 
                                                                 
""")

znakovi=["+","-","*","/"]
flag = 1
operacija = None
prviBroj = None
drugiBroj = None
rezultat = None

while flag:
    operacija = input("Unesi jedan od znakova za racunsku operaciju:\n'+', '-', '*', '/'\nUnos: ")
    if operacija not in znakovi:
        print("\nNije ispravna racunska operacija unesena.\nPokusaj ponovno!\n\n")
    else:
        flag = 0

#Unos prvog broja
flag = 1

while flag:
    try:
        prviBroj = float(input("Unesi prvi broj: "))
        flag = 0
    except:
        print("Unos broja nije bio uspjesan. Pokusaj ponovno!\n\n")

#Unos drugog broja
flag = 1

while flag:
    try:
        drugiBroj = float(input("Unesi drugi broj: "))
        flag = 0
    except:
        print("Unos broja nije bio uspjesan. Pokusaj ponovno!\n\n")

if operacija is "+":
    rezultat = prviBroj + drugiBroj
elif operacija is "-":
    rezultat = prviBroj - drugiBroj
elif operacija is "*":
    rezultat = prviBroj * drugiBroj
elif operacija is "/":
    rezultat = round(prviBroj / drugiBroj, 2)

print(f"Rezultat računske operacije {operacija} je {rezultat}") 