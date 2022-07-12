# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers
#1 year = 365days, 52 weeks, 12 months

age = input("How old are you ?: ")
remaining = 90 - int(age)
inDays = remaining*365
inWeeks = remaining*52
inMonths = remaining*12
print(f"You have {inDays} days, {inWeeks} weeks, and {inMonths} months left.")
