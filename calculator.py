def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    if b == 0:
        return "Error: Can not devide by zero"
    return a / b

def power(a, b):
    return a ** b

def reminder(a, b):
    if b == 0:
        return "Error: Can not devide by zero"
    return a % b

def calculator():
    print("Hello, Welcome to OT's calculator")

    while True:
        print("\nChoose an operator:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Devide")
        print("5. Exponent")
        print("6. Reminder")
        print("7. Check History")
        print("8. Exit")

        choice=input("Enter choice(1-8): ")
        if choice=="8":
            print("Thank you for using the calculator. Have a nice day!")
            break
        if choice not in ['1','2','3','4','5','6','7']:
            print("Invalid input. Please choose a valid option")
            continue

        try:
            num1=float(input("Enter the first number: "))
            num2=float(input("Enter the second number: "))
        except ValueError:
            print("Invalid number. Please enter numeric values.")
            continue

        history=[]

        if choice == "1":
            print("Answer: ", add(num1, num2))
            history.append(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print("Answer: ", subtract(num1, num2))
            history.append(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print("Answer:", multiply(num1, num2))
        elif choice == "4":
            print("Answer: ", devide(num1, num2))
        elif choice == '5':
            print("Answer: ", power(num1, num2))
        elif choice == '6':
            print("Answer: ", reminder(num1, num2))
        elif choice == '7':
            if history:
                print("\nCalculation History:")
                for item in history:
                    print(item)
calculator()
        