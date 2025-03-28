# password generator

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    # Ensure valid password length input
    while True:
        try:
            length = int(input("Enter password length (between 4 and 12): "))
            if 4 <= length <= 12:
                break  # Valid input
            else:
                print("Error: Password length must be between 4 and 12. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 4 and 12.")

    # Keep generating passwords until user is satisfied
    while True:
        password = generate_password(length)
        print("Generated Password:", password)
        
        retry = input("Do you like this password? (yes to accept / no to retry): ").strip().lower()
        if retry == "yes":
            print("Final Password:", password)
            break  # Exit loop when user is satisfied
