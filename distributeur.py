stock1 = 5 
stock2 = 2
stock3 = 0

choix = 0

while ((stock1 + stock2 + stock3) > 0 and choix !=4 ) :
    print("Veuillez sélectionner une boisson :")
    print("1. Eau")
    print("2. Soda")
    print("3. Orangeade")
    print("4. Finir")

    choix = int(input());

    match choix:
        case 1 : 
            if (stock1 != 0) :
                print("Voici votre eau")
                stock1 = stock1 - 1
            else :
                print("Sold out!")        
        case 2 : 
            if( stock2 != 0 ) :
                print("Voici votre soda")
                stock2 = stock2 - 1
            else :
                print("Sold out!")
        case 3 : 
            if( stock3 != 0 ) :
                print("Voici votre orangeade")
                stock3 = stock3 - 1
            else :
                print("Sold out!")
        case 4 :
            print("Merci d'utiliser distributeur 3000!")
        case _ : 
            print("Choix indisponible")