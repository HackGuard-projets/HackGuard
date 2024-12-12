import bcrypt
import hashlib
import random
import string
import threading
import time
import base64
from hashlib import pbkdf2_hmac

def check_password(password_test, encrypted_password, choice):
    salt = "this_is_a_salt".encode('utf-8')
    
    if choice in ['1', '01']:
        return bcrypt.checkpw(password_test.encode('utf-8'), encrypted_password.encode('utf-8'))
    elif choice in ['2', '02']:
        return hashlib.md5(password_test.encode('utf-8')).hexdigest() == encrypted_password
    elif choice in ['3', '03']:
        return hashlib.sha1(password_test.encode('utf-8')).hexdigest() == encrypted_password
    elif choice in ['4', '04']:
        return hashlib.sha256(password_test.encode('utf-8')).hexdigest() == encrypted_password
    elif choice in ['5', '05']:
        return pbkdf2_hmac('sha256', password_test.encode('utf-8'), salt, 100000).hex() == encrypted_password
    elif choice in ['6', '06']:
        return base64.b64decode(encrypted_password.encode('utf-8')).decode('utf-8') == password_test
    else:
        return False

def generate_password(characters_number):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(all_characters) for _ in range(random.randint(1, characters_number)))

def test_decrypted(encrypted_password, choice, characters_number, generated_passwords, password_found):
    while not password_found[0]:
        password_test = generate_password(characters_number)
        if password_test not in generated_passwords:
            generated_passwords.add(password_test)
            if check_password(password_test, encrypted_password, choice):
                password_found[0] = True
                print(f'Password found: {password_test}')
                time.sleep(1)

def request(encrypted_password, choice, threads_number, characters_number):
    threads = []
    password_found = [False]
    generated_passwords = set()

    for _ in range(threads_number):
        t = threading.Thread(target=test_decrypted, args=(encrypted_password, choice, characters_number, generated_passwords, password_found))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

def main():
    print("Password Decryption Options:")
    print("[01] BCRYPT")
    print("[02] MD5")
    print("[03] SHA-1")
    print("[04] SHA-256")
    print("[05] PBKDF2 (SHA-256)")
    print("[06] Base64 Decode")

    choice = input("Select Encryption Method: ")
    if choice not in ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06']:
        print("Invalid choice.")
        return

    encrypted_password = input("Enter Encrypted Password: ")
    threads_number = int(input("Enter Number of Threads: "))
    characters_number = int(input("Enter Maximum Password Length: "))

    print(f"Starting password decryption for: {encrypted_password}")
    request(encrypted_password, choice, threads_number, characters_number)

if __name__ == "__main__":
    main()
