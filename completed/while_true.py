x = "hello"

def user_input(x):
    while True:
        user_input = input("Enter 'exit' to break the loop: ")
        if user_input.lower() == 'exit':
            break  
        else:
            print("Looping...")

user_input(x)
