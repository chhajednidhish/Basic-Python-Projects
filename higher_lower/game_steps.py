"""
-----------------------------Higher Or Lower-----------------------------
Inspiration: 
This game is basically inspired from the online higher or lower game, in which the user can play the game and guess the number of searches for a particular topic. 

Basic Rules:- 
If the guessed answer (only 2 options, higher or lower), is right, your score will be incremented by 1, and the game continues ahead. Otherwise the game is over, and final score is displayed. 
Here if you guess the correct one, you have to compare the next one to this one's number of guesses. 

Modification:
Here instead of searches, we are comparing the number of followers. 

Example output:
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Ellen DeGeneres, a Comedian, from United States.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Jennifer Lopez, a Musician and actress, from United States.
Who has more followers? Type 'A' or 'B':

If right:
  / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

You're right! Current score: 1. --- the change
Compare A: Beyoncé, a Musician, from United States.

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: 9GAG, a Social media platform, from China.
Who has more followers? Type 'A' or 'B':
"""

'''
Steps to be performed:- 
1. Import random, data.py, and logo.py

3. Define game_logic() - 
Define the initial score as zero. (in game_logic())
4. Define continue_game = True

5. Create select_random()
You can select random number using randint from 0 to len(data) and print details about the same using list and dictionaries methods.
return the following data - name, follower_count, description, country as a dictionary

6. While continue_game:
    print logo
    8. If the initial score is zero, 
        7. Randomly select one person/one data entry from the list of data. (make a function for the same select_random()) (in game_logic()) - save as p1 dictionary
        select one more person/one data entry. (using select_random()) (in game_logic()) - save as p2 dictionary
    9. If score >=1 : 
        Display the foll - You're right! Your current score is : score
        Display the initial person/one data entry. (in game_logic())
        Select one more person/one data entry. (in game_logic()) save as p2 dictionary
    10. Print 1st person/one data entry --> print vs logo --> print second one person/data entry. (in game_logic())
    11. Take user input for selecting higher or lower. (in game_logic())
    12. If the answer is right, 
        increment the score by 1 (in game_logic())
        person 1 = person 2
        person 2 = {}
    13. If the answer is wrong,
        continue_game = False
        clear screen 
        print logo
        print - Sorry, that's wrong. Final score: 1

    
'''

# Step 1. Import random, data.py, and logo.py

# Step 8: Create select_random()




import random
import data
import art
import os
def select_random():
    # Step 9: You can select random number using randint from 0 to len(data) and print details about the same using list and dictionaries methods.
    # print(len(data.data))
    selected_index = random.randint(0, len(data.data) - 1)
    # print(selected_index)
    selected_person = data.data[selected_index]

    # Step 10:return the following data - name, follower_count, description, country as a dictionary
    return selected_person

# print(select_random())


# Step 2: Define game_logic() -
def game_logic():
    # Step 3: Define the initial score as zero, person1 and person2 variables (in game_logic())
    score = 0
    person1 = {}
    person2 = {}

    # Step 4: Define continue_game = True
    continue_game = True

    # Step 5: While continue_game:
    while continue_game:
        os.system('cls')
        # Step 6: print logo
        print(art.logo)

        # Step 7: If the initial score is zero,
        if score == 0:
            # Step 11: Randomly select one person/one data entry from the list of data. (make a function for the same select_random()) (in game_logic()) - save as p1 dictionary
            person1 = select_random()

            # Step12: select one more person/one data entry. (using select_random()) (in game_logic()) - save as p2 dictionary
            person2 = select_random()

        # Step 13: If score >=1 :
        if score >= 1:
            # Display the foll - You're right! Your current score is : score
            print(f"You're right! Your current score is: {score}")
            # Select one more person/one data entry. (in game_logic()) save as p2 dictionary
            person2 = select_random()

        # Step 14: Print 1st person/one data entry --> print vs logo --> print second one person/data entry. (in game_logic())
        print("Compare A: " + person1['name'] + ", " + person1['description'] +
              ", from " + person1['country'] + str(person1['follower_count']))
        print(art.vs)
        print("Compare B: " + person2['name'] + ", " + person2['description'] +
              ", from " + person2['country'] + str(person2['follower_count']))

        # Step 15: Compare number of followers of A and B, if A>B, compare_var = 1 else compare_var = 0
        compare_var = 0
        if person1['follower_count'] >= person2['follower_count']:
            compare_var = 1
        else:
            compare_var = 0

        # Step 16: Take user input for selecting higher or lower. (in game_logic())
        user_guess = input("Who has more followers? Type 'A' or 'B': ")
        user_compare_var = 0
        if user_guess == 'A':
            user_compare_var = 1
        else:
            user_compare_var = 0

        # Step 17: If the answer is right,
        if user_compare_var == compare_var:
            # increment the score by 1 (in game_logic())
            # person 1 = person 2
            # person 2 = {}
            score += 1
            person1 = person2
            person2 = {}

        # Step 18: If the answer is wrong,
        else:
            # continue_game = False
            # clear screen
            # print logo
            # print - Sorry, that's wrong. Final score: 1
            continue_game = False
            os.system('cls')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")


def main():
    game_logic()


if __name__ == '__main__':
    main()
