taille = int(input("La taille du tableau : "))
print(f"Taille {taille}")
personnes = []

for i in range(taille):
    print(f"Veuillez saisir les infos de la personne {i+1}")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    note = float(input("Note : "))
    moyenne = float(input("Moyenne : "))
    classe = input("Classe : ")
    
    personne = {
        "nom": nom,
        "prenom": prenom,
        "note": note,
        "moyenne": moyenne,
        "classe": classe
    }
    personnes.append(personne)
    print("= " * 25)
    
print("La liste des informations")
for personne in personnes:
    print(f"NOM : {personne['nom']}; PRENOM : {personne['prenom']}; NOTE : {personne['note']}; MOYENNE : {personne['moyenne']}; CLASSE : {personne['classe']}")