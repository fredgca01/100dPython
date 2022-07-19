# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

def prime_checker(number):
    nb=int(number)
    isPrime=True
    for i in range(2,nb):
        if (nb%i==0):
            isPrime=False
    print(f"Is {nb} a prime number ? {isPrime}")

prime_checker(2)
prime_checker(4)
prime_checker(73)
prime_checker(75)
prime_checker(97)
n = input("Give the number you want to check if it's a prime nb ?: ")
prime_checker(n)
