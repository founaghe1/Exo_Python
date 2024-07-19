class Calculatrice:
    def addition(self, a, b):
        return a + b

    def soustraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("La division par zéro n'est pas autorisée.")
        return a / b


calc = Calculatrice()

# Addition
print(calc.addition(5, 3))           
print(calc.addition(5.0, 3.0))      
print(calc.addition(5, 3.0))         

# Soustraction
print(calc.soustraction(5, 3))       
print(calc.soustraction(5.0, 3.0))   
print(calc.soustraction(5, 3.0))     

# Multiplication
print(calc.multiplication(5, 3))     
print(calc.multiplication(5.0, 3.0)) 
print(calc.multiplication(5, 3.0))   

# Division
print(calc.division(6, 3))           
print(calc.division(6.0, 3.0))     
print(calc.division(6, 3.0))   
