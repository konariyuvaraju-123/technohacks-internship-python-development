import random
import string

def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits
    # Generate a password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    #random.choice function chooses the each character from the prefer set characters at a 
    # time till the length of the password 
    return password

# Prompt the user for the desired password length
length = int(input("Enter the length of the password: "))

# Generate the password
password = generate_password(length)
print("Generated Password:", password)