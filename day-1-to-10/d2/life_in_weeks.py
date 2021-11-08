# Day 2 Exercise: Life in Weeks

age = input("What is your current age? ")
rest_age = 90 - int(age)

months = rest_age * 12
weeks = rest_age * 52
days = rest_age * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
