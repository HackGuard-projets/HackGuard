from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64
import time


LANGUAGE = 'fr' 
translations = {
    'fr': {
        'DecryptFile': 'Déchiffrer le fichier',
        'Chose': 'Choisissez',
        'PathToDecrypt': 'Chemin du fichier à déchiffrer',
        'PasswdForDecrypt': 'Mot de passe pour déchiffrer',
        'ErrorReadFile': 'Erreur lors de la lecture du fichier',
        'DecryptedContent': 'Contenu déchiffré enregistré à',
        'ErrorDecrypt': 'Erreur lors du déchiffrement',
    }
}

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def current_time_hour():
    return time.strftime("%H:%M:%S")

def ErrorModule(e):
    print(f"Erreur de module: {e}")

def ErrorChoice():
    print("Choix invalide.")

def Error(e):
    print(f"Erreur: {e}")

def Slow(message):
    print(message)
    time.sleep(1)

def Title(message):
    print(f"=== {message} ===")

def Continue():
    input("Appuyez sur Entrée pour continuer...")

def Reset():
    print("Réinitialisation des paramètres...")

Title("File Decryptor")

def decrypt_file(encrypted_file_content, password):
    salt = encrypted_file_content[:16]
    iv = encrypted_file_content[16:32]
    encrypted_content = encrypted_file_content[32:]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_content) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

try:
    Slow(f"""Déchiffreur de fichiers
    [{tr('DecryptFile')}]
    """)

    choice = input(f"{current_time_hour()} {tr('Chose')} -> ")

    if choice not in ['1', '01']:
        ErrorChoice()

    file_path = input(f"{current_time_hour()} {tr('PathToDecrypt')} -> ")
    password = input(f"{current_time_hour()} {tr('PasswdForDecrypt')} -> ")

    try:
        with open(file_path, 'rb') as file:
            encrypted_file_content = file.read()
    except Exception as e:
        print(f"{current_time_hour()} {tr('ErrorReadFile')}: {e}")
        raise e

    try:
        decrypted_content = decrypt_file(encrypted_file_content, password)
        output_directory = "1-Output/FileDecrypted"
        os.makedirs(output_directory, exist_ok=True)
        file_name = os.path.basename(file_path)
        decrypted_file_path = os.path.join(output_directory, file_name.replace('.enc', ''))
        
        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_content)
        
        print(f"{current_time_hour()} {tr('DecryptedContent')} {decrypted_file_path}")
    except Exception as e:
        print(f"{current_time_hour()} {tr('ErrorDecrypt')} {e}")

    Continue()
    Reset()
except Exception as e:
    Error(e)