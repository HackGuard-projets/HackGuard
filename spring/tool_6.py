import socket
import ssl
import os
import time
import threading
from colorama import init, Fore, Style

init(autoreset=True)

exit_program = False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_exit():
    global exit_program
    input(Fore.BLUE + "Press Enter to exit at any time...")
    exit_program = True

class SSLCertificateChecker:
    def __init__(self, domain):
        self.domain = domain

    def check_certificate(self):
        try:
            context = ssl.create_default_context()
            with socket.create_connection((self.domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=self.domain) as ssock:
                    cert = ssock.getpeercert()
                    print(Fore.GREEN + f"Certificate for {self.domain}:")
                    print(Fore.YELLOW + f"  Subject: {cert['subject']}")
                    print(Fore.YELLOW + f"  Issuer: {cert['issuer']}")
                    print(Fore.YELLOW + f"  Valid from: {cert['notBefore']}")
                    print(Fore.YELLOW + f"  Valid until: {cert['notAfter']}")
        except ssl.SSLError as e:
            print(Fore.RED + f"SSL error: {e}")
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")

def main():
    global exit_program
    clear_console()
    print(Fore.BLUE + Style.BRIGHT + "=== SSL Certificate Checker ===")
    print(Fore.YELLOW + "Press Enter to exit at any time...\n")

    domain = input(Fore.YELLOW + "Enter the domain to check (e.g., example.com): ")

    exit_thread = threading.Thread(target=wait_for_exit)
    exit_thread.start()

    checker = SSLCertificateChecker(domain)

    try:
        while not exit_program:
            checker.check_certificate()
            print(Fore.BLUE + "SSL Certificate check completed.")
            break  
    except KeyboardInterrupt:
        exit_program = True
    finally:
        print(Fore.BLUE + "Exiting the SSL Certificate Checker...")
        exit_thread.join()  
        input(Fore.BLUE + "Press Enter to exit...")

if __name__ == "__main__":
    main()
