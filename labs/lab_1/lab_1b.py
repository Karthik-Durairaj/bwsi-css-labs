"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    if operation == "add":
        return (num1 + num2)
    elif operation == "subtract":
        return (num1 - num2)
    elif operation == "multiply":
        return (num1 * num2)
    elif operation == "divide":
        if num2 != 0:
            return (num1 / num2)
        else:
            print("Cannot divide by zero.")
            return -1
    else:
        print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
        return -1

def sanitize_input(operation: str) -> float:
    while True:
        try:
            number = float(input(operation))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    
    print(f"===== Simple Calculator =====")
    # Ask the user for sample input    
    num1 = sanitize_input("Enter the first number: ")
    num2 = sanitize_input("Enter the second number: ")
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)

    if(result != -1):
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    
if __name__ == "__main__":
    main()
