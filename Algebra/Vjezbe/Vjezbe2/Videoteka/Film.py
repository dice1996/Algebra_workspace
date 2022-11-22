

class Film():
    def __init__(self, id, naziv, godina):
        self.id = id
        self.naziv = naziv
        self.godina = godina
    
    def __repr__(self):
        return str(self.__dict__)