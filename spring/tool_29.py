import os
import requests
import sys
from colorama import Fore, Style

def print_data(data):
    print(f"{Fore.RED}=============================={Style.RESET_ALL}")
    print(f"{Fore.RED}IP Information:{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Public IP: {data.get('ip', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] City: {data.get('city', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Region: {data.get('region', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Country: {data.get('country', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Postal Code: {data.get('postal', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] ISP: {data.get('isp', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Latitude: {data.get('latitude', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}[+] Longitude: {data.get('longitude', 'Unavailable')}{Style.RESET_ALL}")
    print(f"{Fore.RED}=============================={Style.RESET_ALL}")

def error(ex):
    print(f"{Fore.RED}Error: {ex}{Style.RESET_ALL}")

def my_ip():
    try:
        res = requests.get('https://api.ipify.org?format=json')
        public_ip = res.json()['ip']

        res = requests.get(f'https://api.techniknews.net/ipgeo/{public_ip}')
        print_data(data=res.json())

    except Exception as ex:
        error(ex)

def ret():
    input(f"{Fore.RED}Press Enter to continue...{Style.RESET_ALL}")

my_ip()
ret()
