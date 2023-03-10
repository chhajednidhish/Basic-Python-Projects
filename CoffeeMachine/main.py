"""
Coffee Machine simulator:
Code a coffee machine simulator that has 3 options for coffee.
Espresso/Latte/Cappuccino (Recipes of each of the following is given)

The user can also prompt the code to ask for a report, that is how much resources are left and what is the profit
till now.
Every time a user selects a particular coffee, first the resources are checked if they are sufficient for making
the following coffee, if not the coins are returned.

Money basics :
Penny = 0.01 dollars
Nickel = 0.05 dollars
Dime = 0.10 dollars
Quarter = 0.25 dollars
"""

# Pre-defined menu
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Pre-defined resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Global profit variable
profit = 0


def take_input():
    """Taking initial user input"""
    print("What would you like? (espresso/latte/cappuccino)"
          "\nPress A for espresso"
          "\nPress B for latte"
          "\nPress C for cappuccino")
    user_choice = input("\nEnter your choice: ").lower()

    return user_choice


def print_report():
    """If the user asks for a report"""

    # Print available resources
    for key in resources.keys():
        if key == 'water' or key == 'milk':
            print(f"{key.title()}: {resources[key]}ml")
        else:
            print(f"{key.title()}: {resources[key]}mg")
    print(f"Total profit = ${profit}.\n")


def is_sufficient(selected_coffee):
    """This particular functions checks if the machine has enough resources to make the coffee."""
    for key in resources.keys():
        if resources[key] < menu[selected_coffee]['ingredients'][key]:
            print(f"Sorry there is not enough {key}!\n")
            return False
        else:
            return True


def get_coins():
    """This function takes all the coins in the machine and returns the total amount inputted"""
    print("\nEnter coins...")
    penny = int(input("How many penny?: "))
    nickel = int(input("How many nickel?: "))
    dime = int(input("How many dime?: "))
    quarter = int(input("How many quarters?: "))

    total_money_collected = penny * 0.01 + nickel * 0.05 + dime * 0.10 + quarter * 0.25

    return total_money_collected


def make_coffee(selected_coffee):
    """This function will basically deduct resources used to make the selected coffee"""
    for key in resources.keys():
        resources[key] -= menu[selected_coffee]['ingredients'][key]


def main_logic(selected_coffee):
    global profit
    if is_sufficient(selected_coffee):
        money_collected = get_coins()
        if money_collected >= menu[selected_coffee]['cost']:
            print(f"Here is ${round((money_collected - menu[selected_coffee]['cost']), 2)} in change.")
            profit += menu[selected_coffee]['cost']
            make_coffee(selected_coffee)
            print("\n-----Here is your espresso ☕️. Enjoy!-----\n")
        else:
            print("Sorry that's not enough money. Money refunded.\n")


def main():
    """Main logic for the coffee machine"""
    print("Welcome to the coffee machine!\n"
          "Hope you have a great day today...😇\n")

    # Initializing basic variables
    user_input = 'on'
    selected_coffee = ''
    while user_input != 'off':
        # Taking user inputs
        user_input = take_input()
        if user_input == 'report':
            print_report()
        elif user_input == 'a':
            selected_coffee = 'espresso'
            main_logic(selected_coffee)
        elif user_input == 'b':
            selected_coffee = 'latte'
            main_logic(selected_coffee)
        elif user_input == 'c':
            selected_coffee = 'cappuccino'
            main_logic(selected_coffee)
        elif user_input == 'off':
            break
        else:
            print("Wrong Input, please try again!\n")


if __name__ == "__main__":
    main()
