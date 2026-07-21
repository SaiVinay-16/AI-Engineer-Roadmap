import random
import string

def generate_password(length):
    """Generate a random password of given length."""
    # Characters to choose from: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for password length
length = int(input("Enter the desired password length: "))
print("Generated Password:", generate_password(length))