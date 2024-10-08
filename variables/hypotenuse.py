"""
Instructions:

If you slept through your geometry class, a Pythagorean theorem is the relationship between the three sides of a right triangle. It was named after the Greek philosopher Pythagoras, born around 570 BC.

Pythagorean equation looks like:

c = sqrt(a^2 + b^2)

The a is the length of a short side.
The b is the length of another short side.
The c is the length of the hypotenuse.
The hypotenuse is the longest side of the right triangle.

Create a hypotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

Bonus: If you are looking for a harder challenge, try the Quadratic formula!
"""

a = input("Enter the length of side a: ")
b = input("Enter the length of side b: ")
a = float(a)
b = float(b)
c = (a**2 + b**2) ** 0.5
print("The length of the hypotenuse is", c)
