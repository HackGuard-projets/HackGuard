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

   ┌─────────────────────────────── File and System Tools ───────────────────────────────┐
   │ [1] File Hash Checker                     [2] Network Traffic Monitor               │
   │ [3] Wi-Fi Scanner                         [4] Port Knocking Tool                    │
   │ [5] DNS Lookup Tool                       [6] SSL Certificate Checker               │
   │ [7] Malware Scanner                       [8] Social Media Scraper                  │
   │ [9] Geolocation Tool                      [10] System Resource Monitor              │
   └─────────────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────── Network and Security Tools ──────────────────────────┐
   │ [11] Network Speed Test                   [12] IP Geolocation API                   │
   │ [13] Vulnerability Scanner                [14] Packet Sniffer                       │
   │ [15] Firewall Configuration Tool          [16] Log Analyzer                         │
   │ [17] Phishing Detection Tool              [18] Browser Fingerprinting Tool          │
   │ [19] Credential Stuffing Tool             [20] API Testing Tool                     │
   └─────────────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────── Data and Recovery Tools ─────────────────────────────┐
   │ [21] Data Breach Checker                  [22] File Integrity Checker               │
   │ [23] RAT Simulator                        [24] WAF Tester                           │
   │ [25] Cryptography Tool                    [26] CLI Tool                             │
   │ [27] Data Recovery Tool                   [28] Backup Tool                          │
   │ [29] System Information Tool              [30] User Account Management Tool         │
   └─────────────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────── Mapping and Intelligence Tools ──────────────────────┐
   │ [31] Network Mapping Tool                 [32] Incident Response Tool               │
   │ [33] Threat Intelligence Tool             [34] Web Scraper                          │
   │ [35] Digital Forensics Tool               [36] Privacy Checker                      │
   │ [37] Email Spoofing Tester                [38] Data Encryption Tool                 │
   │ [39] Network Configuration Tool           [40] User Activity Monitor                │
   └─────────────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────────────────────────────────────────────┐
   │ Press (B) to go Back                                             Press (N) for Next │
   └─────────────────────────────────────────────────────────────────────────────────────┘
"""+ Style.RESET_ALL)


def display_next_menu():
    clear_console()
    print("No other menu for moment !")

def main():
    current_menu = 'main'

    while True:
        if current_menu == 'main':
            display_main_menu()
            choice = input(Fore.YELLOW + "Choose an option (1-40, N for Next, B for Back): " + Style.RESET_ALL)

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
            choice = input(Fore.YELLOW + "No menu (press B or b) " + Style.RESET_ALL)

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
