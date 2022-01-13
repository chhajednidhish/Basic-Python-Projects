''' -------------------------------ATM command line---------------------------------------
Methods to be added- 
    pin authorization
    balance check
    withdrawal
    deposit funds
    return card
'''

import time

def passAuth(password):
    """ Returns true if the password matches with the user's password, else returns false."""
    if password == 9241:
        return True
    else:
        return False

def balanceCheck(initialBalance):
    print("Your current balance is: ", initialBalance)

def withdrawal(initialBalance):
    withdraw = int(input("How much money do you want to be removed?: "))
    if withdraw <= initialBalance-100 and withdraw >= 100:
        return initialBalance - withdraw
    else:
        print("You cannot withdraw this amount.")

def depositFunds(initialBalance):
    deposit = int(input("How much money do you want to deposit?: "))
    return initialBalance + deposit

def main():
    chances = 3
    initialBalance = 10000
    while chances>0: # Taking password inputs from the user for max 3 times, if wrong
        password = int(input("\nEnter your 4-digit password: "))
        if passAuth(password):
            print("Accepted")
            cont = "y"
            while cont == "y":
                print("Menu\n1.Press 1 for checking your balance.\n2.Press 2 for withdrawing cash\n3.Press 3 for depositing funds.\n4. Exit")
                choice = int(input("What do you want to do?: "))
                if choice == 1:
                    balanceCheck(initialBalance)
                elif choice == 2:
                    initialBalance = withdrawal(initialBalance)
                elif choice == 3:
                    initialBalance = depositFunds(initialBalance)
                elif choice == 4:
                    break
                else:
                    print("Wrong input!")  
            break
        else:
            chances = chances - 1
            if chances == 0:
                print("Sorry! Since you tried to unlock using wrong pin 3 times, you have been blocked to use the atm for a while.")
                time.sleep(20)
            else:
                print(f"You have entered wrong pin, please try again!\nYou have {chances} chance more.")                
    print("Thank you for using our ATM!")

if __name__ == "__main__":
    main()
