def menu_principal():
    print("Bienvenue sur le menu principal de notre calculatrice.\nPour continuer; veuillez faire un choix:")
    print("1. Faire la somme de deux valeurs")
    print("2. Faire la soustraction de deux valeurs")
    print("3. Faire le produit de deux valeurs")
    print("4. Faire la division de deux valeurs")
    print("5. Quitter")
    
def somme(a, b):
    return a + b
def soustraction(a, b):
    return a - b
def produit(a, b):
    return a * b
def division(a, b):
    if b <= 0:
        print("Erreur: division par un nombre inferieur ou egal à 0")
    else:
        return a / b

while True:
    menu_principal()
    choix = int(input("Votre choix: "))
    if choix == 1:
        a = int(input("Entrez la première valeur: "))
        b = int(input("Entrez la deuxième valeur: "))
        print(f"La somme de {a}, et {b}, est, {somme(a, b)}")
        print("= " * 25)
    elif choix == 2:
        a = int(input("Entrez la première valeur: "))
        b = int(input("Entrez la deuxième valeur: "))
        print(f"La soustraction de {a}, et {b}, est, {soustraction(a, b)}")
        print("= " * 25)
    elif choix == 3:
        a = int(input("Entrez la première valeur: "))
        b = int(input("Entrez la deuxième valeur: "))
        print(f"Le produit de {a}, et {b}, est, {produit(a, b)}")
        print("= " * 25)
    elif choix == 4:
        a = int(input("Entrez la première valeur: "))
        b = int(input("Entrez la deuxième valeur: "))
        print(f"La division de {a}, et {b}, est, {division(a, b):.2f}")
        print("= " * 25)
    elif choix == 5:
        print("Au revoir")
        break
    