# Day 13 Exercise: Debug Odd or Even Program

number = int(input("Which number do you want to check? "))

# Error, because using assignment operator (=) instead of comparison operator (==)
# if number % 2 = 0:

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
