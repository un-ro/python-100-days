# Day 3: Treasure Island

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice_direction = input("left or right ? ")

if choice_direction == "right":
    print("Fall into a hole. Game Over.")
else:
    choice_action = input("swim or wait ? ")
    if choice_action == "swim":
        print("Attacked by trout. Game Over.")
    else:
        choice_door = input("Which door (red, blue, yellow, green) ? ")
        if choice_door == "red":
            print("Burned by fire. Game Over.")
        elif choice_door == "blue":
            print("Eaten by beasts. Game Over.")
        elif choice_door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
