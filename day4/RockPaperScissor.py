import random

data =["Paper", "Rock", "Scissor"]

print("Welcome to the rock,paper,scissor contest !\n")
player = int(input("What do you choose ? (0 for paper, 1 for rock and 2 for scissor) "))
computer = random.randint(0,2)
print(f"Computer choose: {data[computer]}")

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
result="Player win"
if(computer==1 and player==2):
    result="Computer win"
elif (computer==2 and player==0):
    result="Computer win"
elif (computer==0 and player==1):
    result="Computer win"
elif(computer==player):
    result="Draw !"
print(result)