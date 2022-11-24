from Osoba import Osoba

class Predavac(Osoba):
    def __init__(self, id, ime, prezime):
        super().__init__(id, ime, prezime)
        self.id_predavaca = None

predavac = Predavac(1, "Dino", "Cerjak")
predavac.unesiOib(55255525)

print(predavac)

