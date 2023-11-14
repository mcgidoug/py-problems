import time
import random

delay = 0.5
lower_alpha = "abcdefghijklmnopqrstuvwxyz"
upper_alpha = lower_alpha.upper()
numbers = '1234567890'
special_characters = '!@#$%^&*()-_=+;'
final_pass = ''

def pass_gen():
    new_pass = ''
    global final_pass

# length
    length_str = input('how long should your password be? ')
    if length_str.isdigit():
        length = int(length_str)
        print(f'your password will be {length} characters long ')
    else:
        print('please enter a valid number')
    time.sleep(delay)

# lower
    lower = input('would you like lowercase letters y/n? ')
    if lower == 'y':
        new_pass += lower_alpha
        print('your password will have lowercase letters ')
    elif lower == 'n':
        print('your password will not have lowercase letters')
    else: 
        print('please choose y or n')
    time.sleep(delay)

# upper
    upper = input('would you like uppercase letters y/n? ')
    if upper == 'y':
        new_pass += upper_alpha
        print('your password will have uppercase letters')
    elif upper == 'n':
        print('your password will not have uppercase letters')
    else:
        print('please choose y or n')
    time.sleep(delay)
    

# numbers
    include_numbers = input('would you like numbers y/n? ')
    if include_numbers == 'y':
        new_pass += numbers
        print('your password will have numbers')
    elif include_numbers == 'n':
        print('your password will not have numbers')
    else:
        print('please choose y or no')
    time.sleep(delay)

# special characters
    include_special_characters = input('would you like special characters y/n? ')
    if include_special_characters == 'y':
        new_pass += special_characters
        print('your password will have special characters')
    elif include_special_characters == 'n':
        print('your password will not have special characters')
    else:
        print('please choose y or n')
    time.sleep(delay)

# create password
    for _ in range(length):
        random_letter = random.choice(new_pass)
        final_pass += random_letter

    print(f'your password is: {final_pass}')

    
pass_gen()