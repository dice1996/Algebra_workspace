"""
Zadatak za vjezbu:

Napraviti dictionary

_todo = {
    "id": 1,
    "zadatak": "Tekst što jos trebamo odraditi",
    "izvrsen": True/False
    "vrijemeKreiranja": timestamp,
    "vrijemeIzvrsavanja": timestamp
}

id - unique autoincrement

izbornik proizvoljan:
primjer:
0 - Izlaz
1 - Unos zadataka
2 - Toggle statusa
3 - Ispis svih izvrsenih zadataka
4 - Ispis svih neizvrsenih zadataka

Toggle nam oznacava promjenu stanja (kao upali/ugasi svijetlo)
Dakle ako je status True - toggle ce ga pretvoriti u False i obrnuto

Rjesenje poslati na
andreas.grdjan@predavaci.algebra.hr

""" 
import time
from datetime import datetime as dt
from prettytable import PrettyTable, ALL
import os

"""
todo={
    "id": 1, - autoincrement
    "zadatak": "Tekst što jos trebamo odraditi",
    "izvrsen": True/False
    "vrijemeKreiranja": timestamp,
    "vrijemeIzvrsavanja": timestamp
}
"""

todo=[]

glavniIzbornik = {
    1: "Unos zadataka",
    2: "Toggle statusa",
    3: "Ispis svih izvrsenih zadataka",
    4: "Ispis svih neizvrsenih zadataka",
    0: "Izlaz iz aplikacije"
}

def ocisti_ekran():
    os.system("cls" if os.name == "nt" else "clear")

def unesiCijeliBroj(text = None, index = None):
    while True:
        try:
            if text is None and index is None:
                return int(input("Unesi broj: "))
            elif text is None and index is not None:
                return int(input(f"Unesi {index}. broj: "))
            else:
                return int(input(text))
        except:
            print("Krivi unos")

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
            ocisti_ekran()
        else:
            if izbor == 0:
                ocisti_ekran()
                print("Kraj programa!")
                return 0
            else:
                return izbor

def unosZadatka(lista: list):
    ocisti_ekran()
    noviZadatak = {}

    if lista == []:
        noviZadatak["id"] = 1
    else:
        noviZadatak["id"] = lista[-1]["id"] + 1
    noviZadatak["zadatak"] = input("Unesi tekst zadatka (potvrdi pritiskom tipke Enter): ")
    noviZadatak["izvsen"] = False
    noviZadatak["vrijemeKreiranja"] = int(dt.now().timestamp())
    noviZadatak["vrijemeIzvrsavanja"] = None
    lista.append(noviZadatak)
    print("Podaci uspješno uneseni. Povratak u glavni izbornik...")
    time.sleep(2)
    ocisti_ekran()

def ispisZadataka(lista: list, index = None):
    ocisti_ekran()
    t = PrettyTable(["ID", "TEKST ZADATKA", "IZVRŠEN/NEIZVRŠEN", "VRIJEME KREIRANJA", "VRIJEME IZVRŠENJA"], padding_width = 3, hrules=ALL)
    if index == None:
        for item in lista:
            if item["vrijemeIzvrsavanja"] == None:
                t.add_row([item["id"], item["zadatak"], "\u274c", dt.fromtimestamp(item["vrijemeKreiranja"]).strftime("%d.%m.%Y. - %H:%M:%S"), "N/A"])
    else:
        for item in lista:
            if item["vrijemeIzvrsavanja"] != None:
                t.add_row([item["id"], item["zadatak"], "\u2713", dt.fromtimestamp(item["vrijemeKreiranja"]).strftime("%d.%m.%Y. - %H:%M:%S"), dt.fromtimestamp(item["vrijemeIzvrsavanja"]).strftime("%d.%m.%Y. - %H:%M:%S")])
    print(f"{t}\n")

def toggleStatusa(lista: list):
    ocisti_ekran()
    ispisZadataka(lista)
    izbor = unesiCijeliBroj("Unesi ID zadatka kojem želiš promijeniti status: ")
    flag = False
    for item in lista:
        if item["id"] == izbor and item["vrijemeIzvrsavanja"] == None:
            flag = True
    if flag == False:
        print("Pogrešan ID. Pokušaj ponovno...")
        time.sleep(2)
        ocisti_ekran()
    else:
        lista[izbor - 1]["izvrsen"] = True
        lista[izbor - 1]["vrijemeIzvrsavanja"] = int(dt.now().timestamp())
        print("Podaci uspješno uneseni. Povratak u glavni izbornik...")
        time.sleep(2)
        ocisti_ekran()

if __name__ == "__main__":
    flag = True
    ocisti_ekran()
    while flag:
        opcija = unosOpcije(glavniIzbornik)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            unosZadatka(todo)
        elif opcija == 2:
            toggleStatusa(todo)
        elif opcija == 3:
            ispisZadataka(todo, 1)
        elif opcija == 4:
            ispisZadataka(todo)