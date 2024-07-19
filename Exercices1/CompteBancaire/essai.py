class CompteBancaire:
    def __init__(self, solde=0):
        self.solde = solde
        
    def deposer(self, montant):
        self.montant = montant
        
        if montant > 0:
            self.solde += montant
        else:
            print("Montant à deposer invalide")
            return "Montant à deposer invalide"
        return self.solde
    def retirer(self, montant):
        self.montant = montant
        if montant > 0:
            if montant <= self.solde:
                self.solde -= montant
            else:
                print("Solde insuffisant")
                return "Solde insuffisant"
        else:
            print("Montant à retirer invalide")
            return "Montant à retirer invalide"
    def consulterSolde(self):
        return self.solde
    
compte = CompteBancaire()

compte.deposer(1000)
print(compte.consulterSolde())
compte.retirer(5500)
print(compte.consulterSolde())