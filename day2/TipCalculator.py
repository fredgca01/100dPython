print("welcome to the Tip calculator\n")
bill = input("What was the total of the bill ?: ")
percent = input("What percentage tip would you like to give ?: ")
attendees = input("How many people to split the bill ?: ")

tip = (float(bill) * int(percent)) / 100
amount = (float(bill) + float(tip)) / int(attendees)
final_amount = "{:.2f}".format(amount)
print(f"each person should pay: {final_amount}")