import random

def guess_word(word_list):
    secret_word = random.choice(word_list)
    guessed = False
    attempts = 0

    while not guessed:
        print("Attempts:", attempts)
        print("Guessing...")

        guessed_word = random.choice(word_list)
        print("Computer guesses:", guessed_word)

        if guessed_word == secret_word:
            print("Computer guessed the word:", secret_word)
            guessed = True
        else:
            print("Incorrect guess. Trying again...")
            attempts += 1

    print("Total attempts made:", attempts + 1)

# Example word list
words = ["apple", "banana", "orange", "grape", "kiwi", "melon"]

# Start the game
guess_word(words)
