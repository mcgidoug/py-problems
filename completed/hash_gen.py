import hashlib

def generate_hash_from_input(input):
    user_input = input("Enter your input: ")
    
    # Encode the input string before hashing (using UTF-8 encoding)
    encoded_input = user_input.encode('utf-8')
    
    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256(encoded_input)
    
    # Get the hexadecimal representation of the hash
    generated_hash = hash_object.hexdigest()
    
    return generated_hash

print(generate_hash_from_input(input))

# hello => 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824