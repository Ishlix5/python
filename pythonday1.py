# Basic calculator program
# get user input
num1 = float(input("enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation( +, -, *, /:)")

# perform calculation
if operation == "+":
    result = num1 +num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")