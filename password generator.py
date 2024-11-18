import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets based on parameters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""
    
    # Combine all chosen character sets
    all_characters = lowercase + uppercase + digits + special

    # Ensure we have characters to choose from
    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Generate password with random choices from the combined character set
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Main program to take user inputs and generate a password
def main():
    try:
        length = int(input("Enter password length (default is 12): ") or 12)
        use_uppercase = input("Include uppercase letters? (y/n, default is y): ").lower() != 'n'
        use_digits = input("Include numbers? (y/n, default is y): ").lower() != 'n'
        use_special = input("Include special characters? (y/n, default is y): ").lower() != 'n'

        # Generate and display the password
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print("Generated password:", password)

    except ValueError:
        print("Please enter a valid number for length.")

# Run the password generator
main()
