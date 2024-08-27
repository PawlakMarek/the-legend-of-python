"""
Instructions
In the last exercise, we created a Restaurant class.

In a new file called bobs_burgers.py, create an instance of the Restaurant class called bobs_burgers with the following attributes:

'Bob\'s Burgers'
'American Diner'
4.7
False
Once you do that, create two more instances of the Restaurant class with your favorite dinner spots nearby.

Then, use print(vars()) to output each of the three restaurants!
"""

import restaurants

bob_burgers = restaurants.Restaurant()
bob_burgers.name = "Bob's Burgers"
bob_burgers.category = "American Diner"
bob_burgers.rating = 4.7
bob_burgers.delivery = False

sahar_kebab = restaurants.Restaurant()
sahar_kebab.name = "Sahar Kebab Dębiec"
sahar_kebab.category = "Kebab"
sahar_kebab.rating = 4.4
sahar_kebab.delivery = False

chilli_masala = restaurants.Restaurant()
chilli_masala.name = "Chilli Masala"
chilli_masala.category = "Indian"
chilli_masala.rating = 4.3
chilli_masala.delivery = True

print(vars(bob_burgers))
print(vars(sahar_kebab))
print(vars(chilli_masala))
