# Day 4 Project: Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

option = [rock, paper, scissors]

user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user not in [0, 1, 2]:
    print("Please enter a valid number.")
    exit()

print(option[user] + "\n")
cpu = random.randint(0, 2)
print(option[cpu] + "\n")

if user == cpu:
    print("It's a tie!")
elif user == 0:  # Rock
    if cpu == 1:
        # CPU Paper
        print("You lose! Paper covers Rock!")
    else:
        # CPU Scissors
        print("You win! Rock breaks Scissors!")
elif user == 1:  # Paper
    if cpu == 2:
        # CPU Scissors
        print("You lose! Scissors cuts Paper!")
    else:
        # CPU Rock
        print("You win! Paper covers Rock!")
elif user == 2:  # Scissors
    if cpu == 0:
        # CPU Rock
        print("You lose! Rock breaks Scissors!")
    else:
        # CPU Paper
        print("You win! Scissors cuts Paper!")
else:
    print("You didn't choose a valid option!")
