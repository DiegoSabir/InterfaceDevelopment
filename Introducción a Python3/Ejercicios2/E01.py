"""
The Collatz conjecture states that any natural number can be transformed into 1
by following these steps: if it's even, divide it by 2; if it's odd, multiply it by 3 and add 1.
Write a program that, given a number, displays the entire sequence of resulting numbers
until it becomes 1.
"""

number = int(input("Enter a positive number: "))

if number > 0:
    while number != 1:
        print(number)
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1

else:
    print("The entered number is negative.")