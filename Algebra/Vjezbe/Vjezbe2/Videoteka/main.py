from VideotekaService import VideotekaService 
from Utils import Utils
from Povijest import PovijestAkcija

glavniIzbornik = {
    1: "Upis filma",
    2: "Upis korisnika",
    3: "Posudi film",
    4: "Vrati film",
    5: "Ispis videoteke",
    0: "Izlaz iz aplikacije"
}

if __name__ == "__main__":
    service = VideotekaService()
    idFilma = 1
    idKorisnika = 1
    while True:        
        opcija = Utils.unosOpcije(glavniIzbornik)
        if opcija == 0:
            break
        elif opcija == 1:
            idFilma = service.dodajFilm(idFilma)
        elif opcija == 2:
            idKorisnika = service.dodajKorisnika(idKorisnika)
        elif opcija == 3:
            service.akcijaFilm(PovijestAkcija.posudi)
        elif opcija == 4:
            service.akcijaFilm(PovijestAkcija.vrati.value)
        elif opcija == 5:
            service.ispisi()