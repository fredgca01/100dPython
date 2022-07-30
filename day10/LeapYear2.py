# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, 
# with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE
# This is how you work out whether if a particular year is a leap year.
#     on every year that is evenly divisible by 4 
#     **except** every year that is evenly divisible by 100 
#   **unless** the year is also evenly divisible by 400
# 
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
# it should return True if it is a leap year and return False if it is not a leap year.
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:28
# The List month_days contains the number of days in a month from January to December for a non-leap year. 
# A leap year has 29 days in February.

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysInMonth(year,month):
    if month == 2 :
        if(isLeap(year)):
            return 29
    else:
        return month_days[month-1]

def isLeap(year):
    """Return True if the year given in parameter is a Leap year"""
    if(year %4 == 0):
        if(year%100==0):
            if(year%400==0):
                return True
            else :
                return False
        else :
            return True
    else:
        return False

print("I'll tell you how many days for a given month and a given year")
year = int(input("What year ? "))
month = int(input("What month ?"))
print(f"There is {daysInMonth(year,month)} days for the month {month} in {year}")


