# Day 7 Challenge: Hangman 4 - Keeping user lives

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for letter in chosen_word:
    display.append("_")

is_continue = True
while is_continue:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            display[index] = guess

    if guess not in chosen_word:
        lives -= 1

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

    if "_" not in display and lives > 0:
        print("You win!")
        is_continue = False
    elif lives == 0:
        print(f"You lose! choosen word is {chosen_word}")
        is_continue = False
