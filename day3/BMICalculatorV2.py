# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

#    Under 18.5 they are underweight
#    Over 18.5 but below 25 they have a normal weight
#    Over 25 but below 30 they are slightly overweight
#    Over 30 but below 35 they are obese
#    Above 35 they are clinically obese.



height = input("enter your height (m): ")
weight = input("enter your weight (kg): ")

bmi_index = int(weight) / (float(height))**2
bmi_index = round(bmi_index)
print("Your BMI index is: "+str(bmi_index))
if(bmi_index<=18.5):
    print("You are underweight")
elif(bmi_index<=25):
    print("You have a normal weight")
elif(bmi_index<=30):
    print("You are slightly overweight")
elif(bmi_index<=35):
    print("You are obese")
elif(bmi_index>35):
    print("You are clinically obese")