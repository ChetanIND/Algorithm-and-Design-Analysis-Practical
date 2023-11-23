import string
import random


def password_strength(password):
    strength = 0

    # Check the length of the password
    if len(password) < 8:
        return "Weak", generate_strong_password()

    # Check for at least one uppercase letter
    if any(char.isupper() for char in password):
        strength += 1

    # Check for at least one lowercase letter
    if any(char.islower() for char in password):
        strength += 1

    # Check for at least one digit
    if any(char.isdigit() for char in password):
        strength += 1

    # Check for at least one special character
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 1:
        return "Weak", generate_strong_password()
    elif strength == 2:
        return "Moderate", generate_strong_password()
    elif strength >= 3:
        return "Strong", password


def generate_strong_password():
    # Define character sets for each category
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a pool of characters for password generation
    pool = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate a strong password with a random combination of characters
    password_length = 12  # You can adjust the length as needed
    strong_password = "".join(random.choice(pool) for _ in range(password_length))

    return strong_password


# Main program
if __name__ == "__main__":
    user_password = input("Enter a password: ")
    strength, suggested_password = password_strength(user_password)

    if strength == "Weak":
        print("The password is weak. Here's a suggested strong password:")
        print(suggested_password)
    elif strength == "Moderate":
        print(
            "The password is of moderate strength. Here's a suggested strong password:"
        )
        print(suggested_password)
    else:
        print("The password is strong. Good job!")
