# Day 4 Exercise: Head or Tails

import random
from time import sleep

print("A coin was tossed, Head or Tails ?")
sleep(3)
coin = random.randint(0, 1)
if coin == 0:
    print("Heads")
else:
    print("Tails")
