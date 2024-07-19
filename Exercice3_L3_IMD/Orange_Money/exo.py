solde = 5000


while True:
    print("Bienvenue dans votre portefeuille Orange Money.")
    print("Pour commencer; Tapez #144#")
    code = input("")
    if code == "#144#":
        while True:
            print("1. Solde de mon compte.")
            print("2. Transfert d’argent.")
            print("3. Paiement de facture.")
            print("4. Achats de crédit.")
            print("5. Quitter.")
            
            choix = int(input("Faites votre choix : "))
            print("= " * 35)
            if choix == 1:
                print("Votre solde est de", solde, "FCFA")
                print("= " * 35)
                break
            elif choix == 2:
                print("Pour effectuer un transfert d’argent, veuillez")
                print("1. Entrer le numéro du destinataire : ")
                print("2. Quitter")
                choix = int(input("Faites votre choix : "))
                
                if choix == 1:
                    print("Saisissez ici le numéro du destinataire : ")
                    destinataire = input("")
                    print("Entrez le montant à transférer : ")
                    montant = int(input(""))
                    print("= " * 35)
                    if montant > solde:
                        print("Vous n'avez pas assez d'argent sur votre compte.")
                        print("= " * 35)
                    else:
                        solde = solde - montant
                        print("Le transfert a été effectué avec succès.")
                        print(f"Votre nouveau solde est de {solde} FCFA")
                        print("Merci d'avoir utilisé le portefeuille Orange Money.")
                        print("= " * 35)
                        break
                elif choix == 2:
                    print("Merci d'avoir utilisé le portefeuille Orange Money.")
                    print("A la prochaine!")
                    print("= " * 35)
                    break
                
            elif choix == 3:
                print("Pour le paiement de vos factures, veuillez choisir:")
                print("1. Liquide (saisir le montant en int)")
                print("2. Chèque (saisir le montant en String)")
                print("3. Quitter")
                choix = int(input("Faites votre choix : "))
                print("= " * 35)
                if choix == 1:
                    print("Entrez le montant à payer : ")
                    montant = int(input(""))
                    print("= " * 35)
                    if montant > solde:
                        print("Vous n'avez pas assez d'argent sur votre compte.")
                        print("= " * 35)
                    else:
                        solde = solde - montant
                        print("Le paiement en LIQUIDE a été effectué avec succès.")
                        print(f"Votre nouveau solde est de {solde} FCFA")
                        print("Merci d'avoir utilisé le portefeuille Orange Money.")
                        print("= " * 35)
                elif choix == 2:
                    print("Entrez le montant à payer : ")
                    montant = input("")
                    print("= " * 35)
                    if int(montant) > solde:
                        print("Vous n'avez pas assez d'argent sur votre compte.")
                        print("= " * 35)
                    else:
                        solde = solde - int(montant)
                        print("Le paiement par CHEQUE a été effectué avec succès.")
                        print(f"Votre nouveau solde est de {solde} FCFA")
                        print("Merci d'avoir utilisé le portefeuille Orange Money.")
                        print("= " * 35)
                elif choix == 3:
                    print("Merci d'avoir utilisé le portefeuille Orange Money.") 
                    print("A la prochaine!")
                    print("= " * 35)
                    break
                
            elif choix == 4:
                print("Pour acheter de credit, veuillez: ")
                numero = input("Entrer le numéro de telephone : ")
                montant = int(input("Saisir le montant : "))
                if montant > solde:
                    print("Vous n'avez pas assez d'argent sur votre compte.")
                    print("= " * 35)
                else:
                    solde = solde - montant
                    print("Le crédit a été acheté avec succès.")
                    print(f"Votre nouveau solde est de {solde} FCFA")
                    print("Merci d'avoir utilisé le portefeuille Orange Money.")
                    print("= " * 35)
            elif choix == 5:
                print("Fermeture du programme.")
                break
                        
    else:     
        print("Code incorrect. Veuillez réessayer.")
        