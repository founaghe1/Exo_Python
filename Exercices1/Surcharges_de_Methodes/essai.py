class Calculatrice:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def addition(self):
        return self.a + self.b
    
    def soustraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        if self.b == 0:
            raise ValueError ("La division par zéro n'est pas autorisée.")
        return self.a / self.b
    
while True:
    try:
        a = int(input("Entrez un nombre : "))
        b = int(input("Entrez un nombre : "))
        
        calculatrice = Calculatrice(a, b)
        
        print("La somme est : ", calculatrice.addition())
        print("La soustraction est : ", calculatrice.soustraction())
        print("La multiplication est : ", calculatrice.multiplication())
        print("La division est : ", calculatrice.division())
        break
    except ValueError:
        print("Veuillez entrer un nombre entier")
        
    