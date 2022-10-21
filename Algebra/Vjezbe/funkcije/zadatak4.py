from pomocne_funkcije import *
counterPar = 0
counterNepar = 0

listaBrojeva = []

brojUnosa = brojPonavljanja("Unesi koliko brojeva zelis unijeti: ")
listaBrojeva = unosBroja(listaBrojeva, brojUnosa)
counterPar, counterNepar = countParNepar(listaBrojeva)
    
if listaBrojeva == []:
    print("Nista nije uneseno! Program zavrsava...")
else:
    print(f"Broj parnih brojeva je {counterPar}, a neparnih {counterNepar}.")