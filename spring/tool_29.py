import os
import requests
import sys
from colorama import Fore, Style

def print_data(data):
    print(f"{Fore.RED}=============================={Style.RESET_ALL}")
    print(f"{Fore.RED}Informations IP :{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] IP publique : {data.get('ip', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Ville : {data.get('city', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Région : {data.get('region', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Pays : {data.get('country', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Code postal : {data.get('postal', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Fournisseur : {data.get('isp', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Latitude : {data.get('latitude', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Longitude : {data.get('longitude', 'Non disponible')}{Style.RESET_ALL}")
    print(f"{Fore.RED}=============================={Style.RESET_ALL}")

def error(ex):
    print(f"{Fore.RED}Erreur : {ex}{Style.RESET_ALL}")

def my_ip():
    try:
        res = requests.get('https://api.ipify.org?format=json')
        public_ip = res.json()['ip']

        res = requests.get(f'https://api.techniknews.net/ipgeo/{public_ip}')
        print_data(data=res.json())

    except Exception as ex:
        error(ex)

def ret():
    input(f"{Fore.RED}Appuyez sur Entrée pour continuer...{Style.RESET_ALL}")

my_ip()
ret()