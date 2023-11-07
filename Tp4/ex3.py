from abc import ABC , abstractmethod
class Employe(ABC):
    def __init__(self , nom , prenom):
        self.nom = nom 
        self.prenom = prenom
    def getNom(self):
        return self.nom
    def getPrenom(self):
        return self.prenom
    def setNom(self , nom):
        self.nom = nom
    def setPrenom(self , prenom):
        self.prenom = prenom
    def __str__(self):
        return f'Employe(Nom:{self.nom} Prenom:{self.prenom})'
    @abstractmethod
    def gains(self):
        pass
class TravailleurCommission(Employe):
    def __init__(self,nom , prenom , salaire , commission , quantite ):
        super().__init__(nom , prenom)
        self.salaire = salaire
        self.commission = commission
        self.quantite = quantite
    def getSalaire(self):
        return self.salaire
    def setSalaire(self, salaire):
        self.salaire = salaire
    def getCommission(self):
        return self.commission
    def setCommission(self, commission):
        self.commission = commission
    def getQuantite(self):
        return self.quantite
    def setQuantite(self, quantite):
        self.quantite = quantite
    def gains(self):
        return self.salaire + self.commission + self.quantite
    def __str__(self):
        return f'Employe(Nom:{self.nom},Prenom:{self.prenom} (Travailleur à la commission) - Salaire: {self.salaire}, Commission : {self.commission}, Quantité: {self.quantite})'
class TravailleurHoraire(Employe):
    def __init__(self, nom, prenom, retribution, heures):
        super().__init__(nom, prenom)
        self.retribution = retribution
        self.heures = heures
    def get_retribution(self):
        return self.retribution
    def set_retribution(self, retribution):
        self.retribution = retribution
    def get_heures(self):
        return self.heures
    def set_heures(self, heures):
        self.heures = heures
    def gains(self):
        return self.retribution * self.heures
    def __str__(self):
        return f'Employe(Nom:{self.nom} Prenom:{self.prenom} (Travailleur horaire) - Rémunération horaire : {self.retribution}, Heures: {self.heures})'
employes = [
    TravailleurCommission("Abdeladim", "Khadrouf", 2000, 10, 100),
    TravailleurHoraire("zakaria", "hadraf", 15, 160)
]
for employe in employes:
    print(employe)
    print(f'gains:{employe.gains()}\n')