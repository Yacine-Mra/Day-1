from random import randint

a = randint (0, 100)

print("Donnez le nombre exact :")

while a == a:
    nombre = input()
    if a < a+1:
        print("le nombre est trop haut")
    elif a > a+1:
        print("le nombre est trop bas")
    elif a == a:
        print("le nombre est juste")