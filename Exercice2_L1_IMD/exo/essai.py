# Demander la taille du tableau
taille = int(input("Entrez le nombre de personnes: "))

# Initialiser une liste vide pour stocker les informations des personnes
personnes = []

# Saisir les informations de chaque personne
for i in range(taille):
    print(f"Entrez les informations pour la personne {i+1}:")
    prenom = input("Prénom: ")
    nom = input("Nom: ")
    note = float(input("Note: "))
    moyenne = float(input("Moyenne: "))
    classe = input("Classe: ")
    
    # Stocker les informations dans un dictionnaire
    personne = {
        "prenom": prenom,
        "nom": nom,
        "note": note,
        "moyenne": moyenne,
        "classe": classe
    }
    
    # Ajouter le dictionnaire à la liste
    personnes.append(personne)

# Afficher les résultats
print("\nInformations des personnes saisies:")
for personne in personnes:
    print(f"Prénom: {personne['prenom']}, Nom: {personne['nom']}, Note: {personne['note']}, Moyenne: {personne['moyenne']}, Classe: {personne['classe']}")
