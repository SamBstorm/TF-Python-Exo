stock1 = 5 
stock2 = 2
stock3 = 0

print("Veuillez sélectionner une boisson :")
print("1. Eau")
print("2. Soda")
print("3. Orangeade")

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
    case _ : 
        print("Choix indisponible")