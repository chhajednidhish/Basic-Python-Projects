'''
Small intro to the game by ChatGPT AI
This code is a script that plays the game of Hangman. Hangman is a guessing game where a player attempts to guess a word by guessing one letter at a time. In this version of the game, the script imports two modules hangman_art and hangman_words, which contain the ASCII art for the hangman and a list of words to be used in the game respectively. The script defines several functions:

create_blanks(word_length) returns a list of "_" characters with length equals to the length of the word to be guessed.
main_logic(chosen_word) is the core logic of the game, it takes a word as an input. The function initializes some variables, such as word_length, end_of_game, lives, display, game_result. Then, it enters a loop which continues until the game is over. In each iteration of the loop, the user is prompted to guess a letter, which is then checked against the chosen word. If the letter is in the word, it replaces the corresponding "_" character in the display variable. If the letter is not in the word, the lives variable is decremented by 1. If the user runs out of lives, the game is over and the game_result variable is set to "You lose.". If the user correctly guesses all the letters in the word, the game is over and the game_result variable is set to "You win.".
main() is the entry point of the script, it generates a random word from the word_list, calls the main_logic() function and prints the game result and the chosen word.
It also includes an if __name__ == '__main__': block which runs the main() function when the script is executed.
'''

# Importing required modules
import random
import hangman_art
import hangman_words

def create_blanks(word_length):
    display = []
    for _ in range(word_length):
        display += "_"

    return display

def main_logic(chosen_word):
    # declaring basic variables
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6
    display = create_blanks(word_length)
    game_result = "You win."

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        # If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print(f"You've already guessed {guess}")

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            #  If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(
                f"You've guessed {guess}, that's not in the word. You lose a life")
            lives -= 1
            if lives == 0:
                end_of_game = True
                game_result = "You lose."

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            game_result = "You win."

        # Displaying stages of hangman
        print(hangman_art.stages[lives])

    return game_result

def main():
    # Beautifying output by adding Hangman logo
    print(hangman_art.logo)

    # Declaring basic variables
    chosen_word = random.choice(hangman_words.word_list)
    game_result = main_logic(chosen_word)

    print(game_result + f"The word was {chosen_word}")

if __name__ == '__main__':
    main()








