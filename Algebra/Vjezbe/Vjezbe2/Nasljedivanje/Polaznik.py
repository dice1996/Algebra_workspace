from Osoba import Osoba

class Polaznik(Osoba):
    def __init__(self, id, ime, prezime):
        super().__init__(id, ime, prezime)
        self.id_polaznika = None