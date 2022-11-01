"""
Kreirati softver za videoteku. Arhitektura je proizvoljna.

id_naloga

kreirati u formatu npr: 001-ID_KORISNIKA-ID_FILMA-GODINA

001-025-018-2022

"""
import time
from datetime import datetime as dt
from prettytable import PrettyTable, ALL
import os
from popis_filmova import *
from popis_korisnika import *

izdani_filmovi = []

glavniIzbornik = {
    1: "Ispis svih članova",
    2: "Ispis posuđenih filmova",
    3: "Posudi film",
    4: "Vrati film",
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
                ocisti_ekran()
                return izbor

def funkcijaIspisa(lista: list, index = None):
    ocisti_ekran()
    if index == None:
        t = PrettyTable(["ID", "IME", "SRANJE RAČUNA", "VRIJEME UČLANJENJA"], padding_width = 3, hrules=ALL)
        print(f"Popis sadrži {len(lista)} članova:")
        for item in lista:
            t.add_row([str(item["id"]).zfill(3), item["ime"], item["stanje_racuna"], dt.fromisoformat(item["vrijeme_kreiranja"]).strftime("%d.%m.%Y.")])
    else:
        t = PrettyTable(["ID NALOGA", "IME KUPCA", "IME FILMA", "VRIJEME POSUDBE", "FILM VRAĆEN"], padding_width = 3, hrules=ALL)
        for mainItem in lista:
            t.add_row([str(mainItem["id_naloga"]), mainItem["ime_kupca"], mainItem["ime_filma"], dt.fromisoformat(mainItem["vrijeme_kreiranja"]).strftime("%d.%m.%Y."), ""])
    print(f"{t}\n")

def posudiFilm(lista: list):
    ocisti_ekran()
    novi_nalog = {}
    izbor = unesiCijeliBroj("Unesi ID člana koji pouđuje film: ")
    flag = False
    for item in popis_korisnika:
        if item["id"] == izbor:
            flag = True
   
    if flag == False:
        print("Pogresan ID. Pokusaj ponovno...")
    else:
        flag = False 
        odluka = search(input("Unesi jednu do dvije riječi imena filma: ")) 
        if odluka == 0:
            print("Nema filma na popisu. Povratak u glavni izbornik...")
            time.sleep(2)
            ocisti_ekran()
        else:
            izbor_film = unesiCijeliBroj("Unesi ID filma koji član posuđuje (unesi 0 za prekid): ")
            for item in popis_filmova:
                if izbor_film == item["id"]:
                    flag = True
            if flag == False:
                if izbor_film == 0:
                    print("Povratak u glavni izbornik...")
                else:
                    print("Pogresan ID. Pokusaj ponovno...")
                time.sleep(2)
                ocisti_ekran()
            else:
                if lista == []:
                    novi_nalog["id_naloga"] = str(1).zfill(3) + "-" + str(izbor).zfill(3) + "-" + str(izbor_film).zfill(3) + "-" + dt.now().strftime("%Y")
                else:
                    pomocna = lista[-1]["id_naloga"]
                    pomocna_lista = pomocna.split("-")
                    novi_nalog["id_naloga"] = str(int(pomocna_lista[0]) + 1).zfill(3) + "-" + str(izbor).zfill(3) + "-" + str(izbor_film).zfill(3) + "-" + dt.now().strftime("%Y")
                
                novi_nalog["id_kupca"] = izbor
                novi_nalog["id_filma"] = izbor_film
                for item1 in popis_korisnika:
                    if item1["id"] == izbor:
                        novi_nalog["ime_kupca"] = item1["ime"]
                for item2 in popis_filmova:
                    if item2["id"] == izbor_film:
                        novi_nalog["ime_filma"] = item2["ime"]
                novi_nalog["vrijeme_kreiranja"] = dt.now().strftime("%Y-%m-%d")
                lista.append(novi_nalog)
                print("Podaci uspješno uneseni. Povratak u glavni izbornik...")
                time.sleep(2)
                ocisti_ekran()

def search(ime):
    lista_pretrage = ime.split()
    novi_popis = []
    for item in popis_filmova:
        for word in lista_pretrage:
            if word in item["ime"].lower():
                novi_popis.append(item)
    novi_popis = [i for n, i in enumerate(novi_popis) if i not in novi_popis[:n]]
    if novi_popis == []:
        return 0
    else:
        t = PrettyTable(["ID", "IME FILMA", "GODINA FILMA"], padding_width = 3, hrules=ALL)
        for item in novi_popis:
            t.add_row([str(item["id"]), item["ime"], dt.fromisoformat(item["datum"]).strftime("%Y")])
        print(f"{t}\n")

if __name__ == "__main__":
    flag = True
    ocisti_ekran()
    while flag:
        opcija = unosOpcije(glavniIzbornik)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            funkcijaIspisa(popis_korisnika)
        elif opcija == 2:
            funkcijaIspisa(izdani_filmovi, 1)
        elif opcija == 3:
            posudiFilm(izdani_filmovi)
        elif opcija == 4:
            pass