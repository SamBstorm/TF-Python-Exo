LIMITE_MAX = 3

stocks = []

stocks.append(3)
stocks.append(0)
stocks.append(1)

noms = ["Eau","Soda","Orangeade"]

totalStock = sum(stocks)

choix = 0

while (totalStock > 0 and choix !=4 ) :
    print("Veuillez sélectionner une boisson :")
    for i in range(LIMITE_MAX):
        print(f"{i+1}. {noms[i]}")
    print("4. Finir")

    choix = int(input());

    if choix != 4 :
        if (stocks[choix-1] > 0) :
            print(f"Voici votre {noms[choix-1]}")
            stocks[choix-1] = stocks[choix-1] - 1
        else :
            print("Sold out!")
    totalStock = sum(stocks)
print("Merci d'utiliser distributeur 3000!")