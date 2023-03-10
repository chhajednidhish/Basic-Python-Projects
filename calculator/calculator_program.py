'''
Problem statement of calculator made by ChatGPT
This code is a simple calculator program that performs basic mathematical operations such as addition, subtraction, multiplication, and division. The program uses the 'art' module to display a logo at the start and the 'os' module to clear the screen after each calculation.

The program has four functions, 'add', 'subtract', 'multiply', and 'divide', which take in two numbers as inputs and return the sum, difference, product, and remainder of the two numbers respectively.

The 'calculator_logic' function contains the main logic of the program. It first displays the logo using the 'art.logo' command. Then, it initializes two variables, 'num1' and 'should_continue', which are used later in the program. The 'operations' variable is a dictionary that maps the mathematical symbols to the corresponding functions.

The program then asks the user to pick an operation to perform, and takes the second number as input. The selected operation is then performed using the 'operation_selected' variable and the result is displayed. The user is then asked if they want to continue with the result or start a new calculation. If the user wants to continue, the 'num1' variable is updated with the result and the loop continues. If the user wants to start a new calculation, the 'should_continue' variable is set to False, the screen is cleared, and the calculator logic is run again.

The 'main' function then calls the 'calculator_logic' function, and the last line checks if the program is being run as the main script. If it is, the 'main' function is called.
'''
# Calculator
# Importing required modules
import art
import os


def add(a, b):
    '''Returns sum of two numbers given as inputs'''
    return a + b


def subtract(a, b):
    '''Returns difference of two numbers given as inputs'''
    return a - b


def multiply(a, b):
    '''Returns product of two numbers given as inputs'''
    return a * b


def divide(a, b):
    '''Returns remainder of two numbers given as inputs'''
    return a / b


def calculator_logic():
    '''Contains the main logic of program'''
    print(art.logo)

    # Initializing basic variables
    num1 = float(input("What is the first number?: "))
    should_continue = True
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    # Displaying all the operations possible, to take one as an input
    for symbol in operations:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick an operation you want to perform: ")
        # Num2 is asked after the operation just to improve user experience
        # as well as to simulate real world like calculators
        num2 = float(input("What is the next number?: "))

        # Performing required operations
        operation_selected = operations[operation_symbol]
        result = operation_selected(num1, num2)

        # Final output
        print(f"\n{num1} {operation_symbol} {num2} = {result}")

        # Asking if the user wants to continue the loop
        continue_with_result = input(
            f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_with_result == 'n':
            should_continue = False
            os.system('clear')
            calculator_logic()
        elif continue_with_result == 'y':
            num1 = result
        else:
            print("Invalid input...")


def main():
    calculator_logic()


if __name__ == "__main__":
    main()
