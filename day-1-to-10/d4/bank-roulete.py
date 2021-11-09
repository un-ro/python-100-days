# Day 4 Exercise: Bank Roulette

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names_list = names_string.split(",")

print(f"{random.choice(names_list)} is going to buy the meal today")
