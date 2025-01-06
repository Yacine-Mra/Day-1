import random
import string

def generer_mot_de_passe(longueur):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe
longueur = int(input("Quelle longueur doit avoir le mot de passe ? "))
mot_de_passe = generer_mot_de_passe(longueur)
print("Votre mot de passe est :", mot_de_passe)



