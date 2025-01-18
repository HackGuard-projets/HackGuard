import psutil
import os
import time
from colorama import init, Fore, Style

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_system_info():
    clear_console()
    print(Fore.BLUE + Style.BRIGHT + "=== System Resource Monitor ===")
    
    cpu_usage = psutil.cpu_percent(interval=1)
    print(Fore.GREEN + "CPU Usage: " + Fore.YELLOW + f"{cpu_usage}%")
    
    memory = psutil.virtual_memory()
    print(Fore.GREEN + "Memory Usage: " + Fore.YELLOW + f"{memory.percent}% ({memory.used / (1024 ** 2):.2f} MB used / {memory.total / (1024 ** 2):.2f} MB total)")
    
    disk = psutil.disk_usage('/')
    print(Fore.GREEN + "Disk Usage: " + Fore.YELLOW + f"{disk.percent}% ({disk.used / (1024 ** 3):.2f} GB used / {disk.total / (1024 ** 3):.2f} GB total)")
    
    net_io = psutil.net_io_counters()
    print(Fore.GREEN + "Network Usage: " + Fore.YELLOW + f"Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB, Received: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

def main():
    try:
        while True:
            display_system_info()
            time.sleep(2)
    except KeyboardInterrupt:
        print(Fore.RED + "\nExiting System Resource Monitor...")
        print(Fore.YELLOW + "\n" + "="*30) 
        print(Fore.YELLOW + "Press Enter to exit the program...")
        input()

if __name__ == "__main__":
    main()
