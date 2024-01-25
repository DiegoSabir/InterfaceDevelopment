"""
Write a program that allows you to calculate the factorial of a number entered by the user.
The factorial of a number is calculated as follows:
    n · (n-1) · (n-2) · .... · 1
Taking into account the following:
If the entered number is 0, the factorial is always 1.
If the entered number is negative or decimal, display an error message to the user.
"""
number = int(input("Enter a positive number: "))

if number >= 0:
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("The factorial of", number, "is", factorial)
else:
    print("The entered number is negative.")
