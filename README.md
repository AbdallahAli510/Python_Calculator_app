# Python_Calculator_app
# 🧮 Simple CLI Calculator

A small, terminal-based **Calculator** written in Python.  
Supports basic arithmetic operations: addition, subtraction, multiplication, division, modulus, exponentiation, and floor division. No external libraries required.

---

## Table of Contents
- [About](#about)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Example Session](#example-session)  
- [How it works](#how-it-works)  
- [Customization](#customization)  
- [Contributing](#contributing)  
- [License](#license)  
- [Script (`calculator.py`)](#script-calculatorpy)

---

## About
This CLI calculator provides a menu-driven interface to perform common arithmetic operations. It validates numeric input and handles division-by-zero errors gracefully.

---

## Features
- Addition, subtraction, multiplication  
- Division and floor division (with zero-check)  
- Modulus (remainder)  
- Exponentiation (power)  
- Simple input validation and error messages  
- No dependencies — works with Python 3.x

---

## Requirements
- Python 3.x

---

## Installation
1. Create a new file in your repository (recommended name: `calculator.py`).  
2. Paste the script from the **Script** section below.  
3. Commit and push to GitHub. Optionally add this README as `README.md`.

---

## Usage
Run the script from a terminal:

```bash
python calculator.py
```

Choose an operation from the menu, then enter two numeric values. Enter `q` to quit.

---

## Example Session

```
$ python calculator.py

Choose the desired arithmetic operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponentiation
7. Floor division
Enter 'q' to quit
Enter your choice (1/2/3/4/5/6/7/q): 1
Enter first number: 12
Enter second number: 5
Result: 17.0

Choose the desired arithmetic operation:
...
Enter your choice (1/2/3/4/5/6/7/q): q
Exiting the calculator. Goodbye!
```

---

## How it works
- Each operation is implemented as a small function (`add`, `subtract`, `multiply`, etc.).  
- A dictionary maps menu choices (`"1"`..`"7"`) to the corresponding functions.  
- The main loop shows the menu, reads user choice, validates it, reads two numbers (floats), calls the chosen function, and prints the result.  
- Division-related functions check for division by zero and raise a `ValueError` which is caught and shown to the user.

---

## Customization
- Add more operations (square root, logarithm) using `math` module.  
- Add command-line arguments to run a single operation non-interactively (`argparse`).  
- Persist a history of calculations to a text file.  
- Improve UX by formatting integers without `.0` when appropriate.

---

## Contributing
Small, beginner-friendly project — contributions welcome:
- Add unit tests.  
- Add advanced operations or input parsing improvements.  
- Add localization or better CLI formatting.

---

## License
This project can be reused freely. Add an open-source license file (e.g., MIT) if you want to clarify reuse terms.

---

## Script: `calculator.py`
Copy the exact code below into `calculator.py`:

```python
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
```
