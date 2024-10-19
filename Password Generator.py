import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by selecting random characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Main function
def password_generator():
    # Prompt the user for the desired password length
    length = int(input("Enter the desired length for the password: "))

    # Generate and display the password
    if length < 6:
        print("Password length should be at least 6 characters for better security.")
    else:
        password = generate_password(length)
        print(f"Your generated password is: {password}")

# Run the password generator
password_generator()
