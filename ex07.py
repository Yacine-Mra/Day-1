print("Entrer une phrase :")

phrase = input()
a = 0
print("Voici le nombre de voyelle")
for char in phrase:
    if char in 'aeiouyAEIOUY':
        a == char
        print("Voici le nombre de voyelle", a)
