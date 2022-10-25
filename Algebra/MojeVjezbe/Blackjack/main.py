############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from random import randint
import math
from os import system

karte = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dijeli_karte(listaKarata: list, deck = []):
    if deck == []:
        for i in range(2):
            index = randint(0, 12)
            deck.append(listaKarata[index])
    else:
        deck.append(listaKarata[randint(0, 12)])
    return deck

def izracun_rezultata(deck: list): 
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)

def usporedbaRezultata(rez_igrac, rez_house):
    if rez_igrac == rez_house:
        return "Izjednaceno 🙃"
    elif rez_house == 0:
        return "Gubitak, house ima Blackjack 😱"
    elif rez_igrac == 0:
        return "Pobjeda! 😎"
    elif rez_igrac > 21:
        return "Rezultat iznad 21. Izgubio si! 😭"
    elif rez_house > 21:
        return "House iznad 21. Ti si pobijedio! 😁"
    elif rez_igrac > rez_house:
        return "Pobjeda 😃"
    else:
        return "Gubitak 😤"

def igra():
    print(logo)
    igrac = []
    house = []
    rez_igrac = int()
    rez_house = int()
    igra_gotova = False
    ponovnoVuci = str()

    dijeli_karte(karte, igrac)
    dijeli_karte(karte, house)

    while not igra_gotova:        
        rez_igrac = izracun_rezultata(igrac)
        rez_house = izracun_rezultata(house)
        
        if rez_igrac == 0 or rez_house == 0 or rez_igrac > 21:
            print(f"Tvoje karte su {igrac} dok house ima karte {house}")
            igra_gotova = True
        elif rez_igrac != 0 or rez_house != 0:
            print(f"Tvoje karte su {igrac}, tvoj rezultat je {rez_igrac}.")
            print(f"House ima karte {house}, rezultat je {rez_house}.")
        if not igra_gotova:    
            ponovnoVuci = input("Zelis li vuci novu kartu (y/n): ").lower()

            if ponovnoVuci == "y":
                dijeli_karte(karte, igrac)
                rez_igrac = izracun_rezultata(igrac)
            else:
                    igra_gotova = True
        
        while rez_house != 0 and rez_house < 17:
            dijeli_karte(karte, house)
            rez_house = izracun_rezultata(house)
        if rez_house != 0 or rez_igrac != 0:
            print(f"Tvoj konacni deck je {igrac}, konacni rezultat je {rez_igrac}.")
            print(f"House konacni deck je {house}, konacni rezultat je {rez_house}.")
        print(usporedbaRezultata(rez_igrac, rez_house))
        igra_gotova = True


#main app
while input("Zelis li igrati Blackjack (y/n): ") == "y":
  system("clear")
  igra()