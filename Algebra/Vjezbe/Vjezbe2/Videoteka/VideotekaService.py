from Videoteka import Videoteka
from Film import Film
from Utils import Utils
from Korisnik import Korisnik
from Povijest import Povijest, PovijestAkcija

class VideotekaService:

    def __init__(self):
        self.videoteka = Videoteka()

    def dodajFilm(self, idFilma):
        film: Film = Film(
            idFilma,
            input("Naziv filma: "),
            Utils.unesiCijeliBroj("Godina filma: ")
        )
        self.videoteka.dodajFilm(film)
        return idFilma + 1


    def dodajKorisnika(self, idKorisnika):
        korisnik: Korisnik = Korisnik(
            idKorisnika,
            input("Ime korisnika: "),
            input("Prezime korisnika: ")
        )
        self.videoteka.dodajKorisnika(korisnik)
        return idKorisnika + 1


    def akcijaFilm(self, akcija: PovijestAkcija):
        film: Film = self.videoteka.dohvatiFilmPoIdu(Utils.unesiCijeliBroj("Unesite ID filma: "))
        if film is not None:
            korisnik: Korisnik = self.videoteka.dohvatiKorisnikaPoIdu(Utils.unesiCijeliBroj("Unesite ID korisnika: "))
            if korisnik is not None:
                match akcija:
                    case PovijestAkcija.posudi:
                        if not film.posuden:
                            film.posuden = True
                            film.idKorisnika = korisnik.id
                            povijest: Povijest = Povijest(korisnik.id, film.id, akcija.value)
                            self.videoteka.dodajPovijest(povijest)
                        else:
                            print("Film je vec posuden")
                    case PovijestAkcija.vrati:
                        if film.posuden:
                            if film.idKorisnika == korisnik.id:
                                film.posuden = False
                                film.idKorisnika = None
                                povijest: Povijest = Povijest(korisnik.id, film.id, akcija.value)
                                self.videoteka.dodajPovijest(povijest)
                            else:
                                print("Film nije posuden od navedenog korisnika.")
                        else:
                            print("Ovaj film nije posuden.")
                    case other:
                        print("Opcija ne postoji!")
            else:
                print("Korisnik s odabranim IDom ne postoji!")
        else:
            print("Film s odabranim IDom ne postoji!")


    def ispisi(self):
        print("-----------------Filmovi-----------------")
        self.videoteka.ispisFilmova()
        print("-----------------Korisnici-----------------")
        self.videoteka.ispisKorisnika()
        print("-----------------Povijest-----------------")
        self.videoteka.ispisPovijesti()

