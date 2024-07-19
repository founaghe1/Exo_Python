class Animal:
    def __init__(self, nom, cri):
        self.nom = nom
        self.cri = cri
        
    def __str__(self):
        article = "Le"
        if self.nom[0].lower() in "eoiua":
            article = "L'"
        elif self.nom[-1] == "e":
            article = "La"
        
        return f"{article} {self.nom} : {self.cri}"
    
class Chat(Animal):
    def __init__(self):
        super().__init__("Chat", "Miaou")
        
class Oiseau(Animal):
    def __init__(self):
        super().__init__("Oiseau", "Pou")
        
chat = Chat()
oiseau = Oiseau()

print(chat)
print(oiseau)