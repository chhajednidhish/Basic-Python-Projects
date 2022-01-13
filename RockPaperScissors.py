''' --------------------------------------------------------Rock Paper Scissors-------------------------------------------------------
Using random.choice, select one from rock paper or scissors
Then give user chance to select from rock paper or scissors
Select the winner in accordance to the rules of the game
User has total 10 chances, using while loop. '''

# Importing random variable for selecting the cpu's choice
import random

def gameLogic(compChoice, userChoice):
    """ This is the main game logic function which takes computers choice and user's choice as input.
    This function can retrun three variables based on status of winning, losing or tie."""
    #If computer chooses rock
    if compChoice == 'r': 
        if userChoice == 'r':           # If user too selects rock then it is a tie
            return 't' 
        elif userChoice == 'p':         # If user selects paper then user wins
            return 'w'
        elif userChoice == 's':         # If user selects scissor then user looses
            return 'l' 
        else:
            print("Invalid Choice!")
    #If computer chooses paper
    elif compChoice == 'p':
        if userChoice == 'r':           # If user selects rock then the user looses
            return 'l' 
        elif userChoice == 'p':         # If user too selects paper then it is a tie
            return 't' 
        elif userChoice == 's':         # If user selects scissors then the user wins
            return 'w' 
        else:
            print("Invalid Choice!")
    #If computer chooses scissors
    elif compChoice == 's':
        if userChoice == 'r':            # If user selects rock then the user wins
            return 'w' 
        elif userChoice == 'p':          # If user selects paper then the user looses
            return 'l' 
        elif userChoice == 's':          # If user too selects scissors then it is a tie
            return 't' 
        else:
            print("Invalid Choice!")
    else:
        print("Kuch toh gadbad hai bhaiya!")

def main():
    print("""-----------------------------------Rock Paper Scissors-------------------------------------
Rules:
You have to choose options between rock paper and scissors.
    Rock wins over scissors but looses to paper
    Paper wins over rock but looses to scissors
    Scissors wins over paper but looses to rock
You can play the game for 10 times, and whoever wins between you and cpu the most will be declared as the final winner.""")

    # Initializing variables 
    playCount = 10
    result = 'w'
    userScore = 0
    cpuScore = 0

    # Using while to let user play game for 10 times
    while playCount > 0:
        userChoice = input("\nOptions...\nr for Rock\np for Paper\ns for Scissor\nEnter your choice: ")
        userChoice.lower() # If user enters capital letters instead of lower letters
        cpuChoice = random.choice(["r","p","s"]) # Generating cpu choice
        result = gameLogic(cpuChoice, userChoice) # Getting the result using cpu choice and user choice
        playCount = playCount - 1
        if playCount == 0:
            # After all the chances of the user are over
            if userScore>cpuScore:
                print("\nCongratulations you won the game!\nThank you so much for playing my game.")
            elif userScore<cpuScore:
                print("\nSorry you lost. Better luck next time!\nThank you for playing my game.")
            elif userScore == cpuScore:
                print("\nHaha! It is a tie.\nThank you for playing my game.")
            else:
                print("Invalid.")
        else:
            # Untill user has chances to play
            if result == 'w':  # If user wins
                userScore = userScore + 1
                print(f"Congratulations! You won this round.\nMore {playCount} rounds to go.")   
            elif result == 'l': # If user looses
                cpuScore = cpuScore + 1
                print(f"Oops! Try again in the next round.\nMore {playCount} rounds to go.")    
            elif result == 't': # If it is a tie
                print(f"Haha! It is a tie.\nMore {playCount} rounds to go.") 
            else:
                print("Wrong input.")

if __name__ == "__main__":
    main()