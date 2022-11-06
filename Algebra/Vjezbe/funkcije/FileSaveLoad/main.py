import pickle as p
import os

l = []

#ODNOSI SE NA MOJ SETUP, MORAŠ POGLEDATI KOJI JE APSOLUTNI PUT NA TVOM RAČUNALU
fname = "file.p" 

def dodajFilm(l: list):
    k = dict()
    print("- - upis podataka novog filma - -")
    k["NASLOV"] = input("Naslov: ")
    k["ZANR"] = input("Žanr: ")
    k["GOD"] = input("Godina: ")
    k["DUR"] = input("Trajanje: ")
    k["RESTR"] = float(input("Dobno ograničenje: "))
    k["CIJENA"] = float(input("Cijena po danu: "))
    k["ZARADA"] = float()
    l.append(k)
    save_load(fname, l, 0) #index 0 odabire funkciju save, bez indeksa ide funkcija load

def save_load(fname, lista: list,  index = None):

    if index == 0: #FUNKCIJA SAVE
        p.dump(lista, open( fname, "wb" ))
    else: #FUNKCIJA LOAD
        if os.path.getsize(fname) > 0: #PROVJERA POSTOJE LI VEĆ ZAPISI U FILEU
            return p.load( open( fname, "rb" ) )
        else:
            return []

if __name__ == "__main__":
    
    l = save_load(fname, l)
    print(l)
    #dodajFilm(l)
    #dodajFilm(l)
    #print(l)

