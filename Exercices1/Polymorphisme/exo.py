from abc import ABC, abstractmethod
import math

# Définition de la classe abstraite Forme
class Forme(ABC):
    
    @abstractmethod
    def calculerAire(self):
        pass

    def afficherType(self):
        print(f"Ceci est une forme de type {self.__class__.__name__}")

# Définition de la classe Cercle qui hérite de Forme
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculerAire(self):
        return math.pi * (self.rayon ** 2)

# Définition de la classe Rectangle qui hérite de Forme
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
       

    def calculerAire(self):
        return self.longueur * self.largeur

# Utilisation du polymorphisme pour calculer l'aire de différentes formes
formes = [
    Cercle(5),
    Rectangle(6, 4)
]

for forme in formes:
    forme.afficherType()
    print(f"L'aire est: {forme.calculerAire()}")

