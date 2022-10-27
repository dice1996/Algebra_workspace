"""
Vi ste tvrtka za veleprodaju pića. Imate skladiste pića i vaši klijenti su kafići.
Kreirate kasu za skladiste pića

Model kase sadrzi listu kafica i listu racuna.

Funkcionalnosti koje kasa treba imati su:
1 - Dodaj kafic - id, naziv, vlasnik, grad, KOD, polog, vrijemeKreiranja
KOD se ne upisuje nego se generira prema uputama:
KOD kafica je u formatu [id]-[prva dva slova naziva]-[trenutna godina]-[prva dva slova grada] 
prva dva slova naziva i grada nek budu velika stampana slova bez obzira ako se unose malim slovima s tipkovnice (hint lower() i upper())

Opcionalno ko zeli malo znojenja  ko ne zeli, odabrat ID po zelji (unos ili autoincrement) ali da bude unique.
ID kafica mora imati minimalno 3 znamenke (koristite autoincrement, dakle za prvi ID = 1, i za svaki unesen kafic se poveca za 1 (0 se dodaju ispred svakog IDa 001, 002, 003, 004 ... 098, 099, 100) dakle uvijek su minimalno 3 znamenke, a 0 dodajemo po potrebi)

npr:    id kafica: 001
        naziv kafica: Envy
        grad: Varaždin
        KOD: 001-EN-2022-VA

2 - Ispisi sve kafice
3 - Izdaj racun kaficu (blagajnik upise iznos racuna i taj iznos se oduzima iz pologa kafica)
4 - Polozi novce kaficu
5 - Povijest prodaje (ispis svih racuna) + ukupan zaraden iznos
0 - Izlaz iz aplikacije

racuni je dictionary koji u listu sprema dictionary racun koji sadrzi id kafica, iznos koji je kafic platio i
vrijeme prodaje (zamislite kao racun koji isporucite kaficu kad kupuje kod vas) 

kasa = {
    "kafici": [],
    "racuni": []
}

kafic = {
    "id": None,
    "naziv": None,
    "vlasnik": None,
    "grad": None,
    "KOD": None,
    "polog": 0,
    "vrijemeKreiranje": None
}

racun = {
    "kaficID": None,
    "iznos": None,
    "vrijeme_izdavanja": None
}
"""
from os import system
from pomocne_funkcije import *
import time
from datetime import datetime as dt
from prettytable import PrettyTable

kasa = {
    "kafici": [],
    "racuni" : []
}

glavniIzbornik = {
    1: "Dodaj kafic",
    2: "Ispisi sve kafice",
    3: "Izdaj racun kaficu",
    4: "Polozi novce kaficu",
    5: "Povijest prodaje",
    0: "Izlaz iz aplikacije"
}

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

def dodajKafic(lista: list):
    system("clear")
    kafic = dict()
    if lista == []:
        kafic["id"] = str(1).zfill(3)
    else:
        kafic["id"] = str(int(lista[-1]["id"]) + 1).zfill(3)
    kafic["naziv"] = input("Unesi ime kafica: ").upper()
    kafic["vlasnik"] = input("Unesi vlasnika kafica: ").upper()
    kafic["grad"] = input("Unesi grad kafica: ").upper()
    kafic["polog"] = float(input("Unesi polog kafica u kunama: "))
    kafic["vrijemeKreiranje"] = int(dt.now().timestamp())
    kafic["KOD"]= str(kafic["id"]) + "-" + kafic["naziv"][:2] + "-" + dt.now().strftime("%Y") + "-" + kafic["grad"][:2]
    lista.append(kafic)
    print("Podaci uspješno uneseni. Povratak u glavni izbornik...")
    time.sleep(2)
    system("clear")

def funkcijaIspisaKafica(lista: list, index = None):
    system("clear")
    t = PrettyTable(["ID", "KAFIC", "VLASNIK", "GRAD", "POLOG", "KOD KAFICA", "KREIRANO"], padding_width = 4)
    if index == None:
        print(f"Popis sadrži {len(lista)} objekat/a:")
        for item in lista:
            t.add_row([item["id"], item["naziv"], item["vlasnik"], item["grad"], item["polog"], item["KOD"], dt.fromtimestamp(item["vrijemeKreiranje"]).strftime("%H:%M:%S - %d.%m.%Y.")])
    else:
        uniqeitem = lista[index-1]
        t.add_row([uniqeitem["id"], uniqeitem["naziv"], uniqeitem["vlasnik"], uniqeitem["grad"], uniqeitem["polog"], uniqeitem["KOD"], dt.fromtimestamp(uniqeitem["vrijemeKreiranje"]).strftime("%H:%M:%S - %d.%m.%Y.")])  
    print(f"{t}\n")

def funkcijaIspisaRacuna(lista: list, index = None):
    system("clear")
    ukupno = 0
    t = PrettyTable(["ID KAFICA", "IZNOS RACUNA", "KREIRANO"], padding_width = 4)
    if index == None:
        print(f"Popis sadrži {len(lista)} racun/a:")
        for item in lista:
            t.add_row([item["kaficID"], item["iznos"], dt.fromtimestamp(item["vrijeme_izdavanja"]).strftime("%H:%M:%S - %d.%m.%Y.")])
            ukupno += item["iznos"]
    else:
        uniqeitem = lista[index-1]
        t.add_row([uniqeitem["kaficID"], uniqeitem["iznos"], dt.fromtimestamp(uniqeitem["vrijeme_izdavanja"]).strftime("%H:%M:%S - %d.%m.%Y.")])  
    print(f"{t}\n")
    print(f"Ukupan iznos izdanih racuna je {ukupno} kn.\n")

def dodajRacun(listaKafica: list, listaRacuna: list):
    system("clear")
    noviRacun = {}
    funkcijaIspisaKafica(listaKafica)
    izbor = unesiCijeliBroj("\nUnesi ID kafica za izdavanje racuna: ")
    flag = False
    for element in listaKafica:
        if int(element["id"]) == izbor:
            flag = True
            break
        else:
            pass
    if flag != True:
        print("Pograsan ID unesen. Povratak u glavni izbornik...")
    else:
        noviRacun["kaficID"] = str(izbor).zfill(3)
        while True:
            try:
                noviRacun["iznos"] = float(input("Unesi iznos racuna u kunama: "))
                break
            except:
                print("Pogresan unos. Pokusaj ponovno!")
        noviRacun["vrijeme_izdavanja"] = int(dt.now().timestamp())

        listaRacuna.append(noviRacun)
        azurirajIznosPologa(listaKafica, noviRacun["iznos"], izbor, "-" )

        print("Podaci uspješno uneseni. Povratak u glavni izbornik...")
    time.sleep(2)
    system("clear")

def azurirajIznosPologa(listaKafica: list, iznos: float, izbor : int, operation = None):
    item = listaKafica[izbor-1]
    if operation == None:        
        item["polog"] = float(item["polog"]) + iznos
    elif operation == "-":
        item["polog"] = float(item["polog"]) - iznos

def dodajPolog(listaKafica: list):
    system("clear")
    funkcijaIspisaKafica(listaKafica)
    izbor = unesiCijeliBroj("\nUnesi ID kafica za izdavanje racuna: ")
    flag = False
    for element in listaKafica:
        if int(element["id"]) == izbor:
            flag = True
            break
        else:
            pass
    if flag != True:
        print("Pograsan ID unesen. Povratak u glavni izbornik...")
    else:
        while True:
            try:
                iznos = float(input("Unesi iznos pologa u kunama: "))
                break
            except:
                print("Pogresan unos. Pokusaj ponovno!")
        azurirajIznosPologa(listaKafica, iznos, izbor)
        print("Podaci uspješno uneseni. Povratak u glavni izbornik...")
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
            dodajKafic(kasa["kafici"])
        elif opcija == 2:
            funkcijaIspisaKafica(kasa["kafici"])
        elif opcija == 3:
            dodajRacun(kasa["kafici"], kasa["racuni"])
        elif opcija == 4:
            dodajPolog(kasa["kafici"])
        elif opcija == 5:
            funkcijaIspisaRacuna(kasa["racuni"])