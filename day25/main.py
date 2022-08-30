
# # data = []
# # with open("./day25/weather_data.csv") as weather:
# #     data = weather.readlines()
    
# # print(data)

# import csv

# temps=[]
# with open("./day25/weather_data.csv") as weather:
#     data = csv.reader(weather)
#     for row in data:
#         print(row[1])
#         if(row[1]!="temp"):
#             temps.append(int(row[1]))
        
# print(temps)

import pandas
from numpy import average

data = pandas.read_csv("./day25/weather_data.csv")
print(type(data))
print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)
#avg_temp = average(data_list)
#print(round(avg_temp,1))
print(round(data["temp"].mean(),1))
print(data["temp"].max())

print(data["condition"])
print(data.condition)
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

def celsToFarenheit(celsius):
    return celsius*9/5+32

dataFaren = data["temp"].apply(celsToFarenheit)
print(dataFaren)


squirel_data = pandas.read_csv("./day25/Squirrel_Data.csv")
print(squirel_data["Primary Fur Color"])
grouped_data = squirel_data.groupby(squirel_data["Primary Fur Color"])
print(grouped_data["Primary Fur Color"].count())