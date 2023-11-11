import random

my_str = "abcdefg"
final_pass = ''
# create password
def create_random():
    length = 5  
    global final_pass
    for _ in range(5):
        random_letter = random.choice(my_str)
        final_pass = final_pass + random_letter
        print(final_pass)

create_random()

print("Generated password:", final_pass)
