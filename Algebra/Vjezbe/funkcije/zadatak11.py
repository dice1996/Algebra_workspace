from pomocne_funkcije import *

listaOcjena = [1, 2, 3, 4, 5]
najnizaOcjena = []
prosjekOcjena = None
predmeti = {}
suma = 0
BROJ_PREDMETA = brojPonavljanja("Unesi broj predmeta: ")
predmeti = unosPredmeta(predmeti, BROJ_PREDMETA, listaOcjena)
najnizaOcjena, suma = provjeraPredmeta(predmeti, suma)

prosjekOcjena = suma / predmeti.__len__()

print(f"Predmet s najnižom ocjenom {najnizaOcjena[1]} je {najnizaOcjena[0]}.")
print(f"Prosjek svih unesenih ocjena je {prosjekOcjena}")