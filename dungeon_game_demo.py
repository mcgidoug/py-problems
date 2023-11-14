import random
import time


main_char = {
    "hp": 100,
    "dmg": 50
}

side_char = {
    "hp": 80,
    "dmg": 25
}

def battle_func():
    global main_char, side_char  # Declare variables as global to modify them
    user_input = input(f"You are about to go into battle, continue (y/n)? ")
    if user_input == "y":
        main_char["hp"] -= side_char["dmg"]
    else:
        response = input("Roll the die to escape (hit ENTER to roll).")
        die_roll = random.randint(1,20)
        print(f"You rolled a {die_roll}!")

battle_func()
