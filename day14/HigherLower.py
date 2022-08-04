# Qui a le plus de follower entre ces deux propositions ?
from GameData import data
from random import choice

def next():
    return choice(data)

def doYouWin(first, second, userChoice):
    if first['name'] == userChoice['name']:
        if first['follower_count']>second['follower_count']:
            print(f"Exact ! {first['follower_count']} contre {second['follower_count']}")
            return True
        else :
            print(f"Perdu ! {first['follower_count']} contre {second['follower_count']}")
            return False
    else :
        if first['follower_count']>second['follower_count']:
            print(f"Perdu ! {first['follower_count']} contre {second['follower_count']}")
            return False
        else :
            print(f"Exact ! {first['follower_count']} contre {second['follower_count']}")
            return True
score=0
noError = True
first = next()
while noError :
    print("Qui a le plus d'abonnés entre ces deux propositions ?")
    print(f"A) {first['name']}, {first['description']} from {first['country']}")
    print("et ")
    second = next()
    print(f"B) {second['name']}, {second['description']} from {second['country']}\n")
    answer = input("Qui ? (A ou B) ").lower()
    if answer=="a":
        noError = doYouWin(first,second,first)
        first = first
    else :
        noError = doYouWin(first,second,second)
        first = second
    if noError:
        score+=1
        
    print(f"\n Votre score est de:{score} \n")