taille = int(input("Veuillez saisir la taille du tableau : "))
print(f"Taille = {taille}")
personnes = []

for _ in range(taille):
    nom = input("Veuillez saisir le nom : ")
    prenom = input("Veuillez saisir le prénom : ")
    note = int(input("Veuillez saisir la note : "))
    moyenne = int(input("Veuillez saisir la moyenne : "))
    classe = input("Veuillez saisir la classe : ")
    
    personnes.append({"prenom": prenom, "nom": nom, "note": note, "moyenne": moyenne, "classe": classe})
    print("= " * 25)
print(personnes)