from datetime import datetime as dt

class Povijest():
    def __init__(self, korisnikID, filmID, akcija):
        self.korisnikID = korisnikID
        self.filmID = filmID
        self.akcija = akcija
        self.datum = int(dt.now().timestamp())

    def __repr__(self):

        model = {
            "korisnikID": self.korisnikID,
            "filmID": self.filmID,
            "akcija": self.akcija,
            "datum": dt.fromtimestamp(self.datum).strftime("%d. %m. %Y")
        }

        return str(model)