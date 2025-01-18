import psutil
from colorama import init, Fore, Style
import os
import time
import socket
import threading

init(autoreset=True)

exit_program = False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_network_info():
    net_info = psutil.net_if_addrs()
    net_io = psutil.net_io_counters(pernic=True)
    return net_info, net_io

def print_table(interface, addr, stats):
    print(Fore.BLUE + Style.BRIGHT + "+" + "-"*85 + "+")
    print(Fore.BLUE + "| {:<40} | {:<40} |".format(f"Interface: {interface}", f"IP Address: {addr}"))
    print(Fore.BLUE + "| {:<40} | {:<40} |".format("Bytes Sent: " + str(stats.bytes_sent), "Bytes Received: " + str(stats.bytes_recv)))
    print(Fore.BLUE + "| {:<40} | {:<40} |".format("Packets Sent: " + str(stats.packets_sent), "Packets Received: " + str(stats.packets_recv)))
    print(Fore.BLUE + "| {:<40} | {:<40} |".format("Errors Sent: " + str(stats.errout), "Errors Received: " + str(stats.errin)))
    print(Fore.BLUE + "+" + "-"*85 + "+")

def wait_for_exit():
    global exit_program
    input(Fore.BLUE + "Press Enter to exit at any time...")
    exit_program = True

def main():
    global exit_program
    clear_console()
    print(Fore.BLUE + Style.BRIGHT + "=== Network Traffic Monitor ===")
    print(Fore.YELLOW + "Press Enter to exit at any time...\n")
    
    exit_thread = threading.Thread(target=wait_for_exit)
    exit_thread.start()
    
    try:
        while not exit_program:
            clear_console()
            print(Fore.BLUE + Style.BRIGHT + "=== Network Traffic Monitor ===")
            print(Fore.YELLOW + "Press Enter to exit at any time...\n")
            net_info, net_io = get_network_info()
            for interface, addresses in net_info.items():
                stats = net_io.get(interface)
                if stats:
                    for addr in addresses:
                        if addr.family == socket.AF_INET: 
                            print_table(interface, addr.address, stats)
            time.sleep(1)
    except KeyboardInterrupt:
        exit_program = True
    finally:
        print(Fore.BLUE + "Exiting the Network Traffic Monitor...")
        exit_thread.join()  
        input(Fore.BLUE + "Press Enter to exit...")

if __name__ == "__main__":
    main()
