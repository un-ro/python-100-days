# Day 14: Higher Lower Game Project

import art
from game_data import data
from random import randint
from os import system

score = 0

def game():
    global score
    def scoring(num1, num2):
        global score
        if num1 > num2:
            score += 1
            system('clear')
            game()
        elif num1 == num2:
            score += 1
            system('clear')
            game()
        else:
            system('clear')
            print(f"You lose! total score: {score}")
            exit()

    print(art.logo)
    if score != 0:
        print(f"Your current score is: {score}")

    object_a = data[randint(0, len(data) - 1)]
    object_b = data[randint(0, len(data) - 1)]
    follower_a = object_a['follower_count']
    follower_b = object_b['follower_count']

    print(f"Debug purpose: First {object_a['follower_count']} | Second {object_b['follower_count']}")
    print(f"Compare A: {object_a['name']}, {object_a['description']}, from {object_a['country']}")

    print(art.vs)

    print(f"Against B: {object_b['name']}, {object_b['description']}, from {object_b['country']}")

    if input("Who has more followers? Type 'A' or 'B': ").lower() == 'a':
        scoring(follower_a, follower_b)
    else:
        scoring(follower_b, follower_a)

game()