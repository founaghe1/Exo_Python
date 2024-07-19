# definition de la function
def estPalindrome(mot):
    """Vérifie si un mot est un palindrome"""
    # verification du mot 
    return mot == mot[::-1]

# normalisation du mot saisi
mots = input("Veuillez saisir un mot ou une phrase : ").lower().replace(" ", "")

print(f"Le mot '{mots}' est-il Palindrome : {estPalindrome(mots)}") 

