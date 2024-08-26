"""
Instructions
Create a dry.py program and check out the complete list of built-in functions:

Find 4 built-in functions that we have used previously in the course.
Pick 1 built-in function that we have not seen before.
Use each of these once in the program.

For the new function, try to read the documentation (😵‍💫) or Google it (👍)!

Add a comment for each built-in function to explain how they work.
"""

import random

array = []

for i in range(10):
    # Generates a random integer between 0 and 1000 and appends it to the array
    array.append(random.randint(0, 1000))

# print() outputs the specified message to the console
print("Randomly generated array:", array)

# min() returns the smallest item in an iterable or the smallest of two or more arguments
print("Minimum value:", min(array))

# max() returns the largest item in an iterable or the largest of two or more arguments
print("Maximum value:", max(array))

# sum() returns the sum of all items in an iterable
# len() returns the number of items in an iterable
print("Average value:", sum(array) / len(array))
