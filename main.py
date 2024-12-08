import requests
import socket
import whois
import dns.resolver
import nmap
from colorama import Fore, Style, init

init(autoreset=True)

def scan_url(url):
    try:
        response = requests.get(url)
        return response.status_code, response.headers
    except Exception as e:
        return str(e), None

def ip_detect(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except Exception as e:
        return str(e)

def port_scanner(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1024')  # Scan ports 1 to 1024
    return nm[ip]['tcp']

def dns_lookup(url):
    try:
        result = dns.resolver.resolve(url, 'A')
        return [ip.address for ip in result]
    except Exception as e:
        return str(e)

def whois_lookup(url):
    try:
        domain_info = whois.whois(url)
        return domain_info
    except Exception as e:
        return str(e)

def display_menu():
    print(Fore.GREEN + "\n--- Menu Principal ---")
    print(Fore.CYAN + "[1] Scan URL")
    print(Fore.CYAN + "[2] Détection IP")
    print(Fore.CYAN + "[3] Scanner de ports")
    print(Fore.CYAN + "[4] Recherche DNS")
    print(Fore.CYAN + "[5] Recherche Whois")
    print(Fore.CYAN + "[7] Credits")
    print(Fore.CYAN + "[6] Quitter")
    print(Style.RESET_ALL)



def main():
    print(Fore.MAGENTA + r"""
  _    _            _     _____                     _ 
 | |  | |          | |   / ____|                   | |
 | |__| | __ _  ___| | _| |  __ _   _  __ _ _ __ __| |
 |  __  |/ _` |/ __| |/ / | |_ | | | |/ _` | '__/ _` |
 | |  | | (_| | (__|   <| |__| | |_| | (_| | | | (_| |
 |_|  |_|\__,_|\___|_|\_\\_____|\__,_|\__,_|_|  \__,_|
""" + Style.RESET_ALL)

    while True:
        display_menu()
        choice = input(Fore.YELLOW + "Choisissez une option (1-6) : " + Style.RESET_ALL)

        if choice == '1':
            url = input(Fore.YELLOW + "Entrez l'URL ou le domaine à analyser : " + Style.RESET_ALL)
            status_code, headers = scan_url(url)
            print(Fore.GREEN + f"Code de statut : {status_code}")
            print(Fore.GREEN + f"En-têtes : {headers}")

        elif choice == '2':
            url = input(Fore.YELLOW + "Entrez l'URL ou le domaine à analyser : " + Style.RESET_ALL)
            ip_address = ip_detect(url)
            print(Fore.GREEN + f"Adresse IP : {ip_address}")

        elif choice == '3':
            url = input(Fore.YELLOW + "Entrez l'URL ou le domaine à analyser : " + Style.RESET_ALL)
            ip_address = ip_detect(url)
            ports = port_scanner(ip_address)
            print(Fore.GREEN + f"Ports ouverts : {ports}")

        elif choice == '4':
            url = input(Fore.YELLOW + "Entrez l'URL ou le domaine à analyser : " + Style.RESET_ALL)
            dns_records = dns_lookup(url)
            print(Fore.GREEN + f"Enregistrements DNS : {dns_records}")

        elif choice == '5':
            url = input(Fore.YELLOW + "Entrez l'URL ou le domaine à analyser : " + Style.RESET_ALL)
            whois_info = whois_lookup(url)
            print(Fore.GREEN + f"Informations Whois : {whois_info}")

        elif choice == '6':
            print(Fore.RED + "Au revoir!")
            break

        elif choice == '7':
            print(Fore.CYAN + """
            Tools by potopilo 
            Version 1.0
            
            """)

        else:
            print(Fore.RED + "Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
