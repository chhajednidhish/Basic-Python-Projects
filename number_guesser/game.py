"""
Create a number guesser game to guess selected number between 1 and 100.
You'll get a prompt if you are higher than the number, or lower than the number...
Here there are two levels available:-
Hard = 5 attempts for guessing the number
Easy = 10 attempts for guessing the number
"""
# Importing required modules
import art
import os
import random

EASY_TURNS = 10
HARD_TURNS = 5


def select_difficulty():
    '''Select difficulty level'''
    difficulty = input("Select your level: Hard or Easy?: ").lower()
    if difficulty == 'hard':
        return HARD_TURNS
    elif difficulty == 'easy':
        return EASY_TURNS
    else:
        print("Unknown difficulty")


def compare_guesses(user_guess, actual_number, turns):
    '''Compares if the number guessed by the user is lower, higher or equal to the actual number. Returns number of
    turns remaining'''
    if user_guess == actual_number:
        # Found the number
        print(
            f"\n---------------------------------------------------{user_guess} is the "
            f"number!---------------------------------------------------\n"
            f"------------------------------------------Congratulations!! You win the "
            f"game!------------------------------------------\n")
        return -1
    elif user_guess > actual_number:
        # Higher than the number
        print(
            f"{user_guess} is higher than the number to be guessed... Try again...")
        return turns - 1
    else:
        # Lesser than the number
        print(
            f"{user_guess} is lower than the number to be guessed... Try again...")
        return turns - 1


def guesser():
    """Main logic for the program"""
    to_be_guessed = random.randint(1, 100)
    # Getting number of guesses based on the difficulty level
    number_of_guesses = select_difficulty()

    while number_of_guesses > 0:
        # Taking user input as well as checking if it is the number or not
        user_input = int(input("\n\t\tGuess the number: "))
        # Comparing as well as getting the number of guesses
        number_of_guesses = compare_guesses(
            user_input, to_be_guessed, number_of_guesses)
        if number_of_guesses > 0:
            print(f"You have {number_of_guesses} guesses left!")
        elif number_of_guesses == 0:
            print("\n\t\tBetter luck next time!\n")


def main():
    """The main function of the program."""
    should_continue = True

    while should_continue:
        os.system('cls')
        print(art.logo)
        print("\n------------------------------------------Welcome to the Number Guesser "
              "Game!------------------------------------------")
        print('''Rules:
        1. There are two levels available(Hard and Easy)
        2. You have 5 lives to guess the number in hard level
        3. You have 10 lives to guess the number in easy level
        Choose your level accordingly and enjoyy the restt....''')

        # Calling the main logic
        guesser()

        continue_var = input("Do you want to play again?: 'y' or 'n': ")
        if continue_var == 'n':
            print("\n----------------------------Thank you for playing our game! Hope you enjoyed your time "
                  "here!----------------------------")
            should_continue = False
        elif continue_var == 'y':
            continue


if __name__ == '__main__':
    main()
