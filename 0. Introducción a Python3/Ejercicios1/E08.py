"""
A toy store is very successful with two of its products: clowns and dolls.
They usually do mail-order sales, and the logistics company charges them based on the weight of each package.
So, they need to calculate the weight of the clowns and dolls that will go in each package on demand.
Each clown weighs 112 g, and each doll weighs 75 g.
Write a program that reads the number of clowns and dolls sold in the last order
and calculates the total weight in kg of the package that will be sent and the price, with a rate of 3.5 €/kg.
"""

clownWeight = 112
dollWeight = 75
rate = 3.5

clowns = int(input("Enter the number of clowns:"))
dolls = int(input("Enter the number of dolls:"))

totalClownWeight = clowns * clownWeight
totalDollWeight = dolls * dollWeight
totalGrams = totalClownWeight + totalDollWeight
totalKg = totalGrams / 1000
totalPrice = totalKg * rate

print(f"Total package weight: {totalKg:.2f} kg")
print(f"Package price: {totalPrice:.2f} €")
