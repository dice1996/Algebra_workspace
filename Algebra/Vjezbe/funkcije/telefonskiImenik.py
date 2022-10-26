"""
Napraviti zadatak telefonski imenik. 
Telefonski imenik (id, ime, prezime, brojTelefona, vrijemeKreiranjaZapisa)

*id treba biti uniqe (ne smije se ponoviti)

Napraviti izbornik:

1 - Unos kontakta
2 - Ispis svih kontakata
3 - brisanje kontakta
4 - Izmjena kontakta
5 - Ispis kontakta po ID-u
0 - Izlaz iz programa

Aplikacija se vrti dok korisnik ne pritisne 0
Ako se odabere bilo što osim navedenih funkcija, vratiti poruku da opcija ne postoji
"""
from os import system
from pomocne_funkcije import *
import time
from datetime import datetime as dt
from prettytable import PrettyTable

glavniIzbornik = {
    1: "Unos kontakta",
    2: "Ispis svih kontakata",
    3: "Brisanje kontakta",
    4: "Izmjena kontakta",
    5: "Ispis kontakata po ID-u",
    0: "Izlaz iz imenika"
}

imenik = [] #lista kontakata dict kontakt

def ispisIzbornika(izbornik):
    for item in izbornik:
        print(f"{item}. {izbornik[item]}")

def unosOpcije(izbornik):
    while True:
        print("GLAVNI IZBORNIK\n")
        ispisIzbornika(izbornik)
        izbor = unesiCijeliBroj("\nUnesi opciju iz gornjeg izbornika: ")
        if izbor not in izbornik.keys():
            print("Unije validan unos! Pokusaj ponovno!")
            time.sleep(2)
            system("clear")
        else:
            if izbor == 0:
                system("clear")
                print("Kraj programa!")
                return 0
            else:
                return izbor
                
def unosKontakta(imenikKontakta: list):
    system("clear")
    kontakt = dict()

    if imenikKontakta == []:
        kontakt["id"] = 1
    else:
        kontakt["id"] = imenikKontakta[-1]["id"] + 1

    kontakt["ime"] = input("Unesi ime kontakta: ")
    kontakt["prezime"] = input("Unesi prezime kontakta: ")
    kontakt["brojTelefona"] = input("Unesi telefonski broj kontakta: ")
    kontakt["vrijemeKreiranjaZapisa"] = int(dt.now().timestamp())
    imenikKontakta.append(kontakt)    

def ispisImenika(imenik: list, index = None):
    system("clear")
    t = PrettyTable(["ID", "IME", "PREZIME", "KONTAKT BROJ", "DATUM I VRIJEME"], padding_width = 4)
    if index == None:
        print(f"Imenik sadrži {len(imenik)} kontakta:")
        for kontakt in imenik:
            t.add_row([kontakt["id"], kontakt["ime"], kontakt["prezime"], kontakt["brojTelefona"], dt.fromtimestamp(kontakt["vrijemeKreiranjaZapisa"])])
    else:
        uniqeKontakt = imenik[index-1]
        t.add_row([uniqeKontakt["id"], uniqeKontakt["ime"], uniqeKontakt["prezime"], uniqeKontakt["brojTelefona"], dt.fromtimestamp(uniqeKontakt["vrijemeKreiranjaZapisa"])])   
    print(f"{t}\n")

def ispisPoIndexu(imenik: list):
    try:
        izbor = unesiCijeliBroj("Unesi ID kontakta: ")
        spisImenika(imenik, izbor)
        
    except:
        print("Pogrešan ID kontakta, povratak u glavni izbornik!")
        time.sleep(2)
        system("clear")

def brisanjeKontakta(imenik: list):
    ispisImenika(imenik)
    try:
        izbor = unesiCijeliBroj("Unesi ID kontakta kojeg zelite obrisati: ")
        imenik.pop(izbor-1)
        imenik = promjenaIndexa(imenik)
        system("clear")
        ispisImenika(imenik)
    except:
        print("Pogrešan ID kontakta, povratak u glavni izbornik....")
        time.sleep(2)
        system("clear")

def promjenaIndexa(imenik: list):
    count = 0
    for item in imenik:
        item["id"] = count + 1
        count += 1
    return imenik

def izmjenaKontakta(imenik: list):
    system("clear")
    ispisImenika(imenik)
    if imenik != []:
        try:
            izbor = unesiCijeliBroj("Unesi ID kontakta: ")
            uniqeKontakt = imenik[izbor-1]
            uniqeKontakt["ime"] = input("Unesi ime kontakta: ")
            uniqeKontakt["prezime"] = input("Unesi prezime kontakta: ")
            uniqeKontakt["brojTelefona"] = input("Unesi telefonski broj kontakta: ")
            uniqeKontakt["vrijemeKreiranjaZapisa"] = int(dt.now().timestamp())
            print("Promjena napravljena! Povratak u glavni izbornik....")
            time.sleep(2)
            system("clear") 
        except:
                print("Pogrešan ID kontakta, pokusaj ponovno!")
    else:
        print("Imenik prazan. Povratak u glavni izbornik...")
        time.sleep(2)
        system("clear")

if __name__ == "__main__":
    flag = True
    system("clear")
    while flag:
        opcija = unosOpcije(glavniIzbornik)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            unosKontakta(imenik)            
            system("clear")
        elif opcija == 2:
            ispisImenika(imenik)
        elif opcija == 3:
            brisanjeKontakta(imenik)
        elif opcija == 4:
            izmjenaKontakta(imenik)
        elif opcija == 5:
            ispisPoIndexu(imenik)