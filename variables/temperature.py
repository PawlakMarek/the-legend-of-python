"""
Instructions:
Create a temperature.py program that converts a temperature from Fahrenheit (°F) to Celsius (°C).

Google the current temperature of Brooklyn, NY (where Codédex is based) in °F.

Use the following formula and write it out in Python:

Celsius = (Fahrenheit - 32) / 1.8

Print out the converted temperature. 🌡️
"""

BrooklynF = 49
BrooklynC = (BrooklynF - 32) / 1.8
print(
    "Current temperature in Brooklyn, NY is " + str(BrooklynC) + " degrees of Celsius"
)
