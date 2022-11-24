from Videoteka import Videoteka
from Utils import Utils as ut
from Film import Film
from Korisnik import Korisnik
from Povijest import Povijest, PovijestAkcija


class VideotekaService:

    def __init__(self):
        self.videoteka = Videoteka()

    def dodajFilm(self, idFilma):
        film: Film = Film(idFilma, input("Naziv filma: "), ut.unesiCijeliBroj("Unesi godinu filma: "))

        self.videoteka.dodajFilm(film)

        ut.clear_screen()
        return idFilma + 1

    def ispisVideoteke(self):
        print("-----------------FILMOVI-----------------")
        self.videoteka.ispisFilmova()
        print("----------------KORISNICI----------------")
        self.videoteka.ispisKorisnika()

    def dodajKorisnika(self, idKorisnika):
        korisnik: Korisnik = Korisnik(idKorisnika, input("Unesi ime korisnika: "), input("Unesi prezime korisnika: "))

        self.videoteka.dodajKorisnika(korisnik)
        ut.clear_screen()
        return idKorisnika + 1


    def akcijaFilm(self, akcija: PovijestAkcija):
        film = self.videoteka.dohvatiFilmPoIdu(ut.unesiCijeliBroj("Unesi ID filma: "))
        if film is not None:
            korisnik: Korisnik = self.videoteka.dohvatiKorisnikaPoIdu(ut.unesiCijeliBroj("Unesi ID korinika: "))
            if korisnik is not None:
                if akcija == PovijestAkcija().posudi:
                    pass
                else:
                    pass
            else:
                print("Korisnik s trazenim ID-jem ne postoji")
        else:
            print("Film s traženim ID-jem ne postoji!")

        # if akcija == PovijestAkcija().posudi:
        #     pass
        # elif akcija == PovijestAkcija().vrati:
        #     pass