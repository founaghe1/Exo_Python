class Animaux:
    def __init__(self, nom):
        self.nom = nom
        
class Chat(Animaux):
    def __init__(self, nom):
        super().__init__(nom)
        self.nom = nom
        
    def crier(self):
        print(f"{self.nom} dit : Miao")
        
class Oiseau(Animaux):
    def __init__(self, nom):
        super().__init__(nom)
        self.nom = nom
        
    def crier(self):
        print(f"{self.nom} dit : PioPio")
        
animaux = [
    Chat("Minou"),
    Oiseau("Poussin")
]

for animal in animaux:
    animal.crier()