import hashlib
from colorama import init, Fore, Style
import os

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    hash_func = hashlib.new(hash_algorithm)
    
    try:
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_func.update(chunk)
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(Fore.RED + f"Error reading the file: {e}")
        return None

    return hash_func.hexdigest()

def main():
    clear_console()
    print(Fore.BLUE + Style.BRIGHT + "=== File Hash Checker ===")
    

    file_path = input(Fore.BLUE + "Enter the path of the file to check: ")
    expected_hash = input(Fore.BLUE + "Enter the expected hash: ")
    
    calculated_hash = calculate_file_hash(file_path)
    
    if calculated_hash is not None:
        print(Fore.BLUE + "Calculated hash: " + Fore.GREEN + calculated_hash)
        print(Fore.BLUE + "Expected hash: " + Fore.GREEN + expected_hash)
        
        if calculated_hash == expected_hash:
            print(Fore.GREEN + "The file is intact.")
        else:
            print(Fore.RED + "The file has been modified or is corrupted.")
    
    input(Fore.BLUE + "Press Enter to exit...")

if __name__ == "__main__":
    main()
