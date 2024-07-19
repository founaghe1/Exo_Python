solde = 5000

def afficher_menu_principal():
    print("Bienvenue dans votre portefeuille Orange Money.")
    print("Pour commencer; Tapez #144#")

def afficher_menu_options():
    print("Veuillez faire un choix : ")
    print("1. Solde de mon compte.")
    print("2. Transfert d’argent.")
    print("3. Paiement de facture.")
    print("4. Achats de crédit.")
    print("5. Quitter.")

def afficher_sous_menu_transfert():
    print("1. Entrez le numéro du destinataire : ")
    print("2. Quitter")

def afficher_sous_menu_facture():
    print("Pour le paiement de vos factures, veuillez choisir:")
    print("1. Liquide (saisir le montant en int)")
    print("2. Chèque (saisir le montant en String)")
    print("3. Quitter")

def effectuer_transfert(solde):
    afficher_sous_menu_transfert()
    choix = int(input("Faites votre choix : "))
    
    if choix == 1:
        destinataire = input("Saisissez ici le numéro du destinataire : ")
        montant = int(input("Entrez le montant à transférer : "))
        if montant > solde:
            print("Vous n'avez pas assez d'argent sur votre compte.")
        else:
            solde -= montant
            print(f"Le transfert de {montant} à {destinataire} a été effectué avec succès.")
            print(f"Votre nouveau solde est de {solde} FCFA")
    elif choix == 2:
        print("Merci d'avoir utilisé le portefeuille Orange Money.")
        print("A la prochaine!")
    return solde

def payer_facture(solde):
    afficher_sous_menu_facture()
    choix = int(input("Faites votre choix : "))
    
    if choix == 1:
        montant = int(input("Entrez le montant à payer : "))
        if montant > solde:
            print("Vous n'avez pas assez d'argent sur votre compte.")
        else:
            solde -= montant
            print("Le paiement en LIQUIDE a été effectué avec succès.")
            print(f"Votre nouveau solde est de {solde} FCFA")
    elif choix == 2:
        montant = input("Entrez le montant à payer : ")
        if int(montant) > solde:
            print("Vous n'avez pas assez d'argent sur votre compte.")
        else:
            solde -= int(montant)
            print("Le paiement par CHEQUE a été effectué avec succès.")
            print(f"Votre nouveau solde est de {solde} FCFA")
    elif choix == 3:
        print("Merci d'avoir utilisé le portefeuille Orange Money.") 
        print("A la prochaine!")
    return solde

def acheter_credit(solde):
    numero = input("Entrer le numéro de téléphone : ")
    montant = int(input("Saisir le montant : "))
    if montant > solde:
        print("Vous n'avez pas assez d'argent sur votre compte.")
    else:
        solde -= montant
        print("Le crédit a été acheté avec succès.")
        print(f"Votre nouveau solde est de {solde} FCFA")
    return solde

while True:
    afficher_menu_principal()
    code = input("")
    
    if code == "#144#":
        while True:
            afficher_menu_options()
            choix = int(input("Faites votre choix : "))
            print("=" * 35)
            
            if choix == 1:
                print(f"Votre solde est de {solde} FCFA")
                print("=" * 35)
            elif choix == 2:
                solde = effectuer_transfert(solde)
            elif choix == 3:
                solde = payer_facture(solde)
            elif choix == 4:
                solde = acheter_credit(solde)
            elif choix == 5:
                print("Fermeture du programme.")
                exit()
            else:
                print("Choix incorrect. Veuillez réessayer.")
            print("=" * 35)
    else:     
        print("Code incorrect. Veuillez réessayer.")
