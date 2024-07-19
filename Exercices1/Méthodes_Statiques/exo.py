class MathUtil():
    # Création de la methode statique
    @staticmethod
    def calculerMoyenne(nombres):
        return sum(nombres) / len(nombres) if nombres else 0
    
# tabNombres = [10, 15, 9, 5, 18]
# moyenne = MathUtil.calculerMoyenne(tabNombres)
# print(f"La moyenne des nombres {tabNombres} est {moyenne}")


tabNombers = []
while True:
    nombre = input("Entrez un nombre ou (0 pour arreter) : ")
    try:
        nombre = int(nombre)
        if nombre == 0:
            break
        tabNombers.append(nombre)
        moyenne = MathUtil.calculerMoyenne(tabNombers)
        print(f"La moyenne des nombres {tabNombers} est {moyenne}")
    except ValueError:
        print("Vous devez entrer un nombre")
        
print(f"La moyenne finale des nombres {tabNombers} est {moyenne}")

    