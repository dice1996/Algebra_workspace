

class Osoba():
    def __init__(self, id, ime, prezime):
        self.id = id
        self.ime = ime
        self.prezime = prezime
        self.oib = None

    def unesiOib(self, oib):
        self.oib = oib

    def __repr__(self):
        return str(self.__dict__)