class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x = x
    def setY(self,y):
        self.y = y
    def __str__(self):
        return f'Point({self.x},{self.y})'
class Rectangle(Point):
    def __init__(self , longueur , largeur , x , y):
        self.longueur = longueur
        self.largeur = largeur
        Point.__init__(self,x,y)
    def getLargeur(self):
        return self.largeur
    def getLongueur(self):
        return self.longueur
    def setLargeur(self,largeur):
        self.largeur = largeur
    def setLongueur(self,longueur):
        self.longueur = longueur
    def aire(self):
        return self.longueur * self.largeur
    def __str__(self):
        return f'Rectangle({self.x}, {self.y}, Longueur: {self.longueur}, Largeur: {self.largeur}, Aire: {self.aire()})'
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, x, y , hauteur):
        super().__init__(longueur, largeur, x, y)
        self.hauteur = hauteur
    def getHauteur(self):
        return self.hauteur
    def setHauteur(self , hauteur):
        self.hauteur = hauteur
    def aire(self):
        lateral = 2 * (self.longueur * self.hauteur + self.largeur * self.hauteur)
        return 2 * super().aire() + lateral
    def volume(self):
        return super().aire() * self.hauteur
    def __str__(self):
        return f'Parallelepipede({self.x}, {self.y}, Longueur: {self.longueur}, Largeur: {self.largeur}, Hauteur: {self.hauteur}, Aire: {self.aire()}, Volume: {self.volume()})'
print(Point(1, 2))
print(Rectangle(3, 4, 5, 6))
print(Parallelepipede(7, 8, 9, 10, 11))   