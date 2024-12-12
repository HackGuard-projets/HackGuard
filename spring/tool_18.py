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
        raise ValueError("Vous devez sélectionner au moins un type de caractère.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Combien de caractères pour le mot de passe ? "))
        
        use_letters = input("Voulez-vous inclure des lettres ? (o/n) ").strip().lower() == 'o'
        use_digits = input("Voulez-vous inclure des chiffres ? (o/n) ").strip().lower() == 'o'
        use_specials = input("Voulez-vous inclure des caractères spéciaux ? (o/n) ").strip().lower() == 'o'
        
        password = generate_password(length, use_letters, use_digits, use_specials)
        print(f"Votre mot de passe généré est : {password}")

    except ValueError as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    main()
