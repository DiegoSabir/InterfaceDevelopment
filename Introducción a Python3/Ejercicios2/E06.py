"""
Using the Luhn algorithm, determine whether a credit card number is valid or not. Luhn Algorithm:
A credit card, or a SIM card, is valid if the sum of the reverse of the even-positioned 
numbers * 2 with the reverse of the odd-positioned numbers results in a number ending in 0. 
Example:
Sample number: 4 9 9 2 7 3 9 8 7 1 6
Multiply by 2 the digits in even positions starting from the end:
        (1*2) = 2, (8*2) = 16, (3*2) = 6, (2*2) = 4, (9*2) = 18
Add the digits in odd positions to the digits of the obtained products:
  6 + (2) + 7 + (1+6) + 9 + (6) + 7 + (4) + 9 + (1+8) + 4 = 70. 
(1+6) is from the multiplication of 8x2, and (1+8) is from the multiplication of 9x2 from the first step.
Since it's 70, ending in 0, it's valid: 70 mod 10 = 0.
"""

creditCard = input("Enter the credit card number: ")
cardDigits = [int(digit) for digit in creditCard[::-1]]
total = 0

for i in range(len(cardDigits)):
    if i % 2 == 1:
        evenDigits = cardDigits[i] * 2
        if evenDigits > 9:
            evenDigits -= 9
        total += evenDigits
    else:
        total += cardDigits[i]

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
    