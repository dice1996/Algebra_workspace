"""
Napraviti aplikaciju za kupovanje artikla iz ducana.
Cilj je da s kupcem kupite robu.

Informacije o kupcu i robi stavite proizvoljno.

Bitna pravila su da kupac ima id (1, 2, 3...), a roba (00001, 00002) itd. dakle, minimalno 5 znamenkaa za id robe(oba su autoincrement)
Prije nego kupac krene kupovat da ga pitate kojom valutom ce platiti.
Kupac unosi string "kn" ili "€".
Cijene na robi su prikazane dvojno, a na racunu naplatite kupcu u valuti koju je odabrao.
Kupac kupuje, odabire proizvode, do kad ne pritisne 0, nakon što je korisnik pritisnuo 0, ispisuje se racun u formatu:

Racun za kupca [ime prezime] - [id]
Artikli:
    naziv artikla: cijena kolicina ukupno (cijena*kolicina)
    ...
    ...

Za platiti: ukupno (od svih artikala) kuna

cijena proizvoda se upisuje u kunama

"""

import time
from datetime import datetime as dt
from prettytable import PrettyTable, ALL
import os

#roba = []
kupac = []

roba = [
    {
        "id": "00001",
        "artikl": "mlijeko",
        "cijena": 8.99,
        "kolicina": 3
    },
    {
        "id": "00002",
        "artikl": "kruh",
        "cijena": 7.99,
        "kolicina": 8
    },
    {
        "id": "00003",
        "artikl": "Coca Cola",
        "cijena": 13.99,
        "kolicina": 6
    }
]
TECAJ = 7.5345

"""
kupac = [
    {
        "id": 1,
        "ime": Dino,
        "prezime": Cerjak,
        "valuta": €
    },
    {
        "id": 2,
        "ime": Ante,
        "prezime": Janjic,
        "Valuta": kn
    }
]

"""
glavniIzbornik = {
    1: "Dodaj proizvod",
    2: "Kreni u kupovinu",
    0: "Izlaz iz aplikacije"
}


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def ispisIzbornika(izbornik):
    for item in izbornik:
        print(f"{item}. {izbornik[item]}")

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

def unosOpcije(izbornik):
    while True:
        print("GLAVNI IZBORNIK\n")
        ispisIzbornika(izbornik)
        izbor = unesiCijeliBroj("\nUnesi opciju iz gornjeg izbornika: ")
        if izbor not in izbornik.keys():
            print("Unije validan unos! Pokusaj ponovno!")
            time.sleep(2)
            clear_screen()
        else:
            if izbor == 0:
                clear_screen()
                #print("Kraj programa!")
                return 0
            else:
                return izbor

def unosProizvoda(roba: list):
    clear_screen()
    proizvod = dict()
    if roba == []:
        proizvod["id"] = str(1).zfill(5)
    else:
        proizvod["id"] = str(int(roba[-1]["id"]) + 1).zfill(5)
    proizvod["artikl"] = input("Unesi ime proizvoda: ").upper()
    while True:
        try:
            proizvod["cijena"] = float(input("Unesi cijenu u kunama: "))
            break
        except:
            print("Unos nije validan. Pokusaj ponovno...")
    while True:
        try:
            proizvod["kolicina"] = int(input("Unesi kolicinu: "))
            break
        except:
            print("Unos nije validan. Pokusaj ponovno...")
    
    roba.append(proizvod)
    print("Podaci uspješno uneseni. Povratak u glavni izbornik...")
    time.sleep(2)
    clear_screen()

def ispisProizvoda(roba: list, index = None):
    if index == 1:
        t = PrettyTable(["SIFRA PROIZVODA", "NAZIV", "CIJENA (kn)", "KOLICINA"], padding_width = 4, hrules=ALL)
        for proizvod in roba:
                t.add_row([proizvod["id"], proizvod["artikl"], proizvod["cijena"], proizvod["kolicina"]])
    else:
        t = PrettyTable(["SIFRA PROIZVODA", "NAZIV", "CIJENA (€)", "KOLICINA"], padding_width = 4, hrules=ALL)
        for proizvod in roba:
                t.add_row([proizvod["id"], proizvod["artikl"], round(proizvod["cijena"]/index, 2), proizvod["kolicina"]])
    print(f"{t}\n")

def ispisKosarice(kosarica: list, valuta):
    print("Trenutno stanje kosarice:")
    if valuta == "kn":
        t = PrettyTable(["SIFRA PROIZVODA", "NAZIV", "KOLICINA", "CIJENA"], padding_width = 4, hrules=ALL)
        for proizvod in kosarica:
            t.add_row([proizvod["id"], proizvod["artikl"], proizvod["kolicina"], proizvod["cijena"]*proizvod["kolicina"] ])
    else:
        t = PrettyTable(["SIFRA PROIZVODA", "NAZIV", "KOLICINA", "CIJENA (€)"], padding_width = 4, hrules=ALL)
        for proizvod in kosarica:
            t.add_row([proizvod["id"], proizvod["artikl"], proizvod["kolicina"], round(proizvod["cijena"]*proizvod["kolicina"]/TECAJ, 2) ])
    print(f"{t}\n")

def kupovina (roba: list, kupac: list):
    clear_screen()
    novi_kupac = {}
    novi_kupac = unosKupca(kupac)
    ime = novi_kupac["ime"]
    valuta = novi_kupac["valuta"]
    clear_screen()
    print(f"Pozdrav {ime}, dobrodosao u kupovinu!\nOvo je lista proizvoda s dostupnim kolicinama:")
    if valuta == "€":
        ispisProizvoda(roba, TECAJ)
    else:
        ispisProizvoda(roba, 1)
    time.sleep(1)
    print("Upute za kupovinu su vrlo jednostavne:\n\t1. Za odabir proizvoda unosis njegovu sifru\n\t2. Nakon toga je potrebno unijeti kolicinu\n\t3. Kako bi zavrsio unos, unesi broj 0\nKupovina moze zapoceti! Sretno!\n")
    time.sleep(3)
    pokreni_kupovinu(roba, novi_kupac, valuta)

def pokreni_kupovinu (roba: list, novi_kupac, valuta = "kn"):
    clear_screen()
    if valuta == "kn":
        index = 1
    else:
        index = TECAJ
    kosarica = []
    while True:
        if kosarica == []:
            print("Vasa kosarica je trenutno prazna.")
        else:
            ispisKosarice(kosarica, valuta)
        proizvod = dict()
        print("\nPopis dostupnih proizvoda:")
        ispisProizvoda(roba, index)
        print("Za prekid unesi '0'!\n")
        idProizvoda = input("Unesi ID proizvoda s liste: ")
        if idProizvoda == "0":
            break
        else:
            flag = False
            for item in roba:
                if item["id"] == idProizvoda:
                    proizvod = item
                    flag = True
            if flag == False:
                print("Pogresan ID. Pokusaj ponovno...")
                time.sleep(2)
                clear_screen()
            else:
                while True:
                    try:
                        kolicina = int(input("Unesi kolicinu: "))
                        for item in roba:
                            if item["id"] == idProizvoda:
                                if item["kolicina"] < kolicina:
                                    print("Kolicna je veca od trenutne. Pokusaj ponovno!")
                                    time.sleep(2)
                                    clear_screen()
                                else:
                                    item["kolicina"] = item["kolicina"] - kolicina
                                    proizvod["kolicina"] = kolicina
                                    break                            
                        kosarica.append(proizvod)
                        clear_screen()
                        break
                    except:
                        print("Pogresna kolicina. Probaj ponovno!")

    ispisRacuna(kosarica, valuta, novi_kupac)      

def ispisRacuna(kosarica: list, valuta, novi_kupac):
    clear_screen()
    ime = novi_kupac["ime"] + " " + novi_kupac["prezime"] + " - " + str(novi_kupac["id"])
    valuta = novi_kupac["valuta"]
    print("Racun za kupca {ime}")
    print("Artikli:")
    ukupno = 0
    for item in kosarica:
        if valuta == "€":
            print(f"\t" + item["artikl"] + ":\t" + str(item["kolicina"]) + "\t" + str(round(item["cijena"]*item["kolicina"]/TECAJ, 2)))
            if item["kolicina"] > 1:
                ukupno = ukupno + item["cijena"] * item["cijena"]
            else:
                ukupno = ukupno + item["cijena"]
        else:
            print(f"\t" + item["artikl"] + ":\t" + str(item["kolicina"]) + "\t" + str(round(item["cijena"]*item["kolicina"], 2)))
            if item["kolicina"] != 1:
                ukupno = ukupno + item["cijena"] * item["kolicina"]
            else:
                ukupno = ukupno + item["cijena"]
    if valuta == "€":
        print(f"Za platiti: ukupno {ukupno}€\n")
    else:
        print(f"Za platiti: ukupno {ukupno}kn\n")
    time.sleep(2)
        

def unosKupca(kupac: list):
    novi_kupac = dict()

    if kupac == []:
        novi_kupac["id"] = 1
    else:
        novi_kupac["id"] = kupac[-1]["id"] + 1
    novi_kupac["ime"] = input("Unesi ime kupca: ")
    novi_kupac["prezime"] = input("Unesi prezime kupca: ")
    while True:
        novi_kupac["valuta"] = input("Unesi valutu kupovine (kn/€): ")
        if novi_kupac["valuta"] == "kn" or novi_kupac["valuta"] == "€":
            break
        else:
            print("Nije dobar izbor valute. Ponovi unos...")
    kupac.append(novi_kupac)
    return novi_kupac

if __name__ == "__main__":
    flag = True
    clear_screen()
    while flag:
        opcija = unosOpcije(glavniIzbornik)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            unosProizvoda(roba)
        elif opcija == 2:
            kupovina(roba, kupac)