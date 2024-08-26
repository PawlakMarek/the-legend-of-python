"""
Instructions
Let's try a classic Computer Science project: simple calculator program! 🔢

Create a calculator.py program and define these five functions:

add(a, b) that adds two numbers a and b.
subtract(a, b) that subtracts two numbers a and b
multiply(a, b) that multiplies two numbers a and b.
divide(a, b) that divides two numbers a and b.
exp(a, b) that takes a to the exponent (or power) of b.
Make sure to return the result in each function definition.

Test your calculator by calling each function once to make sure that it works!
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def exp(a, b):
    return a**b


print(f"add(1, 2) == {add(1, 2)}")  # 3
print(f"subtract(1, 2) == {subtract(1, 2)}")  # -1
print(f"multiply(1, 2) == {multiply(1, 2)}")  # 2
print(f"divide(1, 2) == {divide(1, 2)}")  # 0.5
print(f"exp(1, 2) == {exp(1, 2)}")  # 1
print(f"exp(2, 2) == {exp(2, 2)}")  # 4
