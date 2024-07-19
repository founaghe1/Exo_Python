class Article:
    def __init__(self, nom, quantite, prix_unitaire, designation):
        self.nom = nom
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire
        self.prix_total = prix_unitaire * quantite
        self.designation = designation
        
    def afficheDetail(self):
        print("Nom: ", self.nom)
        print("Quantite: ", self.quantite)
        print("Prix unitaire: ", self.prix_unitaire)
        print("Prix total: ", self.prix_total)
        print("designation: ", self.designation)
        
# article1 = Article("Drap", 5, 10,  "drap blanc")
# article1.afficheDetail()

while True:
    print("1. Ajouter un article")
    print("2. Afficher les articles")
    print("3. Quitter")
    print("=" * 15)
    choix = int(input("Choix: "))
    if choix == 1:
        nom = input("Nom: ")
        quantite = int(input("Quantite: "))
        prix_unitaire = int(input("Prix unitaire: "))
        designation = input("designation: ")
        article = Article(nom, quantite, prix_unitaire, designation)
        # article1.afficheDetail()
    elif choix == 2:
        article.afficheDetail()
        print("=" * 15)
    elif choix == 3:
        break
    