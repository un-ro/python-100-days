# Day 7 Challenge 2 - Hangman 2
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create a list of underscores the same length as the chosen word
display = []
for letter in chosen_word:
    display.append("_")

guess = input("Guess a letter: ").lower()

# Check if the guess is in the chosen word
# If it is, replace the underscore with the letter
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess

# Print the display
print(display)
