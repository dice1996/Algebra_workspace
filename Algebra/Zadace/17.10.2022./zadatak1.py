"""
Zadatak 11:
Napisati program gdje unosite 5 predmeta (predmet ima propertye: ime i ocjena). Nakon unosa ispisati ime predmeta s najnizom ocjenom i prosjek ocjena svih predmeta 
"""
listaOcjena = ["1", "2", "3", "4", "5"]
najnizaOcjena = []
prosjekOcjena = None
predmeti = {}
suma = 0
BROJ_PREDMETA = 5

for i in range(BROJ_PREDMETA):
    while True:
        ime = input("Unesi ime predmeta: ").upper()
        if ime not in predmeti.keys():
            while True:
                ocjena = input(f"Unesi ocjenu predmeta {ime}: ")
                if ocjena in listaOcjena:
                    predmeti[ime] = int(ocjena)
                    break
                else:
                    print("Nije unesena ispravna ocjena. Posukaj ponovno!")
            break    
        else:
            print("Ponovi unos jer je ovaj predmet već unesen!")

for predmet in predmeti:
    if najnizaOcjena == []:
        najnizaOcjena.append(predmet) 
        najnizaOcjena.append(predmeti[predmet])
    elif najnizaOcjena[1] > predmeti[predmet]:
        najnizaOcjena.clear()
        najnizaOcjena.append(predmet) 
        najnizaOcjena.append(predmeti[predmet])
    suma += predmeti[predmet]

prosjekOcjena = suma / predmeti.__len__()

print(f"Predmet s najnižom ocjenom {najnizaOcjena[1]} je {najnizaOcjena[0]}.")
print(f"Prosjek svih unesenih ocjena je {prosjekOcjena}")