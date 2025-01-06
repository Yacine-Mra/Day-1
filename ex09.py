print("Entrer un mot:")
mot = input()

if mot != mot[::-1]:
    print("votre mot est une palindrome")
else:
    print("votre mot n'est pas une palindrome")

