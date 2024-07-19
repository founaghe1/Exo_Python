# Definition de la classe Personne
class Personne():
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        
    # Les getter
    def get_nom(self):
        return self.__nom
    def get_age(self):
        return self.__age
    def get_ville(self):
        return self.__ville
    
    # Les setter
    def set_nom(self, nom):
        self.__nom = nom
    def set_age(self, age):
        self.__age = age
    def set_ville(self, ville):
        self.__ville = ville
        
    def afficher_infos(self):
        return f"Bonjour, mon nom est {self.get_nom()}, j'ai {self.get_age()} ans et j'habite à {self.get_ville()}."
        
personne = Personne("Mohamed", 25, "Dakar")

print(f"Bonjour mon nom est {personne.get_nom()}, j'ai {personne.get_age()} et j'habite à {personne.get_ville()}")
print(personne.afficher_infos())

# Modification des infos
personne.set_ville("Diourbel")
# print(f"Bonjour mon nom est {personne.get_nom()}, j'ai {personne.get_age()} et j'habite à {personne.get_ville()}")
print(personne.afficher_infos())