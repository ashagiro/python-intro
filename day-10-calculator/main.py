# Functions with outputs
# Using recursion
from art import logo


def add(a, b):
    return a+b
def substract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

operations = {
    "/": divide,
    "+": add,
    "*": multiply,
    "-": substract,
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for operation in operations:
        print(operation)
    again = True   
    while again:
        operation = input("Please pick an operation: ")
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        ans = input(f"Calculate again? Press 'y' to continue calculating with {answer}, 'n' to start a new calculation and any other key to exit. ")
        if ans == "n":
            again = False
            calculator()
        elif ans == "y":
            num1 = answer
        else:
            return

calculator()