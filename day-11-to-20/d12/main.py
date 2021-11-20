# Day 12 Project: Guess the number

from art import logo
from random import randint

attempts = 0

def game():
    print(logo)
    print("Welcome to Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    number = randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # print(f"Debug: {number}")

    if difficulty == "easy":
        global attempts 
        attempts = 10
    else:
        attempts = 5
    
    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")
        guess = int(input("Take a guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"You got it! The answer was {number}")
            break
        attempts -= 1
    if attempts == 0:
        print("You lost!")

if __name__ == "__main__":
    game()