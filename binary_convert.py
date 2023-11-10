def convert_to_binary(n):
    binary_string = bin(n)[2:] #removes the "0b" prefix\
    return binary_string

decimal_number = 45
binary_number = convert_to_binary(decimal_number)
print(binary_number)