# Day 9 - Blind Auction Project
# 100 Days of Python - Zero to Hero

from replit import clear
# If you're on VS Code, use this instead of above line:
# import os
# def clear(): os.system('cls' if os.name == 'nt' else 'clear')

logo = '''
                         ___________
                         \\ /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          | | | | | | ''-.
                          | |_| |_ _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                      .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Secret Auction Program.")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()