"""
Instructions
When you go to a drive-thru like McDonald's, you can order food using the item numbers. For example, a Happy Meal might be a #3!

Create a drive_thru.py program with your favorite fast food chain's menu.

Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

For example, if you called the function with:

Argument value 1, it could return '🍔 Cheeseburger'.
Argument value 2, it could return '🍟 Fries'.
Argument value 3, it could return '🥤 Soda'.
Argument value 4, it could return '🍦 Ice Cream'.
Argument value 5, it could return '🍪 Cookie'.
Make sure to call this function a few times to make sure that it works!

Lastly, let's do the following:

Create a welcome menu and put that in a welcome() function.
Create a main program that takes in user input with input().
"""

menu = ["🍔 Cheeseburger", "🍟 Fries", "🥤 Soda", "🍦 Ice Cream", "🍪 Cookie"]


def get_item(item):
    return menu[item]


def print_menu():
    for i in range(len(menu)):
        print(f"{i+1}: {menu[i]}")
    print(f"0: quit")


def print_order(order):
    for i in range(len(order)):
        print(order[i])


def welcome():
    print("Welcome to the drive-thru! Please select an item from the menu below:")
    print_menu()


welcome()
order = []
while True:
    item = int(input("Enter the number of the item you want: "))
    if item == 0:
        if order == []:
            print("You didn't order anything!")
        else:
            print("Thank you for your order!")
            print("Your order:")
            print_order(order)
        break
    order.append(get_item(item - 1))
    print(f"Added {get_item(item-1)} to your order.")
    print("Your order so far:")
    print_order(order)
    print("Do you want to order anything else?")
    print_menu()
