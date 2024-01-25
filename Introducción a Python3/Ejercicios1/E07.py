"""
Enter a word with more than 9 letters via the keyboard and print:
- The first three letters
- The last three letters
- The letters located between the 4th and 7th positions
"""

word = input("Enter a word with more than 9 letters:")

firstThree = word[:3]
lastThree = word[-3:]
middle = word[3:7]

print("The first three letters:", firstThree)
print("The last three letters:", lastThree)
print("The letters located between the 4th and 7th positions:", middle)