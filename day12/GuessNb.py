from random import randint
from logo import GUESS_NB

EASY = 10
HARD = 5

def setDifficulty():
    answer = input("Quel niveau, facile (F) ou difficile (D) ?: ").lower()
    if answer=="d":
        return HARD
    else:
        return EASY
print(GUESS_NB)
print("Bienvenue, vous allez devoir deviner un nombre entre 1 et 100")
max_try = setDifficulty()
guess = randint(1,100)
nb=-1
while max_try>0 and nb != guess:
    print(f"Vous avez {max_try} coups pour deviner.")
    nb = int(input("A quel nombre penses-tu ? "))
    max_try-=1
    if nb>guess:
        print("Trop grand.")
    elif nb<guess:
        print("Trop petit.")

if(nb==guess):
    print(f"Gagné, il fallait bien trouver: {guess}")
else:
    print(f"Perdu !, le nombre a trouver etait: {guess}")

