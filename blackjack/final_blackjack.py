# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# #################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# importing required modules
import art
import random
import os


def deal_cards(score):
    '''Function to randomly distribute cards to players'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if score - cards[0] >= 0:
        cards[0] = 1
    return random.choice(cards)


def get_computer_hand():
    '''Function to get the final computer hand.'''
    # Declaring basic variables
    computer_score = 0
    computer_hand = []

    # Getting cards for computer untill it reaches a score of 16 or above...
    while computer_score <= 17:
        selected_card = deal_cards(computer_score)
        computer_hand.append(selected_card)
        computer_score += selected_card

    return computer_hand


def get_user_hand(user_cards, user_score, computer_cards):
    '''Function to get the user hand'''
    user_cards.append(deal_cards(user_score))
    user_score = sum(user_cards)
    print(f"\n\tYour cards: {user_cards}. \tCurrent score: {user_score}.")
    print(f"\tComputer's first card: {computer_cards[0]}.")

    return user_cards


def main_logic():
    # Declaring basic variables
    user_cards = []
    user_score = 0
    computer_cards = get_computer_hand()
    computer_score = sum(computer_cards)

    while user_score <= 21:
        if user_score == 0:
            user_cards.append(deal_cards(user_score))
            user_score = sum(user_cards)
            user_cards = get_user_hand(user_cards, user_score, computer_cards)
            user_score = sum(user_cards)
        else:
            get_more_cards = input(
                "\tType 'y' to get another card, type 'n' to pass: ")
            if get_more_cards == 'y':
                user_cards = get_user_hand(
                    user_cards, user_score, computer_cards)
                user_score = sum(user_cards)
            elif get_more_cards == 'n':
                break

    print("\n------------------------------------------------------------\n")
    print(f"\tYour final hand: {user_cards}.\n\tYour score: {user_score}.")
    print(
        f"\n\tComputer's final hand: {computer_cards}.\n\tComputer score: {computer_score}.")
    if user_score > 21:
        print("\nOops!!! You went over 21...Sorry you lose!")
    elif computer_score > 21:
        print("\n\tSince computer went over 21\n\tCongratulationsss! You win the bet!")
    else:
        if user_score > computer_score:
            print("\n\tCongratulationsss! You win the bet!")
        elif user_score == computer_score:
            print("\n\tDamn! Draw...")
        else:
            print("\n\tOops! You lose...")


def main():
    # Declaring basic variables
    want_to_play = True

    # If the user wants to play a game of BlackJack, clear screen and restart the game
    while want_to_play:

        play = input(
            "Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if play == 'y':
            os.system('cls')
            print(art.logo)
            main_logic()
            continue
        elif play == 'n':
            print(
                "\n---------------Thank you for playing our game. We hope you had fun---------------")
            want_to_play = False
        else:
            print("Invalid Input! Please try again...")
            break


if __name__ == "__main__":
    main()
