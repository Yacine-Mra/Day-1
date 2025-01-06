print("Choisissez un chiffre :")
chiffre = input()
print ("Voici sa table de multiplication :")
for i in range(1, 11):
    resultat = (chiffre * i)
    print (chiffre + " x " + str(i) + " = " + resultat)
    
              