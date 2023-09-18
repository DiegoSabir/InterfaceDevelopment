"""
Escribe un programa que solicite la fecha de
nacimiento de un usuario y calcule su edad actual.
"""
from datetime import datetime

birthdateString = input("Enter your birthdate(YYYY-MM-DD): ")

birthdate = datetime.strptime(birthdateString, "%Y-%m-%d")

actualDate = datetime.now()

difference = actualDate - birthdate

age = difference.days // 365

print(f"Actual age: {age} years")