"""
Given the radius of a circle, calculate its circumference and area.
Use the math module to access pi.
"""
import math

pi = math.pi
radius = float(input("Enter the radius:"))

perimeter = 2 * pi * radius
area = pi * radius ** 2

print(f"Perimeter: {perimeter:.2f} / Area: {area:.2f}")