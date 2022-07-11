from tkinter import BitmapImage


height = input("enter your height (cm): ")
weight = input("enter your weight (kg): ")

bmi_index = int(weight) / (int(height))**2

print("Your BMI index is: "+str(bmi_index))
