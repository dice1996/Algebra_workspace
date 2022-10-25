from pomocne_funkcije import *

listaOcjena = [1, 2, 3, 4, 5]
najnizaOcjena = []
prosjekOcjena = None
predmeti = {}
suma = 0

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
            suma = predmeti[predmet]
        elif najnizaOcjena[1] > predmeti[predmet]:
            najnizaOcjena.clear()
            najnizaOcjena.append(predmet) 
            najnizaOcjena.append(predmeti[predmet])
            suma += predmeti[predmet]
    
    return najnizaOcjena, suma

BROJ_PREDMETA = brojPonavljanja("Unesi broj predmeta: ")
predmeti = unosPredmeta(predmeti, BROJ_PREDMETA, listaOcjena)
najnizaOcjena, suma = provjeraPredmeta(predmeti, suma)

prosjekOcjena = suma / BROJ_PREDMETA

print(f"Predmet s najnižom ocjenom {najnizaOcjena[1]} je {najnizaOcjena[0]}.")
print(f"Prosjek svih unesenih ocjena je {prosjekOcjena}")