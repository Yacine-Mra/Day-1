import random 


def guess(x):
    guess=0
    z= random.randint(1, x)
    while guess != z:
        guess=int(input(f'dis un nombre entre 0 et 1000:'))
        if guess<z:            
            print(f"Le numéro à deviner est plus haut que {guess}")           
        elif guess>z:
            print(f"Le numéro à deviner est plus bas que {guess}")            
    print("Vous avez gagné")

guess(1000)