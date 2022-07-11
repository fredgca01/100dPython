print("123"+"345")
# Integer
print(123 + 345)
print(1234567890)
print(1_234_567_890)

# Float
print(3.14159)
print(type(123))
print(type(float(123)))

#boolean
print(True)
print(False)



name = input("What is your name ? ")
print(type(name))
nb = len(name)
print(type(nb))
new_nb = str(nb)
print("Your name has "+new_nb+" characters")

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
number = input("enter a two digit number: ")
first_digit = number[0]
second_digit = number[1]
sum = int(first_digit)+int(second_digit)
print(str(sum))

# (); **; */; +-;
print (3 * 3 + 3 / 3 - 3)
print (3 * (3 + 3) / 3 - 3)