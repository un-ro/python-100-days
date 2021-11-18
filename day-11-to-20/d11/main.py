# Day 11 Capstone: The Blackjack Game

from art import logo
from os import system
from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
dealer_hand = []
is_retry = True


def draw_card(total):
    if total > 0:
        for i in range(total):
            user_hand.append(choice(cards))
    dealer_hand.append(choice(cards))


def check_score():
    if sum(user_hand) <= 17 and sum(dealer_hand) <= 17:
        if sum(user_hand) > sum(dealer_hand):
            print("You win! 😁🎉")
        else:
            print("You lose! 😭")
    elif not (sum(user_hand) > 21 or sum(dealer_hand) > 21) and sum(dealer_hand) > sum(user_hand):
        print("You lose! 😭")
    elif not (sum(user_hand) > 21 or sum(dealer_hand) > 21) and sum(dealer_hand) < sum(user_hand):
        print("You win! 😁🎉")
    elif sum(dealer_hand) > 21:
        print("You win! 😁🎉")
    elif sum(user_hand) > 21:
        print("You lose! 😭")
    elif sum(user_hand) == sum(dealer_hand):
        print("It\'s a tie! 😐")


def information(stage):
    if stage == 1:
        print(
            f"Your first card is {user_hand}. Current score is: {sum(user_hand)}")
        print(f"Computer\'s first card is {dealer_hand[0]}.\n")
    else:
        print(
            f"Your final card is {user_hand}. Final score is: {sum(user_hand)}")
        print(
            f"Computer\'s final card is {dealer_hand}.Final score is: {sum(dealer_hand)}")


def debug():
    print(f"""
    user_hand: {user_hand}
    dealer_hand: {dealer_hand}
    """)


def blackjack():
    draw_card(2)
    information(1)
    if input("Type 'y' to get another card, type'n' to pass: ").lower() == 'y':
        draw_card(1)
        information(0)
        check_score()
    else:
        draw_card(0)
        information(0)
        check_score()
    if input("Type 'y' to play again, type 'n' to exit: ").lower() == 'y':
        user_hand.clear()
        dealer_hand.clear()
        system('cls')
        print(logo)
        blackjack()


if input("Would you like to play a game? (y/n): ").lower() == "y":
    system('cls')
    print(logo)
    blackjack()
else:
    exit()
