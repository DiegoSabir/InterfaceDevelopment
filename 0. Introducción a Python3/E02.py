"""
Write a program that asks the user for the number of hours worked 
and the hourly rate in euros with two decimal places. 
Then, it should display on the screen the corresponding payment under the same conditions.
"""

hour = int(input("Enter the worked hours: "))

salaryHour = float(input("Enter the worked hours: "))

salary = hour * salaryHour

print(f"Salary:{salary:.2f}")
