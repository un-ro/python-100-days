# Tip Calculator
# Learn: Data Types, Operators, and String Formatting

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip_percent = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
bill_per_person = total_bill / people
print(f"Each person should pay: ${round(bill_per_person, 2)}")
