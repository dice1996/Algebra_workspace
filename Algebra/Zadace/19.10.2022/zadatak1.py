counterPar = 0
counterNepar = 0

listaBrojeva = []

def unosBroja(listaBrojeva, brojPonavljanja):
    for i in range(brojPonavljanja):
        flag = 1
        while flag:
            try:
                unos = int(input(f"Unesi {i + 1}. cijeli broj: "))
                flag = 0
                listaBrojeva.append(unos)
            except:
                print("Uneseno nije broj! Pokušaj ponovno!")
    return listaBrojeva
def brojPonavljanja():
    flag = 1
    while flag:
        try:
            brojUnosa = int(input("Unesi koliko brojeva zelis upisati: "))
            if brojUnosa >= 0:
                flag = 0
            else:
                print("Broj ponavljanja ne moze biti negativan! Pokusaj ponovno!")
        except:
            print("Uneseno nije broj! Pokušaj ponovno!")
    return brojUnosa
def provjera(listaBrojeva: list):
    par = 0
    nepar = 0
    for item in listaBrojeva:
        if item%2 == 0:
            par += 1
        else:
            nepar += 1
    return par, nepar

brojUnosa = brojPonavljanja()
listaBrojeva = unosBroja(listaBrojeva, brojUnosa)
counterPar, counterNepar = provjera(listaBrojeva)
    
if listaBrojeva == []:
    print("Nista nije uneseno! Program zavrsava...")
else:
    print(f"Broj parnih brojeva je {counterPar}, a neparnih {counterNepar}.")