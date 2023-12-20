x = "hello"

def user_input(x):
    guesses = 4
    while True:
        user_input = input("Guess the password: ")
        if user_input.lower() == 'password':
            print("That's correct!")
            break  
        else:
            guesses -= 1
            print(f"Incorrect... you have {guesses} left")
            if guesses == 0:
                print("Out of guesses. Goodbye.")
                break

user_input(x)
