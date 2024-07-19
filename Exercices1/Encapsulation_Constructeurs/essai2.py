class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
        
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_age(self):
        return self.__age
    
    def set_nom(self, nom):
        self.__nom = nom
        
    def set_prenom(self, prenom):
        self.__prenom = prenom
        
    def set_age(self, age):
        self.__age = age
        
nom = input("Veuillez saisir votre nom : ")
prenom = input("Veuillez saisir votre prénom : ")
age = input("Veuillez saisir votre age : ")

personne = Personne(nom, prenom, age)

print("Nom : ", personne.get_nom())
print("Prénom : ", personne.get_prenom())
print("Age : ", personne.get_age())
        

print(f"Bonjour {personne.get_prenom()} {personne.get_nom()}  vous avez {personne.get_age()} ans")

prenomModif = input("Veuillez tapez votre prenom pour le modifier : ")

personne.set_prenom(prenomModif)

print(f"Bonjour {personne.get_prenom()} {personne.get_nom()}  vous avez {personne.get_age()} ans")

