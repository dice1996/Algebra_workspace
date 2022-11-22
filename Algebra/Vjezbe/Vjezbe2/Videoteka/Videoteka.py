

class Videoteka:
    def __init__(self):
        self.listaKorisnika = []
        self.listaFilmova = []
        self.listaPovijesti = []
    
    def dodajFilm(self, film):
        #u listu filmova dodaj film
        self.listaFilmova.append(film)
    
    def dodajKorisnika(self, korisnik):
        self.listaKorisnika.append(korisnik)

    def dodajPovijest(self, povijest):
        self.listaPovijesti.append(povijest)

    def ispisPovijesti(self):
        for p in self.listaPovijesti:
            print(p)

    def ispisKorisnika(self):
        for k in self.listaKorisnika:
            print(k)