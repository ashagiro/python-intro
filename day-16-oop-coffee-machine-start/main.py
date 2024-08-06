from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
while is_on:
    entry = input(f"What would you like? ({menu.get_items()}) ")
    if entry == "off":
        is_on = False
    elif entry == "report":
        machine.report()
        money.report()
    else:
        order = menu.find_drink(entry)
        if order == None:
            print("Invalid entry. Try again.")
            continue
        if machine.is_resource_sufficient(order) and money.make_payment(order.cost):
            machine.make_coffee(order)

