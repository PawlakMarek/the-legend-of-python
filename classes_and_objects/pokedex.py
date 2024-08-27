"""
Instructions
Since 1996, the Pokémon video game franchise has delighted players around the world with collectible pocket monsters. A Pokédex is a device that tracks the information for Pokémon that are seen or caught.

Create a new file called pokedex.py.

Next, let's define a Pokemon class with the following attributes:
- entry (integer)
- name (string)
- types (list of strings)
- description (string)
- is_caught (boolean)

Note: Make sure to use the __init__() method.

Next, create an instance method called .speak() that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the .speak() simply print out their name twice!

Then, create another instance method called .display_details() that prints the attributes of a Pokemon object like the following:
- Entry Number: 25
- Name: Pikachu
- Type: Electric
- Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
- Pikachu has already been caught!

Lastly, create three Pokemon class objects and use the .speak() or .display_details() instance methods for each one.

For more information about any Pokémon you want to add, see the Pokédex!

Are you ready to earn the next badge?

Bonus: For all the super fans, try and add more attributes to the Pokemon class definition, like level, region, height, or weight.
"""


class Pokemon:
    def __init__(
        self, entry, name, types, description, is_caught, level, region, height, weight
    ):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
        self.level = level
        self.region = region
        self.height = height
        self.weight = weight

    def speak(self):
        print(f"{self.name} {self.name}")

    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.types}")
        print(f"Description: {self.description}")
        if self.is_caught:
            print(f"{self.name} has already been caught!")
        else:
            print(f"{self.name} has not been caught yet!")
        print(f"Level: {self.level}")
        print(f"Region: {self.region}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")


pikachu = Pokemon(
    25,
    "Pikachu",
    ["Electric"],
    "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.",
    True,
    50,
    "Kanto",
    "1'04\"",
    "13.2 lbs",
)

jigglypuff = Pokemon(
    39,
    "Jigglypuff",
    ["Normal", "Fairy"],
    "Nothing can avoid falling asleep hearing a Jigglypuff's song. The sound waves of its singing voice match the brain waves of someone in a deep sleep.",
    False,
    45,
    "Kanto",
    "1'08\"",
    "12.1 lbs",
)

dragonite = Pokemon(
    149,
    "Dragonite",
    ["Dragon", "Flying"],
    "It is said that this Pokémon lives somewhere in the sea and that it flies. However, it is only a rumor.",
    False,
    55,
    "Kanto",
    "7'03\"",
    "463.0 lbs",
)

pikachu.speak()
pikachu.display_details()
jigglypuff.speak()
jigglypuff.display_details()
dragonite.speak()
dragonite.display_details()
