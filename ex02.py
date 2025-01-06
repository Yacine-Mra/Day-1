print("Choisissez une opération entre soustraction, addition, multiplication et division :")
operation = input()
print ("Choisissez 2 nombres")
num1 = int(input("Premier nombre : "))
num2 = int(input("Deuxième nombre : "))

if operation == "soustraction" :
    print("Le résultat est :", num1 - num2)
elif operation == "addition" :
    print("Le résultat est :", num1 + num2)
elif operation == "multiplication":
    print("Le résultat est :", num1 * num2)
elif operation == "division" :
    print("Le résultat est :", num1 / num2)
    
        