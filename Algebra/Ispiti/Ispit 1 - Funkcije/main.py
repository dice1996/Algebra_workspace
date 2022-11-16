"""Tekst zadatka"""

import time
from datetime import datetime as dt
from prettytable import PrettyTable, ALL
import os

# definiranje korištenih varijabli , lista, dictova,...
glavniIzbornik = {
    1: "Test",
    0: "Kraj programa"
}

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



# if name is main
if __name__ == "__main__":
    flag = True
    clear_screen()
    while flag:
        opcija = unosOpcije(glavniIzbornik)
        if opcija == 0:
            flag = False
        elif opcija == 1:
            pass
        elif opcija == 2:
            pass
        elif opcija == 3:
            pass
        elif opcija == 4:
            pass
        elif opcija == 5:
            pass