# Day 5 Project: Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("\nEasy Randomizer")
easy_password = ''
for i in range(nr_letters):
    easy_password += random.choice(letters)
for i in range(nr_symbols):
    easy_password += random.choice(symbols)
for i in range(nr_numbers):
    easy_password += random.choice(numbers)
print(f"{easy_password}\n")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print("Hard Randomizer")
hard_password = ''
for i in range(nr_letters):
    hard_password += random.choice(letters)
for i in range(nr_symbols):
    hard_password += random.choice(symbols)
for i in range(nr_numbers):
    hard_password += random.choice(numbers)

scrambled = random.sample(list(hard_password), len(hard_password))

for i in scrambled:
    print(i, end='')
