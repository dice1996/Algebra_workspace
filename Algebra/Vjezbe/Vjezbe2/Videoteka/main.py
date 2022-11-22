from Videoteka import Videoteka
from Film import Film
from Korisnik import Korisnik
from Povijest import Povijest



if __name__ == "__main__":

    videoteka = Videoteka()
    film = Film("001", "naziv", 2022)
    film2 = Film("002", "na121ziv", 2001)
    videoteka.dodajFilm(film)
    videoteka.dodajFilm(film2)

    povijest = Povijest(2, "001", "POVRAT")
    videoteka.dodajPovijest(povijest)
    povijest = Povijest(3, "002", "NAJAM")
    videoteka.dodajPovijest(povijest)

    print(videoteka.listaFilmova)
    videoteka.ispisPovijesti()


    korisnik = Korisnik(1, "Dino", "Cerjak")
    videoteka.dodajKorisnika(korisnik)
    korisnik = Korisnik(3, "Ante", "Cerjak")
    videoteka.dodajKorisnika(korisnik)
    videoteka.ispisKorisnika()
