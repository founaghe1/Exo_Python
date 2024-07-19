from abc import ABC, abstractmethod

class Vehicule(ABC):

    @abstractmethod
    def deplacer(self):
        pass
    
class Voiture(Vehicule):
    
    def deplacer(self):
        print("Je suis une voiture, je roule sur la route")
        
class Avion(Vehicule):
    
    def deplacer(self):
        print("Je suis un avion, je vole dans les airs")
        
class Bateau(Vehicule):
    
    def deplacer(self):
        print("Je suis un bateau, je navigue sur l'eau")
        
def faireDeplacer(self):
    self.deplacer()
        
        
voirture = Voiture()
avion = Avion()
bateau = Bateau()

vehicules = [
    voirture,
    avion,
    bateau
]

for vehicule in vehicules:
    vehicule.deplacer()
    

# faireDeplacer(avion)
        
