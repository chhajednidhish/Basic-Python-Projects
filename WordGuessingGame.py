'''
In this game, there is a list of words present, out of which our interpreter will choose 1 random word. 
The user first has to input their names and then, will be asked to guess any alphabet. 
If the random word contains that alphabet, it will be shown as the output(with correct placement) 
else the program will ask you to guess another alphabet. 
User will be given 12 turns(can be changed accordingly) to guess the complete word.
'''

def generateRandomWords():
    ''' This function will generate a random word for the user to guess. '''
    import random
    wordsList = ['hello', 'karma', 'compass', 'python', 'code', 'editor']
    return random.choice(wordsList)

def gameLogic(randomWord):
    # Initializing variables
    chances = 12
    wordLength = len(randomWord)
    correctCount = 0
    guesses = ''
    
    while chances > 0:
        # If the current chance is the last chance i.e user fails to guess the word
        if chances == 1:
            print("Sorry! Better luck next time.\n\nThank you for playing our game.\n")
            chances -= 1
        else:   
            # If user guesses the whole word
            if correctCount == wordLength:
                print("Congratulations! You have guessed the word perfectly.\nWord was correctly guessed as", randomWord,"\n\nThank you for playing our game.\n")
                chances = 0
            
            else:
                userGuess = input("Guess an alphabet: ")
                # If user guesses an alphabet from the word
                if userGuess in randomWord:
                    # Adding the user guess to guesses
                    guesses += userGuess

                    # Guilty but yeh part ka logic joh ki actually main logic hai woh uthana pada online...
                    correctCount = 0
                    # Splitting the word in characters
                    for char in randomWord:
                        # If user has guessed the character, then it will print the character at the position because of for loop
                        if char in guesses:
                            correctCount += 1
                            print(char)
                        # Else it will only print dashes in place of characters not yet guessed
                        else:
                            print("-")

                # if user is unable to guess the alphabet
                else:
                    chances -= 1
                    print("Oops! Wrong guess.\nYou have", chances, "chances left.\n")

def main():
    # Initializing variables
    toBe_guessed = generateRandomWords()
    playerName = input("Enter your name: ")

    # Introducing game to the player
    print(f'''\nWelcome {playerName}! 
This is a word guessing game. You will get 12 chances to guess a word by guessing alphabets. 
All the best!\n''')

    # Calling the main game logic
    gameLogic(toBe_guessed)


if __name__ == "__main__":
    main()
