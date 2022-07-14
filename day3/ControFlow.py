height = int(input("What is your heught? (cm) "))
if(height>=120):
    print("You can ride the rollercoaster")
    bill=0
    age = int(input("How old are you ?: "))
    if age< 12:
       bill=5
    elif age <= 18:
        bill=7
    else:
        bill=12
    if age > 45 and age <55:
        bill=0
        print("Free ticket for you !!")
    answer = input("Do you want some photos ?: ")
    if(answer.upper()=="Y"):
       bill+=3
    print(f"You have to pay {bill} $") 
else:
    print("You're too small to ride the rollercoaster")