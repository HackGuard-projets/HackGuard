import socket
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

class PortKnocker:
    def __init__(self, host, ports, delay):
        self.host = host
        self.ports = ports
        self.delay = delay

    def knock(self):
        for port in self.ports:
            print(Fore.GREEN + f"Knocking on port {port}...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)  
                try:
                    result = sock.connect_ex((self.host, port))
                    if result == 0:
                        print(Fore.GREEN + f"Successfully knocked on port {port}.")
                    else:
                        print(Fore.RED + f"Failed to knock on port {port}.")
                except Exception as e:
                    print(Fore.RED + f"Error knocking on port {port}: {e}")
            time.sleep(self.delay)  
def main():
    global exit_program
    clear_console()
    print(Fore.BLUE + Style.BRIGHT + "=== Port Knocking Tool ===")
    print(Fore.YELLOW + "Press Enter to exit at any time...\n")


    host = input(Fore.YELLOW + "Enter the target host (IP or hostname): ")
    ports = input(Fore.YELLOW + "Enter the ports to knock (space-separated): ")
    ports = list(map(int, ports.split()))
    delay = float(input(Fore.YELLOW + "Enter the delay between knocks (in seconds): "))


    exit_thread = threading.Thread(target=wait_for_exit)
    exit_thread.start()


    knocker = PortKnocker(host, ports, delay)
    
    try:
        while not exit_program:
            knocker.knock()
            print(Fore.BLUE + "Knocking sequence completed.")
            break 
    except KeyboardInterrupt:
        exit_program = True
    finally:
        print(Fore.BLUE + "Exiting the Port Knocking Tool...")
        exit_thread.join()  
        input(Fore.BLUE + "Press Enter to exit...")

if __name__ == "__main__":
    main()
