import random
import string

def generate_password(length, use_letters, use_digits, use_specials):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters 
    if use_digits:
        characters += string.digits          
    if use_specials:
        characters += string.punctuation    

    if not characters:
        raise ValueError("You must select at least one type of character.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("How many characters for the password? "))
        
        use_letters = input("Do you want to include letters? (y/n) ").strip().lower() == 'y'
        use_digits = input("Do you want to include digits? (y/n) ").strip().lower() == 'y'
        use_specials = input("Do you want to include special characters? (y/n) ").strip().lower() == 'y'
        
        password = generate_password(length, use_letters, use_digits, use_specials)
        print(f"Your generated password is: {password}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
