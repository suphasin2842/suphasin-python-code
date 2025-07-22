'''
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese
'''
weight = float(input("Enter your weight in kg: "))
hight = float(input("Enter your height in meters: "))
bmi = weight / hight ** 2
if bmi >= 30.0:
 print ("BMI: Obese")
elif 25.0 <= bmi and bmi <= 29.9:
 print ("BMI: Overweight")
elif 18.5 <= bmi and bmi <= 24.9:
 print ("BMI: Normal weight")
else:
 print ("BMI: Underweight")