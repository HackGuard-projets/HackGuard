import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


password = generate_password()
print(f"Your random password is: {password}")


input("\nPress Enter to exit...")
