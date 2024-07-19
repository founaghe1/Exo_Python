from datetime import datetime

class CompteBancaire:
    def __init__(self, solde=0):
        self.solde = solde
    
    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"Déposé: {montant} | Nouveau solde: {self.solde} | Date: {datetime.now()}")
        else:
            print("Le montant doit être positif pour déposer.")
    
    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                print(f"Retiré: {montant} | Nouveau solde: {self.solde} | Date: {datetime.now()}")
            else:
                print("Fonds insuffisants pour ce retrait.")
        else:
            print("Le montant doit être positif pour retirer.")
    
    def consulter_solde(self):
        print(f"Solde actuel: {self.solde} | Date: {datetime.now()}")
        return self.solde

# Création d'une instance de CompteBancaire
compte = CompteBancaire()

compte.consulter_solde()
compte.deposer(1000)
compte.consulter_solde()
compte.retirer(200)
compte.consulter_solde()
compte.retirer(1000)  
compte.deposer(-50)   
compte.retirer(-50)   
