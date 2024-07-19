from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer():
        pass
    
class Voiture(Vehicule):
    def deplacer(self):
        print("Je suis une voiture et je roule")
        
class Avion(Vehicule):
    def deplacer(self):
        print("Je suis un avion et je vole")
        
class Bateau(Vehicule):
    def deplacer(self):
        print("Je suis un bateau et je navigue")
        

def faireDeplacer(self):
    self.deplacer()
    
v = Voiture()
a = Avion()
b = Bateau()

engins = [
    v, a, b
]

for engin in engins:
    engin.deplacer()