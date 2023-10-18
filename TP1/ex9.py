nbr = input("entrez le nombre des produit")
total = 0
for i in range(0,int(nbr)):
    nom = input("entrez le nom d'article")
    qunt = int(input("entrez la quantité de produit"))
    prix = int(input("entrez le prix unitaire"))
    print("Totale pour l'article",nom,":",str(qunt*prix),"dh (ht)")
    total += qunt*prix
print("Totale de votre facture est :",total + total*0.2)
