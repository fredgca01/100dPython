numbers=[1,2,3]
new_numbers=[n+1 for n in numbers]
print(new_numbers)

name = "Frederic"
new_list=[letter for letter in name]
print(new_list)

new_list = [n*2 for n in range(1,5)]
print(new_list)

names = ["Roger","Jeremy","Emmanuel","Fred"]
short_name=[short.upper() for short in names if len(short)<=5]
print(short_name)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]
print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [number for number in numbers if number%2==0]
print (result)