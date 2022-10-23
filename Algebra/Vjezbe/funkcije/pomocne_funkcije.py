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

def unosBroja(brojPonavljanja, listaBrojeva = None):
    if listaBrojeva is None:
        lista = []
    else:
        lista = listaBrojeva     
    for i in range(brojPonavljanja):
        lista.append(unesiCijeliBroj(index = i+1))
    if listaBrojeva is None:
        return lista
    

def brojPonavljanja(text):
    while True:
        brojUnosa = unesiCijeliBroj(text)
        if brojUnosa >= 0:
            break
        else:
            print("Broj ne moze biti negativan! Pokusaj ponovno!")
    return brojUnosa

def jeParan(broj):
    return broj%2 == 0

def countParNepar(listaBrojeva: list):
    par = 0
    nepar = 0
    for item in listaBrojeva:
        if jeParan(item):
            par += 1
        else:
            nepar += 1
    return par, nepar

def unosPredmeta(predmeti : dict, BROJ_PREDMETA, listaOcjena):
    for i in range(BROJ_PREDMETA):
        while True:
            ime = input("Unesi ime predmeta: ").upper()
            if ime not in predmeti.keys():
                ocjena = unesiCijeliBroj(f"Unesi ocjenu za predmet {ime}: ")
                if ocjena in listaOcjena:
                    predmeti[ime] = int(ocjena)  
                    break              
                else:
                    print("Nije unesena ispravna ocjena. Pokusaj ponovno!")
            else:
                print("Ponovi unos jer je ovaj predmet već unesen!")
    return predmeti

def provjeraPredmeta (predmeti: dict, suma):
    najnizaOcjena = []
    for predmet in predmeti:
        if najnizaOcjena == []:
            najnizaOcjena.append(predmet) 
            najnizaOcjena.append(predmeti[predmet])
        elif najnizaOcjena[1] > predmeti[predmet]:
            najnizaOcjena.clear()
            najnizaOcjena.append(predmet) 
            najnizaOcjena.append(predmeti[predmet])
    suma += predmeti[predmet]
    return najnizaOcjena, suma