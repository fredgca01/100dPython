# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

print("Welcome to Fred Pizza\n")
size = (input("What is the size of the pizza ? (S, M, L)")).upper()
peperoni = (input("Do you some additionnal peperonni ? (Y/N)")).upper()
cheese = (input("Do you want some extra cheese ? (Y/N) ")).upper()

bill=0
if(size=="S"):
    bill+=15
    if(peperoni=="Y"):
        bill+=2
elif(size=="M"):
    bill+=20
    if(peperoni=="Y"):
        bill+=3
elif(size=="L"):
    bill+=25
    if(peperoni=="Y"):
        bill+=3
if(cheese=="Y"):
        bill+=1
print(f"You have to pay: {bill}$")