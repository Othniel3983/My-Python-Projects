import math

def add(*args):
    return sum(args)

def subract(a, b):
    return a - b

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(a, b):
    if b == 0:
        return ValueError("Error: Division by 0 is not possible")
    return a/b

def percentage(a, b):
    return (a*b)/100

def square_root(a):
    if 1<0:
        return ValueError("Error: Negative number for this peration is not allowed")
    return math.sqrt(a)

def power(a, b):
    return a**b

def validate_input(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def calculator():
    print("\nPYTON CALCULATOR")

    while True:
        print("\nMENU")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplicaton")
        print("4. Division")
        print("5. Percentages")
        print("6. Square Root")
        print("7. Power")
        print("8. Exit")
        
        choice = input("Choose an operation from 1 - 8: ")

        if choice == "1":
            numbers = input("\nEnter numbers to add, separated by space: ").split()
            if all(validate_input(num) for num in numbers):
                print(f"Result: {add(*map(float, numbers))}")
            else:
                print("Invalid Input: Enter numbers only, separate by space.")
        
        elif choice == "2":
            try:
                a = float(input("\nEnter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {subract(a, b)}")
            except ValueError:
                print("Value Error: Please enter a number")

        elif choice == "3":
            numbers = input("\nEnter numbers to multiply, separated by space: ").split()
            if all(validate_input(num) for num in numbers):
                print(f"Result: {multiply(*map(float, numbers))}")
            else:
                print("Invalid Input: Enter numbers only, separted by space")
        
        elif choice == "4":
            try:
                a = float(input("\nEnter numerator: "))
                b = float(input("Enter denomenator"))
                result = divide(a, b)
                if isinstance(result, ValueError):
                    print(result)
                else:
                    print(f"Result: {result}")
            except ValueError:
                print("Value Error: Please enter a number")
        
        elif choice == "5":
            try:
                a = float(input("\nEnter the number: "))
                b = float(input("Enter the percentage: "))
                print(f"Result: {percentage(a, b)}")
            except ValueError:
                print("Value Error: Please enter a number")
        
        elif choice == "6":
            
            try:
                a = float(input("\nEnter nunmber: "))
                result = square_root(a)
                if isinstance(result, ValueError):
                    print(result)
                else:
                    print(f"Result: {result}")
            except ValueError:
                print("Value Error: Please enter a number")
        
        elif choice == "7":
            try:
                a = float(input("\nEnter base: "))
                b = float(input("Enter exponent: "))
                print(f"Result: {power(a, b)}")
            except ValueError:
                print("Value Error: Please enter a number")
        
        elif choice == "8":
            print("\nGoodbye!!!")
            break

        else:
            print("\nInvalid choice. Please select a valid option (1-8). Thank You")

calculator()
