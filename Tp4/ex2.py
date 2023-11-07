class Batiment:
    def __init__(self, adr):
        self.adr = adr
    def getAdr(self):
        return self.adr
    def setAdr(self,adr):
        self.adr = adr
    def __str__(self):
        return f'Adresse du bâtiment : {self.adr}'
class Maison(Batiment):
    def __init__(self , nbPieces , adr):
        super().__init__(adr)
        self.nbPieces = nbPieces
    def getNbPieces(self):
        return self.nbPieces

    def setNbPieces(self, nbPieces):
        self.nbPieces = nbPieces

    def __str__(self):
        return f'Adresse de la maison : {self.adr}, Nombre de pièces : {self.nbPieces}'
class Immeuble(Batiment):
    def __init__(self , nbAppart , adr):
        super().__init__(adr)
        self.nbAppart = nbAppart
    def getNbAppart(self):
        return self.nbAppart

    def setNbAppart(self, nbAppart):
        self.nbAppart = nbAppart

    def __str__(self):
        return f'Adresse de l\'immeuble : {self.adr}, Nombre d\'appartements : {self.nbAppart}'
print(Batiment("iftikhar tabriquet sale"))
print(Maison(3,"26 iftikhar tabriquet sale"))
print(Immeuble(30,"iftikhar tabriquet sale"))