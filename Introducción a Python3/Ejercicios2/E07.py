"""
Create a program that generates a simple pattern, such as an asterisk triangle, square, or rectangle, 
based on the user's choice.
"""
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
choice = input("Enter one of the displayed options: ")

if choice == "Triangle":
    height = int(input("Enter the height of the triangle: "))
    
    for i in range(1, height + 1):
        print("*" * i)

elif choice == "Square":
    length = int(input("Enter the length of one side of the square: "))
    
    for i in range(length):
        print("*" * length)

elif choice == "Rectangle":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))

    for i in range(width):
        print("*" * length)
else:
    print("Invalid option. Choose one of the displayed options.")
    