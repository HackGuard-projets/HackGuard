import re
import os
import sys

def load_common_passwords(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        input("Press Enter to exit...")
        sys.exit(1)
    with open(file_path, 'r') as file:
        common_passwords = file.read().splitlines()
    return common_passwords

def load_dictionary(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        input("Press Enter to exit...")
        sys.exit(1)
    with open(file_path, 'r') as file:
        dictionary_words = file.read().splitlines()
    return dictionary_words

def has_repetitive_or_sequential_patterns(password):
    return re.search(r'(.)\1{2,}', password) or re.search(r'012|123|234|345|456|567|678|789|890', password)

def has_sequential_characters(password):
    sequences = [
        'abcdefghijklmnopqrstuvwxyz',
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        '0123456789',
        'qwertyuiop',
        'asdfghjkl',
        'zxcvbnm',
        'QWERTYUIOP',
        'ASDFGHJKL',
        'ZXCVBNM'
    ]
    for seq in sequences:
        if any(seq[i:i+3] in password for i in range(len(seq)-2)):
            return True
    return False

def evaluate_password_strength(password, common_passwords, dictionary_words):
    length_score = len(password) * 1.5
    upper_case_score = len(re.findall(r'[A-Z]', password)) * 1.5
    lower_case_score = len(re.findall(r'[a-z]', password)) * 1
    digit_score = len(re.findall(r'\d', password)) * 1.5
    special_char_score = len(re.findall(r'[\W_]', password)) * 2
    
    total_score = length_score + upper_case_score + lower_case_score + digit_score + special_char_score
    
    if password in common_passwords:
        total_score -= 40 
    if password.lower() in dictionary_words:
        total_score -= 25  
    if has_repetitive_or_sequential_patterns(password):
        total_score -= 20  
    if has_sequential_characters(password):
        total_score -= 20  
    if len(password) < 8:
        total_score -= 20  
    max_score = 100
    score_percentage = min(max(total_score, 0), max_score)
    
    if score_percentage < 20:
        strength = 'Weak'
        color = 'Red'
    elif score_percentage < 50:
        strength = 'Medium'
        color = 'Orange'
    else:
        strength = 'Strong'
        color = 'Green'
    
    return strength, color, score_percentage

def estimate_brute_force_time(password):
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[\W_]', password):
        charset_size += 32
    
    num_combinations = charset_size ** len(password)
    checks_per_second = 1_000_000_000
    time_to_crack_seconds = num_combinations / checks_per_second
    
    time_to_crack = {
        'seconds': time_to_crack_seconds,
        'minutes': time_to_crack_seconds / 60,
        'hours': time_to_crack_seconds / 3600,
        'days': time_to_crack_seconds / 86400,
        'years': time_to_crack_seconds / 31_536_000
    }
    
    return time_to_crack

def display_progress_bar(percentage):
    bar_length = 50
    filled_length = int(bar_length * percentage // 100)
    
    if percentage < 20:
        color = '\033[91m' 
    elif percentage < 50:
        color = '\033[93m' 
    else:
        color = '\033[92m' 
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    return f'{color}|{bar}| {percentage:.0f}%\033[0m'

def main():
    default_common_passwords_file = 'common_passwords.txt'
    default_dictionary_file = 'dictionary.txt'
    
    common_passwords_file = sys.argv[1] if len(sys.argv) >  1 else default_common_passwords_file
    dictionary_file = sys.argv[2] if len(sys.argv) > 2 else default_dictionary_file
    
    common_passwords = load_common_passwords(common_passwords_file)
    dictionary_words = load_dictionary(dictionary_file)
    
    password = input("Enter password to evaluate: ")
    
    strength, color, score_percentage = evaluate_password_strength(password, common_passwords, dictionary_words)
    time_to_crack = estimate_brute_force_time(password)
    
    print(f"\nPassword Strength: {strength}")
    print(display_progress_bar(score_percentage))
    print("\nEstimated Time to Crack:")
    for unit, time in time_to_crack.items():
        print(f"{unit.capitalize()}: {time:.2e}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
