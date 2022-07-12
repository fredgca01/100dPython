from tkinter import BitmapImage


height = input("enter your height (m): ")
weight = input("enter your weight (kg): ")

bmi_index = int(weight) / (float(height))**2
print("Your BMI index is: "+str(round(bmi_index)))
