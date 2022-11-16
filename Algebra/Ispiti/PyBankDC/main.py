"""
Kreirajte folder PyBankAG (dakle nakon PyBank stavite vase inicijale)
te u njemu kreirajte jednu datoteku u koju ćete upisivati Vaš Python kôd.
2. Funkcionalnosti koje program treba imati su:
    a. Kreiranje računa Tvrtke
        Tvrtka ima podatke: Naziv, Ulica i broj, Poštanski broj sjedišta, Grad sjedišta,
        OIB (mora imati točno 11 znakova), Ime i prezime odgovorne osobe.
        i. Kod otvaranja računa treba položiti iznos po volji
        ii. Treba odabrati valutu računa EUR ili HRK
        iii. Račun generirati broj računa u formatu:
        1. BA-GODINA-MJESEC-Redni_broj
            Primjer: BA-2022-11-00001
        2. BA - oznaka za Business Account
        3. Redni_broj - 00001 – 5 znamenki i mora imati nule ispred ako
           je manji od 10 tisuća.
    b. Prikaz stanja računa
    c. Prikaz prometa po računu
    d. Polog novca na račun
    e. Podizanje novca s računa
    f. Izlaz iz programa – program se izvršava cijelo vrijeme sve dok korisnik ne
    odabere opciju Izlaz iz glavnog izbornika.

Funkcije zadatka obavezno napisati u istom file-u. Ne koristimo import pomocne_funkcije.py
Kompresiranu datoteku foldera (zip/rar) poslati na email: andreas.grdjan@predavaci.algebra.hr 

tvrtka = {
    "id": "BA-GODINA-MJESEC-Redni_broj",
    "naziv": "TestTvrtka"
    "ulica": "TestUlicaIBroj",
    "postanskiBroj": 31220,
    "gradSjedista": "Osijek",
    "oib": 11111111111,
    "odgovornaOsoba": "TestImeIPrezime",
    "stanjeRacune": 1000,
    "valuta": "EUR ili HRK"
}

promet = {
    "id": "BA-GODINA-MJESEC-Redni_broj",
    "akcija": "IN/OUT",
    "iznos": 100,
    "created": datumivrijeme transakcije
}

"""

import time
from datetime import datetime as dt
from prettytable import PrettyTable, ALL
import os

# definiranje korištenih varijabli , lista, dictova,...
glavniIzbornik = {
    1: "Kreiranje računa Tvrtke",
    2: "Prikaz stanja računa",
    3: "Prikaz prometa po računu",
    4: "Polog novca na račun",
    5: "Podizanje novca s računa",
    0: "Kraj programa"
}

bazaRacuna = []
prometPoRacunima = []


#MODEL TVRTKE
ACC_ID = "id"
ACC_NAZIV = "naziv"
ACC_ULICA = "ulica"
ACC_POSTANSKI_BROJ = "postanskiBroj"
ACC_GRAD_SJEDISTA = "gradSjedista"
ACC_OIB = "oib"
ACC_ODGOVORNA_OSOBA = "odgovornaOsoba"
ACC_STANJE_RACUNA = "stanjeRacune"
ACC_VALUTA = "valuta"

#MODLE TRANSAKCIJA
TR_AKCIJA = "akcija" #može biti IN ili OUT
TR_IZNOS = "iznos"
TR_CREATED = "created"

#Standardne funkcije

def clear_screen():
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
            clear_screen()
        else:
            if izbor == 0:
                clear_screen()
                #print("Kraj programa!")
                return 0
            else:
                return izbor

#Ostale funkcije
def unesiOIB(s):
    while True: 
        try:   
            var = input(s)
            if len(var) != 11:
                print("Ponovi unos. Mora biti duljine 11 znakova...")
            else:
                int(var)
                return var
                break
        except:
            print("Nisu uneseni brojevi. Pokusati ponovno...") 

def novaTvrtka(bazaRacuna: list):
    clear_screen()
    godina = dt.today().strftime("%Y")
    mjesec = dt.today().strftime("%m")
    tvrtka = dict()
    tvrtka[ACC_ID] = f"BA-{godina}-{mjesec}-{str(len(bazaRacuna) + 1).zfill(5)}"
    tvrtka[ACC_NAZIV] = input("Unesi ime Tvrtke: ")
    tvrtka[ACC_ULICA] = input("Unesi ulicu i broj sjedišta Tvrtke: ")
    tvrtka[ACC_POSTANSKI_BROJ] = unesiCijeliBroj("Unesi poštanski broj sjedišta Tvrtke: ")
    tvrtka[ACC_GRAD_SJEDISTA] = input("Unesi mjesto sjedišta Tvrtke: ")
    tvrtka[ACC_OIB] = unesiOIB("Unesi OIB Tvrtke: ")
    tvrtka[ACC_ODGOVORNA_OSOBA] = input("Unesi ime i prezime odgovorne osobe Tvrtke: ")
    while True:
        helper = input("Unesi valutu računa kojeg otvarate (HRK/EUR): ")
        if helper.upper() == "HRK" or helper.upper() == "EUR":
            tvrtka[ACC_VALUTA] = helper
            break
        else:
            print("Nije upisana ispravna valuta. Molim unijeti HRK ili EUR!")

    tvrtka[ACC_STANJE_RACUNA] = unesiCijeliBroj("Unesi polog racuna (unos mora biti cijeli broj): ")
    bazaRacuna.append(tvrtka) 
    print("Unos tvrtke uspjesan! Povratak u glavni izbornik...")
    time.sleep(2)
    clear_screen()   

def stanjeRacuna(bazaRacuna: list):
    clear_screen()
    id_racuna = input("Unesi zadnjih 5 znamenaka svoga racuna: ")
    datum = dt.today().strftime("%d.%m.%Y")
    flag = False
    for racun in bazaRacuna:
        string = racun[ACC_ID]
        string = string.split("-")
        id_tvrtke = string[-1]
        if id_tvrtke == id_racuna:
            print(f"Stanje racuna {racun[ACC_ID]} na dan {datum} iznosi {racun[ACC_STANJE_RACUNA]} {racun[ACC_VALUTA]}")
            flag = True
            time.sleep(5)
            clear_screen()
    if flag != True:
        print("Uneseni ID racuna ne postoji. Povratak u glavni izbornik.")
        time.sleep(2)
        clear_screen()

def polog(bazaRacuna: list, prometPoRacunima: list):
    clear_screen()
    id_racuna = input("Unesi zadnjih 5 znamenaka svoga racuna: ")
    datum = dt.today().strftime("%d.%m.%Y")
    promet = {}
    flag = False
    for racun in bazaRacuna:
        string = racun[ACC_ID]
        string = string.split("-")
        id_tvrtke = string[-1]
        if id_tvrtke == id_racuna:
            print(f"Stanje racuna {racun[ACC_ID]} na dan {datum} iznosi {racun[ACC_STANJE_RACUNA]} {racun[ACC_VALUTA]}\n")
            iznosPologa = unesiCijeliBroj(f"Unesi polog za racun {racun[ACC_ID]} u valuti {racun[ACC_VALUTA]} (koristi krupne iznose): ")
            racun[ACC_STANJE_RACUNA] += iznosPologa
            promet[ACC_ID] = racun[ACC_ID]
            promet[TR_AKCIJA] = "IN"
            promet[TR_IZNOS] = iznosPologa
            promet[TR_CREATED] = int(dt.now().timestamp())
            prometPoRacunima.append(promet)
            flag = True
            print("Polog uspješno dodan. Povratak u glavni izbornik...")
            time.sleep(2)
            clear_screen()
    if flag != True:
        print("Uneseni ID racuna ne postoji. Povratak u glavni izbornik.")
        time.sleep(2)
        clear_screen()

def podizanje(bazaRacuna:list, prometPoRacunima: list):
    clear_screen()
    clear_screen()
    id_racuna = input("Unesi zadnjih 5 znamenaka svoga racuna: ")
    datum = dt.today().strftime("%d.%m.%Y")
    promet = {}
    flag = False
    for racun in bazaRacuna:
        string = racun[ACC_ID]
        string = string.split("-")
        id_tvrtke = string[-1]
        if id_tvrtke == id_racuna:
            print(f"Stanje racuna {racun[ACC_ID]} na dan {datum} iznosi {racun[ACC_STANJE_RACUNA]} {racun[ACC_VALUTA]}")
            iznosPodizanja = unesiCijeliBroj(f"Unesi iznos podizanja za racun {racun[ACC_ID]} u valuti {racun[ACC_VALUTA]} (koristi krupne iznose): ")
            if iznosPodizanja <= racun[ACC_STANJE_RACUNA]:
                racun[ACC_STANJE_RACUNA] -= iznosPodizanja
                promet[ACC_ID] = racun[ACC_ID]
                promet[TR_AKCIJA] = "OUT"
                promet[TR_IZNOS] = iznosPodizanja
                promet[TR_CREATED] = int(dt.now().timestamp())
                prometPoRacunima.append(promet)
                flag = True
                print("Novac uspješno podignut. Povratak u glavni izbornik...")
                time.sleep(2)
                clear_screen()
            else:
                print(f"Iznos koji zelite podici prelazi stvarno stanje. Najvise sto mozete povuci je {racun[ACC_STANJE_RACUNA]} {racun[ACC_VALUTA]}!")
                time.sleep(2)
                print("Transakcija otkazana. Povratak u glavni izbornik...")
                time.sleep(2)
                clear_screen()
    if flag != True:
        print("Uneseni ID racuna ne postoji. Povratak u glavni izbornik.")
        time.sleep(2)
        clear_screen()

def ispisPrometa(bazaRacuna:list, prometPoRacunima: list):
    clear_screen()
    id_racuna = input("Unesi zadnjih 5 znamenaka svoga racuna: ")
    promet = {}
    flag = False
    for racun in bazaRacuna:
        string = racun[ACC_ID]
        string = string.split("-")
        id_tvrtke = string[-1]
        if id_tvrtke == id_racuna:
            clear_screen()
            ukupanPromet = 0
            print(f"PROMET PO RACUNU {racun[ACC_ID]}:\n")
            t = PrettyTable(["ID RACUNA", "NAZIV TVRTKE", "IZNOS TRANSAKCIJE", "TRANSAKCIJA", "VRIJEME TRANSAKCIJE"], padding_width = 3, hrules=ALL)
            for item in prometPoRacunima:
                string = item[ACC_ID]
                string = string.split("-")
                id_racun = string[-1]
                if id_tvrtke == id_racun:
                    t.add_row([item[ACC_ID], racun[ACC_NAZIV], item[TR_IZNOS], item[TR_AKCIJA], dt.fromtimestamp(item[TR_CREATED]).strftime("%d.%m.%Y.")])
                    ukupanPromet += item[TR_IZNOS]
            print(f"{t}\nUkupan promet po racunu do danas iznosi {ukupanPromet} {racun[ACC_VALUTA]}.\n")
            print(f"Trenutno stanje racuna iznosi {racun[ACC_STANJE_RACUNA]} {racun[ACC_VALUTA]}.\n")
            time.sleep(3)
            print("Povratak u glavni izbornik...\n")
            time.sleep(2)
            flag = True
    if flag != True:
        print("Uneseni ID racuna ne postoji. Povratak u glavni izbornik.")
        time.sleep(2)
        clear_screen()

# if name is main
if __name__ == "__main__":
    flag = True
    clear_screen()
    while flag:
        opcija = unosOpcije(glavniIzbornik)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            novaTvrtka(bazaRacuna)
        elif opcija == 2:
            stanjeRacuna(bazaRacuna)
        elif opcija == 3:
            ispisPrometa(bazaRacuna, prometPoRacunima)
        elif opcija == 4:
            polog(bazaRacuna, prometPoRacunima)
        elif opcija == 5:
            podizanje(bazaRacuna, prometPoRacunima)