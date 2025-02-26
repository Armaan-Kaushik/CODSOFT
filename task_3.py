import random
import string

def create_password():
    print("Password Generator")
    
    password_length = int(input("Enter the desired password length: "))
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    new_password = ''.join(random.choice(all_characters) for _ in range(password_length))
    
    print("Generated Password:", new_password)

if __name__ == "__main__":
    create_password()