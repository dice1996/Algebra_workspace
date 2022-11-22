"""
Napraviti videoteku.
Pomocu zadanih modela kreirati podatake o filmovima i korisnicima koristeci izbornik.

model videoteke je dictionary, koji u sebi sadrzi tri liste s kljucevima listaKorisnika, listaFilmova i listaPovijest.
model korisnika: id, ime, prezime, oib, created
model filma: id, naziv, redatelj, godina, posuden, korisnikID
model povijest: korisnikID, filmID, akcija, datum
akcija predstavlja string POSUDEN i VRACEN, dakle u povijest zapisujemo npr.
(1, 001, POSUDIO, timestamp) - koristiti i vrijeme s obzirom da necemo raditi kroz vise dana
(1, 001, VRATIO, timestamp)

ID i od korisnika i od filma se povecava sam (ne upisuje ga korisnik).
ID korisnika je obican broj (1, 2, 3...), dok za film ID treba posjedovati minimalno 3 znamenaka (001, 002, 003,....)

Aplikacija mora sadrzavati:

Upis filma
Upis korisnika
Posudi film
Vrati film
Ispis videoteke
Izadi iz aplikacije

izbornik ispis videoteke:
Ispis korisnika
Ispis filmova
Ispis povijesti

Kod upisa filma, korisnik upisuje samo naziv, redatelja i godinu
(id se zapise sam, posuden se postavlja na False, a korisnikID ostavljamo None).

Kod opcije posudi film:
prvo upisujemo id korisnika koji posuduje film, nakon toga id filma koji zeli posuditi.
film se ne moze posuditi ako je vec posuden.
kada korisnik posudi film (ako je sve kako bi trebalo biti)
u film se zapise posuden: True, i ID korisnika koji je posudio film.

vrati film (id - isti postupak kao i posudi film).
Kada korisnik vraca film, treba se provjeriti da li je pod filmom koji vraca njegov (korisnikov) ID.
Ako je uvjet ispunjen, korisnikID postaje None i posuden False

"""
import time
from datetime import datetime as dt
from prettytable import PrettyTable, ALL
import os

videoteka = {
    "listaKorisnika": [],
    "listaFilmova": [],
    "listaPovijesti": []
}

#MODEL KORISNIKA
USER_ID = "id"
USER_FIRST_NAME = "ime"
USER_LAST_NAME = "prezime"
USER_PIN = "oib"
USER_CREATED = "created"

#MODEL FILMA
MOVIE_ID = "id"
MOVIE_NAME = "naziv"
MOVIE_DIRECTOR = "redatelj"
MOVIE_YEAR = "godina"
MOVIE_RENTED = "posuden"
MOVIE_USERID = "korisnikID"

#MODEL POVIJESTI
HISTORY_USERID = "korisnikID"
HISTORY_MOVIEID = "filmID"
HISTORY_ACTION = "akcija"
HISTORY_DATE = "datum"

glavniIzbornik = {
    1: "Upis filma",
    2: "Upis korisnika",
    3: "Posudi film",
    4: "Vrati film",
    5: "Ispis videoteke",
    0: "Izlaz iz aplikacije"
}

podizbornikispisa = {
    1: "Ispis korisnika",
    2: "Ispis filmova",
    3: "Ispis povijesti",
    0: "Povratak"
}

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

def inputUser(users: list):
    clear_screen()
    user = {}
    if users == []:
        user[USER_ID] = 1
    else:
        user[USER_ID] = users[-1][USER_ID] + 1
    user[USER_FIRST_NAME] = input("Unesi ime korisnika: ")
    user[USER_LAST_NAME] = input("Unesi prezime korisnika: ")
    while True: 
        try:   
            var = input("Unesi OIB korisnika: ")
            if len(var) != 11:
                print("Ponovi unos OIB-a. Mora biti duljine 11 znakova...")
            else:
                int(var)
                user[USER_PIN] = var
                break
        except:
            print("Nisu uneseni brojevi. Pokusati ponovno...") 
    user[USER_CREATED] = int(dt.now().timestamp())
    users.append(user)
    print("Unos korisnika uspjesan! Povratak u glavni izbornik...")
    time.sleep(2)
    clear_screen()

def inputMovies(movies: list):
    clear_screen()
    movie = {}
    if movies == []:
        movie[MOVIE_ID] = str(1).zfill(3)
    else:
        movie[MOVIE_ID] = str(int(movies[-1][MOVIE_ID]) + 1).zfill(3)
    movie[MOVIE_NAME] = input("Unesi ime filma: ")
    movie[MOVIE_DIRECTOR] = input("Unesi redatelja filma: ")
    movie[MOVIE_YEAR] = input("Unesi godinu filma: ")
    movie[MOVIE_RENTED] = False
    movie[MOVIE_USERID] = None
    movies.append(movie)
    print("Unos filma uspjesan! Povratak u glavni izbornik...")
    time.sleep(2)
    clear_screen()

def rentMovie(users: list, movies: list, history: list):
    clear_screen()
    printFunction(movies, 2)

    izbor_filma = unesiCijeliBroj("Unesi ID filma kojeg zelis posuditi: ")
    flag = False
    for movie in movies:
        if int(movie[MOVIE_ID]) == izbor_filma:
            flag = True
    if flag == False:
        print("Pogresan ID. Pokusaj ponovno...")
        time.sleep(2)
        clear_screen()
    else:
        if movies[izbor_filma-1][MOVIE_RENTED] == True:
            print("Film je vec rentan. Povratak u glavni izbornik...")
            time.sleep(2)
            clear_screen()
        else:
            izbor = unesiCijeliBroj("Unesi ID korisnika: ")
            flag = False
            for user in users:
                if user[USER_ID] == izbor:
                    flag = True
            if flag == False:
                print("Pogresan ID. Pokusaj ponovno...")
                time.sleep(2)
                clear_screen()
            else:
                addHistory(izbor, izbor_filma, "POSUDEN", history)
                movies[izbor_filma-1][MOVIE_RENTED] = True
                movies[izbor_filma-1][MOVIE_USERID] = izbor
                print("Film rentan! Povratak u glavni izbornik...")
                time.sleep(2)
                clear_screen()

def returnMovie(users: list, movies: list, history: list):
    clear_screen()
    izbor = unesiCijeliBroj("Unesi ID korisnika koji vraća film: ")
    flag = False
    for movie in movies:
        if movie[MOVIE_USERID] == izbor:
            flag = True
    if flag == False:
        print("Korisnik nema rentan niti jedan film. Povratak u glavni izbornik...")
        time.sleep(2)
        clear_screen()
    elif flag == True: 
        
        m_id = unesiCijeliBroj("Unesi ID filma kojeg korsinik vraca: ")
        if movies[m_id-1][MOVIE_USERID] == izbor:
            
            addHistory(izbor, m_id, "VRACEN", history)
            movies[m_id-1][MOVIE_RENTED] = False
            movies[m_id-1][MOVIE_USERID] = None
            print("Film vracen! Povratak u glavni izbornik...")
            time.sleep(2)
            clear_screen()
        else:
            print("Korisnik nije rentao ovaj film. Povratak u glavni izbornik...")
            time.sleep(2)
            clear_screen()

def addHistory(user, movie, action,  history: list):
    new = {}
    new[HISTORY_USERID] = user
    new[HISTORY_MOVIEID] = str(movie).zfill(3)
    new[HISTORY_ACTION] = action
    new[HISTORY_DATE] = int(dt.now().timestamp())
    history.append(new)

def printFunction(lista: list, index):
    clear_screen()
    #ispis korsinika
    if index == 1:
        t = PrettyTable(["ID KORISNIKA", "IME I PREZIME KORISNIKA", "OIB KORISNIKA", "DATUM REGISTRACIJE"], padding_width = 4, hrules=ALL)
        print(f"Popis sadrži {len(lista)} korisnika: ")
        for user in lista:
            t.add_row([user[USER_ID], user[USER_FIRST_NAME] + " " + user[USER_LAST_NAME], user[USER_PIN], dt.fromtimestamp(user[USER_CREATED]).strftime("%d.%m.%Y. - %H:%M:%S")])
    #ispis filmova
    elif index == 2: 
        t = PrettyTable(["ID FILMA", "NAZIV FILMA", "REDATELJ", "GODINA", "POSUĐEN", "POSUDIO KORISNIK"], padding_width = 4, hrules=ALL)
        for movie in lista:
            var = None
            if movie[MOVIE_RENTED] == True:
                var = "\u2713"
            else:
                var = "\u2717"
            t.add_row([movie[MOVIE_ID], movie[MOVIE_NAME], movie[MOVIE_DIRECTOR], movie[MOVIE_YEAR], var, movie[MOVIE_USERID]])
    elif index == 3:
        print(f"Popis sadrži {len(lista)} stavaka povijesti: ") 
        t = PrettyTable(["ID KORISNIKA", "ID FILMA", "STATUS", "DATUM I VRIJEME STATUSA"], padding_width = 4, hrules=ALL)
        for item in lista:
            t.add_row([item[HISTORY_USERID], item[HISTORY_MOVIEID], item[HISTORY_ACTION], dt.fromtimestamp(item[HISTORY_DATE]).strftime("%d.%m.%Y. - %H:%M:%S")])

    print(f"{t}\n")

def podizbornik(podizbornikispisa):
    flag = True
    clear_screen()
    while flag:
        opcija = unosOpcije(podizbornikispisa)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            printFunction(videoteka["listaKorisnika"], 1)
        elif opcija == 2:
            printFunction(videoteka["listaFilmova"], 2)
        elif opcija == 3:
            printFunction(videoteka["listaPovijesti"], 3)

if __name__ == "__main__":
    flag = True
    clear_screen()
    while flag:
        opcija = unosOpcije(glavniIzbornik)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            inputMovies(videoteka["listaFilmova"])
        elif opcija == 2:
            inputUser(videoteka["listaKorisnika"])
        elif opcija == 3:
            rentMovie(videoteka["listaKorisnika"],videoteka["listaFilmova"], videoteka["listaPovijesti"])
        elif opcija == 4:
            returnMovie(videoteka["listaKorisnika"],videoteka["listaFilmova"], videoteka["listaPovijesti"])
        elif opcija == 5:
            podizbornik(podizbornikispisa)