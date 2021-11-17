# Day 9 Project: Secret Auction Program

from art import logo
import os

is_repeat = True
auctions = {}

while is_repeat:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What\'s your bid?: $"))

    auctions[name] = bid

    is_repeat = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "yes"

highest_bidder = max(auctions, key=auctions.get)

for name, bid in auctions.items():
    if bid == auctions[highest_bidder]:
        print(f"{name} tied with {bid}")
