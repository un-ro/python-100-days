# Day 15 Project: The coffe machine

from os import system
from data import MENU, resources

def print_resource():
    print("The coffee machine has:")
    print(f"\t - {resources['water']}ml of water")
    print(f"\t - {resources['milk']}ml of milk")
    print(f"\t - {resources['coffee']}g of coffee beans")
    print(f"\t - ${resources['money']} of money")

def transaction(coffee_type):
    print("Making coffee...")
    for ingredient, quantity in MENU[coffee_type]['ingredients'].items():
        resources[ingredient] -= quantity
    print(f"Done! Enjoy your {coffee_type} ☕")
    print_resource()

def payment(coffee_type):
    print(f"Please pay for ${MENU[coffee_type]['cost']}")
    cost = MENU[coffee_type]['cost']

    quarter = int(input("Quarter $0.25: "))
    dime = int(input("Dime $0.10: "))
    nickel = int(input("Nickel $0.05: "))
    penny = int(input("Penny $0.01: "))

    total = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)
    
    if total < cost:
        print("Sorry, not enough money. Money refunded")
        return False
    elif total > cost:
        change = round(total - cost, 2)
        print("Thank you!")
        print(f"Your change is ${change}")
        resources['money'] += cost
        return True
    else:
        print("Thank you!")
        resources['money'] += cost
        return True

def check_resources(coffee_type):
    checkmark = []
    print("Checking resource first...")
    for ingredient, quantity in MENU[coffee_type]['ingredients'].items():
        if resources[ingredient] < quantity:
            print(f"Sorry, not enough {ingredient}")
            checkmark.append(False)
            return False
        else:
            checkmark.append(True)
    if False not in checkmark:
        return True
                
def make_request(coffee_type):
    if coffee_type not in MENU:
        print("Sorry, that coffee is not available")
        return False
    else:
        print(f"You picked {coffee_type}")
        return True
        

is_running = True

while is_running:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "off" or command == 'q':
        is_running = False
    elif command == "report":
        print_resource()
    else:
        if make_request(command):
            if check_resources(command):
                if payment(command):
                    transaction(command)



