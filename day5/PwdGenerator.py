import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator")
lettersNb = int(input("How many letters would you want in your password ?\n"))
numbersNb = int(input("How many numbers would you want in your password ? \n"))
specialsNb = int(input("How many special characters would you want in your password ?\n"))

result= []
for num in range(0,lettersNb):
    result.append(random.choice(letters))
for num in range(0,numbersNb):
    result.append(random.choice(numbers))
for num in range(0,specialsNb):
    result.append(random.choice(symbols)) 

random.shuffle(result)

print(result)