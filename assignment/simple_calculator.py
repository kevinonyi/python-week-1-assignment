def calculator():
    # Ask the user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Ask the user for the operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform the operation and display the result
    if operation == "+":
        result = num1 + num2
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
            print("Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")

if __name__ == "__main__":
    calculator()
3