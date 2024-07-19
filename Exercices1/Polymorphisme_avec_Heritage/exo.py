class Animal:
    def __init__(self, nom):
        self.nom = nom
        
class Chat(Animal):
    def __init__(self, nom):
        super().__init__(nom)
        
    def crier(self):
        print(f"{self.nom} dit : miaou")
        
class Chien(Animal):
    def __init__(self, nom):
        super().__init__(nom)
        
        
    def crier(self):
        print(f"{self.nom} dit : ouaf")
        
animaux = [
    Chat("Minou"),
    Chien("Rambo")
]

for animal in animaux:
    animal.crier()

