"""
Mastermind is a game that involves guessing a number.
Write a program that generates a random integer between 1 and 10.
Then, we will be asked to guess the number.
The program will provide hints that if we guess wrong, 
it will tell us whether the number we guessed is higher or lower than the random number.
You should include the number of attempts at the end of the program execution.
"""
import random

x = random.randint(1, 10)
attempts = 0
number = 0

while number != x:
    number = int(input("Enter the secret number:"))
    attempts += 1
    
    if number > x:
        print("The entered number is higher.")
    elif number < x:
        print("The entered number is lower.")
        
print("You guessed the number in", attempts, "attempts.")
