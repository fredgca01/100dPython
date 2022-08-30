from random import randint

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

names = ["Roger","Jeremy","Emmanuel","Fred"]
student_scores={student:randint(0,100) for student in names}
print(student_scores)
passed_students={student:score for (student,score) in student_scores.items() if score>=50 }
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split(" ")
words_size={word:len(word) for word in words}
print(words_size)

weather = {"Monday":12,
"Tuesday":14,
"Wednesday":15,
"Thursday":14,
"Friday":21,
"Saturday":22,
"Sunday":24}

weather_f = {day:temp*9/5+32 for (day,temp) in weather.items()}
print(weather_f)

student_dict = {
    "names":['Roger','Jeremy', 'Emmanuel', 'Fred'],
    "score":[42,67,54,98]
}

for (keys,values) in student_dict.items():
    print(keys)
    print(values)

import pandas

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

for (index,row) in student_dataframe.iterrows():
    if row.names=="Fred":
        print(row.score)

nato_data = pandas.read_csv("./day26/nato_phonetic_alphabet.csv")
sentence = "Fred"
nato_dict={row.letter:row.code for (index,row) in nato_data.iterrows()}
#for (index,row) in nato_data.iterrows():
#    nato_dict[row.letter]=row.code
#for letter in sentence:
#    code = nato_dict.get(letter.upper())
#    print(code)

coded_sentence=[nato_dict.get(letter.upper()) for letter in sentence]
print(coded_sentence)




