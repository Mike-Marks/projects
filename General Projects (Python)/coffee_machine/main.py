from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_item_espresso = MenuItem('espresso', 50, 0, 10, 1.5)
menu_item_latte = MenuItem('latte', 200, 150, 24, 2.5)
menu_item_cappuccino = MenuItem('cappuccino', 250, 100, 24, 3.0)
menu = Menu()


while True:
    print(menu.get_items())
    request = input("What would you like?: ")
    if request == "report":
        print(money_machine.report())
    if request == "espresso":
        if coffe_maker.is_resource_sufficient(menu_item_espresso) == True:
            if money_machine.make_payment(1.5) >= 1.5:
                print(coffe_maker.make_coffee(menu_item_espresso))
    elif request == "latte":
        if coffe_maker.is_resource_sufficient(menu_item_latte) == True:
            if money_machine.make_payment(2.5) >= 2.5:
                print(coffe_maker.make_coffee(menu_item_latte))
    elif request == "cappuccino":
        if coffe_maker.is_resource_sufficient(menu_item_cappuccino) == True:
            if money_machine.make_payment(3.0) >= 3.0:
                print(coffe_maker.make_coffee(menu_item_cappuccino))
