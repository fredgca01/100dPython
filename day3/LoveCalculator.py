# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
# e.g.
# name1 = "Angela Yu
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
# Print: "Your score is 53."

first_name = input("What is your full name ?: ").upper()
second_name = input("What is her/his full name ?: ").upper()
names = first_name+second_name
first_digit=0
second_digit=0
first_digit+=names.count("T")
first_digit+=names.count("R")
first_digit+=names.count("U")
first_digit+=names.count("E")
second_digit+=names.count("L")
second_digit+=names.count("O")
second_digit+=names.count("V")
second_digit+=names.count("E")

lovescore = str(first_digit)+str(second_digit)
if int(lovescore)<10 or int(lovescore)>90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif int(lovescore)>=40 and int(lovescore)<=50:
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}")

