from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def take_input():
    """Taking initial user input"""
    menu = Menu()
    print(f"\nWhat would you like? ({menu.get_items()})"
          "\nPress A for espresso"
          "\nPress B for latte"
          "\nPress C for cappuccino")
    user_choice = input("\nEnter your choice: ").lower()

    return user_choice


def main():
    """Main logic for the coffee machine"""
    print("Welcome to the coffee machine!\n"
          "Hope you have a great day today...😇\n")

    # Creating objects of classes I will be using
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    user_input = 'on'
    selected_coffee = ''
    while user_input != 'off':
        user_input = take_input()  # Taking user inputs
        if user_input == 'report':  # If user wants the report
            coffee_maker.report()
            money_machine.report()
        elif user_input == 'a':  # If user wants espresso coffee
            selected_coffee = 'espresso'
            drink = menu.find_drink(selected_coffee)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        elif user_input == 'b':  # If user wants latte coffee
            selected_coffee = 'latte'
            drink = menu.find_drink(selected_coffee)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        elif user_input == 'c':  # If user wants cappuccino coffee
            selected_coffee = 'cappuccino'
            drink = menu.find_drink(selected_coffee)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        elif user_input == 'off':
            print("Thank you for using our coffee machine! Hope you come back again...")
            break
        else:
            print("Wrong Input, please try again!\n")


if __name__ == "__main__":
    main()
