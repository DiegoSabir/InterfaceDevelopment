"""
Dado el radio de una circunferencia calcula su perímetro y área.
Usad función math para usar pi
"""
import math

radius = float(input("Enter the radius of the circle:"))

perimeter = 2 * math.pi * radius

area = math.pi * radius ** 2

print(f"Perimeter:{perimeter}")
print(f"Area: {area}")