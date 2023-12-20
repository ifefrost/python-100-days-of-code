from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Start the coffee machine
is_on = True

# while loop to keep the coffee machine running

while is_on:
    options = menu.get_items()
    prompt = input(f"What would you like? ({options}):").lower()
    if prompt == "off":
        is_on = False
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(prompt) is None:
        print("Invalid drink selection. Please try again.")
    else:
        drink = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        else:
            print("Sorry, not enough resources. Please try again.")
