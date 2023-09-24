"""
Write a program that asks the user for the number of hours worked
and the hourly wage in € with two decimal places. Then, it should 
display on the screen the corresponding pay under the same conditions.
"""

hoursWorked = int(input("Enter the hours worked:"))
hourlyWage = float(input("Enter the hourly wage in €:"))

salary = hoursWorked * hourlyWage

print(f"The earnings are {salary:.2f} €")
