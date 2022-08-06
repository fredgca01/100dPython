from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

running = True
menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

while running :
    answer = input(f"What do you want ? {menu.get_items()} : \n").lower()
    if answer=="off":
        print("Shuting down")
        running=False
    elif answer =="report":
        print("Printing coffee machine report")
        print(money.report())
        print(coffee.report())
    else :
        drink = menu.find_drink(answer)
        if drink == None:
            print("Choose another drink")
        elif coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
