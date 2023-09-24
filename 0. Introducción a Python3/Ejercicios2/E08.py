"""
Write a program that counts how many vowels (both uppercase and lowercase) 
are in a text string entered by the user.
"""

text = input("Enter a text: ")

vowelsCounter = 0
vowels = "AEIOUaeiou"

for letter in text:
    if letter in vowels:
        vowelsCounter += 1

print("Vowels on the text:", vowelsCounter)