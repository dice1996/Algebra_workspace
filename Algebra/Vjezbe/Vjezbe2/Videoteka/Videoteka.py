

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
    
    def ispisFilmova(self):
        for f in self.listaFilmova:
            print(f)

    def dohvatiFilmPoIdu(self, idFilma):
        for f in self.listaFilmova:
            if f.id == idFilma:
                return f
        return None
        
    def dohvatiKorisnikaPoIdu(self, idFilma):
        for k in self.listaKorisnika:
            if k.id == idFilma:
                return k
        return None


