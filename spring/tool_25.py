from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import time


LANGUAGE = 'fr'
translations = {
    'fr': {
        'CryptMethod': 'Méthode de cryptage',
        'PathFileEncrypt': 'Chemin du fichier à crypter',
        'PasswdCrypt': 'Mot de passe pour le cryptage',
        'ErrorReadFile': 'Erreur lors de la lecture du fichier',
        'SaveFileEncrypt': 'Fichier crypté enregistré à',
        'ErrorEncryptFile': 'Erreur lors de l\'enregistrement du fichier crypté',
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

Title("File Encryptor")

def encrypt_file(file_content, password):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())

    iv = os.urandom(16)

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_content) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_content = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_file_content = salt + iv + encrypted_content
    return encrypted_file_content

try:
    Slow(f"""Déchiffreur de fichiers
    [{tr('CryptMethod')}]
    """)

    choice = input(f"{current_time_hour()} {tr('CryptMethod')} -> ")

    if choice not in ['1', '01']:
        ErrorChoice()

    file_path = input(f"{current_time_hour()} {tr('PathFileEncrypt')} -> ")
    password = input(f"{current_time_hour()} {tr('PasswdCrypt')} -> ")

    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
    except Exception as e:
        print(f"{current_time_hour()} {tr('ErrorReadFile')}: {e}")
        raise e

    encrypted_content = encrypt_file(file_content, password)
    if encrypted_content:
        try:
            output_directory = "1-Output/FileEncrypted"
            os.makedirs(output_directory, exist_ok=True)
            file_name = os.path.basename(file_path)
            encrypted_file_path = os.path.join(output_directory, f"{file_name}.enc")
            
            with open(encrypted_file_path, 'wb') as file:
                file.write(encrypted_content)
            
            print(f"{current_time_hour()} {tr('SaveFileEncrypt')} {encrypted_file_path}")
        except Exception as e:
            print(f"{current_time_hour()} {tr('ErrorEncryptFile')} {e}")

        Continue()
        Reset()
except Exception as e:
    Error(e)