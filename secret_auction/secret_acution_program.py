""" 
Instructions:
The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually. 

```
Welcome to the secret auction program. 
What is your name?: Angela
```
```
What's your bid?: $123
```
```
Are there any other bidders? Type 'yes' or 'no'.
yes

```
If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.  
"""
# Importing required modules
import art
import os
from time import sleep


def get_bid():
    # Greeting every user
    print("Welcome to secret auction program!\n")

    # Taking inputs
    bidder_name = input("What is your name?: ")
    bidder_amount = int(input("What's your bid?: ₹"))

    # Clearing screen for the next user
    sleep(1)

    return bidder_name, bidder_amount


def get_highest_bid(bidders_list):
    highest_bid = 0
    highest_bidder = ''
    
    for bidder in bidders_list:
        if bidders_list[bidder] >= highest_bid:
            highest_bidder = bidder
            highest_bid = bidders_list[bidder]

    return highest_bidder, highest_bid



def secret_auction():
    # Initializing variables
    bidders_exist = True
    bidders_list = {}

    while bidders_exist:
        # Obtaining inputs and adding the same to dictionary
        bidder_name, bid_amount = get_bid()
        bidders_list[bidder_name] = bid_amount

        more_bids = input(
            "Are there any other bidders? Type 'yes' or 'no': ").lower()
        os.system('clear')
        if more_bids == "no":
            # to discontinue the loop
            bidders_exist = False

            # Finding and printing details about highest bidder...
            highest_bidder_name, highest_bidder_amount = get_highest_bid(bidders_list)
            print(f"\n```````````````````Highest Bid is of {highest_bidder_name} for an amount of ₹{highest_bidder_amount}.`````````````````````````` \n```````````````````Congratulations {highest_bidder_name}! You win the auction!``````````````````````````\n")

            break


def main():
    # calling the main function
    secret_auction()


if __name__ == '__main__':
    print(art.logo)
    main()
