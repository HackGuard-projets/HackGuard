import subprocess
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    clear_console()
    print(Fore.MAGENTA + r"""
             _    _            _     _____                     _ 
            | |  | |          | |   / ____|                   | |
            | |__| | __ _  ___| | _| |  __ _   _  __ _ _ __ __| |
            |  __  |/ _` |/ __| |/ / | |_ | | | |/ _` | '__/ _` |
            | |  | | (_| | (__|   <| |__| | |_| | (_| | | | (_| |
            |_|  |_|\__,_|\___|_|\_\\_____|\__,_|\__,_|_|  \__,_| (By potopilo)

   ┌─────────────────────────────── Network Scanner ───────────────────────────────┐
   │ [1] Web Scanner                            [2] SQL Vulnerability              │
   │ [3] Website Info Scanner                   [4] Website URL Scanner            │
   │ [5] URL Checker                            [6] IP Scanner                     │
   │ [7] IP Port Scanner                        [8] IP Pinger                      │
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌────────────────────────────────── OSINT ──────────────────────────────────────┐
   │ [9] Have I Been Pwned                      [10] Username Tracker              │
   │ [11] Email Tracker                         [12] Email Info (No API)           │
   │ [13] Number Info                           [14] IP Info                       │
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────── Utilities ─────────────────────────────────────┐
   │ [15] Password Encrypted                    [16] Password Decrypted            │
   │ [17] Password Checker (HS for now)         [18] Password Generator            │
   │ [19] Random Password Generator             [20] Search in Database            │
   │ [21] IP Generator                          [0] Leave the Tools                │
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │ Press (B) to go Back                         Press (N) for Next               │
   └───────────────────────────────────────────────────────────────────────────────┘
"""+ Style.RESET_ALL)


def display_next_menu():
    clear_console()
    print(Fore.MAGENTA + r"""     
             _    _            _     _____                     _ 
            | |  | |          | |   / ____|                   | |
            | |__| | __ _  ___| | _| |  __ _   _  __ _ _ __ __| |
            |  __  |/ _` |/ __| |/ / | |_ | | | |/ _` | '__/ _` |
            | |  | | (_| | (__|   <| |__| | |_| | (_| | | | (_| |
            |_|  |_|\__,_|\___|_|\_\\_____|\__,_|\__,_|_|  \__,_| (By potopilo)

   ┌──────────────────────────────── Roblox Tools ─────────────────────────────────┐
   │                          [22] Roblox-Cookie-Info                              │
   │                          [23] Roblox-User-Info                                │
   │                          [24] Roblox-Id-Info                                  │
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────── File Tools ────────────────────────────────────┐
   │                          [25] File-Encryptor                                  │
   │                          [26] File-Decryptor                                  │
   │                          [27] File-Converter                                  │
   │                          [28] File-Scanner                                    │
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌───────────────────────────── System Tools ────────────────────────────────────┐
   │                          [29] Get-Your-IP                                     │                
   └───────────────────────────────────────────────────────────────────────────────┘

   ┌───────────────────────────────────────────────────────────────────────────────┐
   │ Press (B) to go Back                                 Press (N) for Next       │
   └───────────────────────────────────────────────────────────────────────────────┘
 """+ Style.RESET_ALL)

def main():
    current_menu = 'main'

    while True:
        if current_menu == 'main':
            display_main_menu()
            choice = input(Fore.YELLOW + "Choose an option (1-21, N for Next, B for Back): " + Style.RESET_ALL)

            if choice == 'N' or choice.lower() == 'n':
                current_menu = 'next'
            elif choice == 'B' or choice.lower() == 'b':
                print(Fore.RED + "You are already in the main menu.")
            elif choice == '0':
                print(Fore.RED + "Goodbye!")       
                break
            elif choice in [str(i) for i in range(1, 30)]: 
                subprocess.run(["python", os.path.join(os.path.dirname(__file__), "spring", f"tool_{choice}.py")])
            else:
                print(Fore.GREEN + "Invalid choice. Please enter a number between 1 and 29.")            

        elif current_menu == 'next':
            display_next_menu()
            choice = input(Fore.YELLOW + "Choose an option (22-29, 0 for Back): " + Style.RESET_ALL)

            if choice == 'B' or choice.lower() == 'b':
                current_menu = 'main'
            elif choice == '0':
                current_menu = 'main'
            elif choice in [str(i) for i in range(22, 30)]:  
                subprocess.run(["python", os.path.join(os.path.dirname(__file__), "spring", f"tool_{choice}.py")])
            else:
                print(Fore.GREEN + "Invalid choice. Please enter a number between 22 and 29.")

if __name__ == "__main__":
    main()
