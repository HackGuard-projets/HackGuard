import bcrypt
import hashlib
import base64
from hashlib import pbkdf2_hmac

def encrypt_password(choice, password):
    if choice in ['1', '01']:
        try:
            salt = bcrypt.gensalt()
            encrypted_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            return encrypted_password.decode('utf-8')
        except Exception as e:
            print(f"Error: {e}")
    elif choice in ['2', '02']:
        try:
            encrypted_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            return encrypted_password
        except Exception as e:
            print(f"Error: {e}")
    elif choice in ['3', '03']:
        try:
            encrypted_password = hashlib.sha1(password.encode('utf-8')).hexdigest()
            return encrypted_password
        except Exception as e:
            print(f"Error: {e}")
    elif choice in ['4', '04']:
        try:
            encrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            return encrypted_password
        except Exception as e:
            print(f"Error: {e}")
    elif choice in ['5', '05']:
        try:
            salt = "this_is_a_salt".encode('utf-8')
            encrypted_password = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
            return encrypted_password
        except Exception as e:
            print(f"Error: {e}")
    elif choice in ['6', '06']:
        try:
            encrypted_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
            return encrypted_password
        except Exception as e:
            print(f"Error: {e}")
    else:
        return None

def main():
    print("Password Encryption")
    print("""
    [01] -> BCRYPT
    [02] -> MD5
    [03] -> SHA-1
    [04] -> SHA-256
    [05] -> PBKDF2 (SHA-256)
    [06] -> Base64 Encode
    """)

    choice = input("Choose Encryption Method -> ")

    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        print("Invalid choice.")
        return

    password = input("Enter Password to Encrypt -> ")

    encrypted_password = encrypt_password(choice, password)
    if encrypted_password:
        print(f"Encrypted Password: {encrypted_password}")
        
        save_choice = input("Do you want to save the encrypted password? (y/n) -> ")
        
        if save_choice.lower() in ['y', 'yes']:
            file_name = input("Enter File Name (without extension) -> ")
            file_path = f"{file_name}.txt"
            try:
                with open(file_path, 'w') as file:
                    file.write(encrypted_password)
                print(f"Password saved to {file_path}")
            except Exception as e:
                print(f"Error saving password: {e}")

if __name__ == "__main__":
    main()
