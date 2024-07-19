def calculerFactorielle(n):
    
    return 1 if n == 0 else n * calculerFactorielle(n-1)


nombre = int(input("Entrez un nombre entier pour calculer sa factorielle : "))
resultat = calculerFactorielle(nombre)
print(f"La factorielle de {nombre} est {resultat}")
