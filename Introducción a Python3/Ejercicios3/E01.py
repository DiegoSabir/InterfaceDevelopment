"""
Create a list of N elements, a value that is requested through the keyboard, 
and then fill it with random integers between 1 and 10. Subsequently, 
display the list and the number that repeats the most.
"""
import random

listSize = int(input("Enter the size of the list: "))

numberList = []

for i in range(listSize):
    number = random.randint(1, 10)
    numberList.append(number)

print("Generated list:", numberList)

maxCounter = 0
repeatedNumber = None

for number in numberList:
    counter = numberList.count(number)
    
    if counter > maxCounter:
        maxCounter = counter
        repeatedNumber = number

if repeatedNumber is None:
    print("No number is repeated.")
else:
    print("The most repeated number is ", repeatedNumber, " and it repeats ", maxCounter, " times.")
