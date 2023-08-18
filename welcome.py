def say_hello(name, city, state):
    new_name = " ".join(name)
    return f"Hello, {new_name}, Welcome to {city}, {state}"

x = say_hello(["bo", "bingus"], "city", "state")
print(x)