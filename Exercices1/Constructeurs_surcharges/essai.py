class Article:
    def __init__(self, nom, prix, quantite) :
        self.nom = nom
        self.prix = prix
        self.prixTotal = prix * quantite
        self.quantite = quantite
        
    def afficheArticle(self):
        print(f"Nom : {self.nom};\nPrix : {self.prix};\nPrix Total : {self.prixTotal};\nQuantité : {self.quantite}")
        
# article = Article("drap", 25, 25)

# article.afficheArticle()

while True:
    print("1. Ajouter un article\n2. Afficher les articles\n3. Quittez")
    choix = int(input("Faites votre choix : "))
    print("=" * 25)
    if choix == 1:
        nom = input("Saisir le Nom de l'article : ")
        prix = int(input("Saisir le Prix Unitaire de l'article : "))
        quantite = int(input("Saisir la Quantité de l'article : "))
        article = Article(nom, prix, quantite)
        print("=" * 25)
    elif choix == 2:
        article.afficheArticle()
        print("=" * 25)
    elif choix == 3:
        print("Nous vous remercions d'avoir utilisé le programme")
        break
    else:
        print("Choix invalide !")
        print("=" * 25)