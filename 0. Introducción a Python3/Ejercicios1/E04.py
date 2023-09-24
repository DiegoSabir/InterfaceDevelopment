"""
Write a program that asks the user for their weight (in kg) and height (in meters), calculates the body mass 
index (BMI), and stores it in a variable <imc>, displaying the following message on the screen: Your body mass index is <imc>,
with two decimal places.
Formula: imc = weight / height * height
"""

weight = float(input("Enter your weight:"))
height = float(input("Enter your height:"))

imc = weight / height ** 2

print(f"Your body mass index is {imc:.2f}")