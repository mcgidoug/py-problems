def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError as e:
        print("Error:", e)
        print("Division by zero is not allowed.")
    except TypeError as e:
        print("Error:", e)
        print("Unsupported operation: division between a number and a string.")
    finally:
        print("This finally block always executes, regardless of exceptions.")

# Example calls to the function
divide_numbers(10, 2)  # This will work fine
divide_numbers(8, 0)   # This will cause a ZeroDivisionError
divide_numbers(8, "e")   # This will cause a TypeError