def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2


def modulus(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 % num2


def exponentiate(num1, num2):
    return num1**num2


def floor_divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 // num2


operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide,
    "5": modulus,
    "6": exponentiate,
    "7": floor_divide,
}

while True:
    print("\nChoose the desired arithmetic operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor division")
    print("Enter 'q' to quit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/q): ")

    if choice == "q":
        print("Exiting the calculator. Goodbye!")
        break

    if choice not in operations:
        print("Invalid choice. Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    try:
        result = operations[choice](num1, num2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
