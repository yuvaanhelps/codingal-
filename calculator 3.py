
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def square_root(a):
    return math.sqrt(a)

while True:
    print("\n--- FUNCTION CALCULATOR ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "6":
        print("Calculator closed!")
        break

    if choice == "5":
        a = float(input("Enter a number: "))
        if a < 0:
            print("Cannot calculate real square root!")
        else:
            print("Answer:", square_root(a))
        continue

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Answer:", add(a, b))
        elif choice == "2":
            print("Answer:", subtract(a, b))
        elif choice == "3":
            print("Answer:", multiply(a, b))
        elif choice == "4":
            print("Answer:", divide(a, b))
    else:
        print("Invalid choice!")
