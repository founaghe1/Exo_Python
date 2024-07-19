class Voiture():
    def __init__(self, marque, couleur,  prix):
        self.__marque = marque
        self.__couleur = couleur
        self.__prix = prix
        
    def get_marque(self):
        return self.__marque
    def get_couleur(self):
        return self.__couleur
    def get_prix(self):
        return self.__prix
    
    def set_marque(self, marque):
        self.__marque = marque
    def set_couleur(self, couleur):
        self.__couleur = couleur
    def set_prix(self, prix):
        self.__prix = prix
        
    def infos(self):
        return f"Ma voiture est une {self.__marque}, sa couleur est {self.__couleur} et elle m'a couté {self.__prix}"
    
voiture = Voiture("Peugeo", "Noire", 2500)
print(voiture.infos())

voiture.set_prix(2700)
print(voiture.infos())