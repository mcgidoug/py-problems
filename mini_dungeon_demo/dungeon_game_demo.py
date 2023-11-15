import random
import time
from characters import main_char, side_char



def battle_func():
    global main_char, side_char  # Declare variables as global to modify them
    user_input = input(f"You are about to go into battle, continue (y/n)? ")
    if user_input == "y":
        main_char["hp"] -= side_char["dmg"]
    else:
        response = input("Roll the die to escape (hit ENTER to roll).")
        die_roll = random.randint(1,20)
        print(f"You rolled a {die_roll}!")
        if die_roll > 10:
            print("You successfully escaped!")
        else: 
            main_char["hp"] -= 5
            print(f"You were not successful in escaping... hp now at {main_char["hp"]}")

battle_func()
