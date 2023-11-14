string = "hello"

def count_letters(string):
    count = 0
    for letter in string:
        if letter == "l":
            count += 1
    return count

result = count_letters(string)
print(result)