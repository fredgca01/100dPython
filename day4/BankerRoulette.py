# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. 
# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
# When you run the code, just use a random number as the seed. e.g. 67346 
# It doesn't matter what you chose, it's only for our testing code to check your work.

import random
#names_string=input("Who were the attendees tonight ?")
#names = names_string.split(",")
names=["Fred","Fady","Manu","Guilhem","Emilie"]
# winner=random.randint(0,len(names)-1)
#print(f"{names[winner]} is paying the bill tonight !! :)")
print(random.choice(names))