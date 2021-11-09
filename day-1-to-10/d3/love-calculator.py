# Day 3 Exercise: Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower().replace(" ", "")
name2 = input("What is their name? \n").lower().replace(" ", "")

combined_names = name1 + name2

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

love_score = str(t + r + u + e) + str(l + o + v + e)
love_score = int(love_score)

if love_score <= 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are right together")
else:
    print("Your score is ", love_score)
