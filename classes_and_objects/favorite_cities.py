"""
Instructions
Ever wonder how many people live in New York City? What about London?

Create a favorite_cities.py program.

Let's make a City class that uses the __init__() method to define the following attributes:
- name (string)
- country (string)
- population (integer rounded to the nearest thousand people)
- landmarks (list of strings)

Next, create an object for your hometown and assign the attributes above.

Lastly, create another object of the city that you've always wanted to visit!

Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.
"""


class City:
    def __init__(
        self, name, country, population, landmarks, nickname, founding_year, mayor
    ):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.nickname = nickname
        self.founding_year = founding_year
        self.mayor = mayor


poznan = City(
    "Poznań",
    "Poland",
    540000,
    ["Old Market Square", "Cathedral", "Lake Malta"],
    "The City of Goats",
    1253,
    "Jacek Jaśkowiak",
)

new_york = City(
    "New York City",
    "USA",
    8258000,
    ["Statue of Liberty", "Central Park", "Empire State Building"],
    "The Big Apple",
    1624,
    "Bill de Blasio",
)
