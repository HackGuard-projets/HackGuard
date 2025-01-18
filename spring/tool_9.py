import requests
import folium
from colorama import init, Fore, Style
import os
from prettytable import PrettyTable

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_location_ipinfo(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        ip_info = response.json()
        lat, long = ip_info.get('loc', '0,0').split(',')
        return float(lat), float(long), ip_info
    except Exception as e:
        print(Fore.RED + f"Error retrieving data: {e}")
        return None, None, {}

def get_location_ipapi(ip_address):
    return None, None, {}

def create_map(lat, long, ip_info):
    user_map = folium.Map(location=[lat, long], zoom_start=12)
    folium.Marker([lat, long], popup=f"IP: {ip_info['ip']}\nCity: {ip_info.get('city', 'N/A')}\nRegion: {ip_info.get('region', 'N/A')}\nCountry: {ip_info.get('country', 'N/A')}").add_to(user_map)
    return user_map

def display_data(ip_info):
    table = PrettyTable()
    table.field_names = ["Field", "Value"]
    
    table.add_row(["IP", ip_info.get('ip', 'N/A')])
    table.add_row(["City", ip_info.get('city', 'N/A')])
    table.add_row(["Region", ip_info.get('region', 'N/A')])
    table.add_row(["Country", ip_info.get('country', 'N/A')])
    table.add_row(["Latitude", ip_info.get('loc', 'N/A').split(',')[0] if 'loc' in ip_info else 'N/A'])
    table.add_row(["Longitude", ip_info.get('loc', 'N/A').split(',')[1] if 'loc' in ip_info else 'N/A'])
    
    print(Fore.GREEN + str(table))

def main():
    clear_console()
    print(Fore.BLUE + Style.BRIGHT + "=== Geolocation-Tool ===")
    ip_address = input(Fore.BLUE + "Enter the IP address to locate: ")
    
    lat, long, ip_info = get_location_ipinfo(ip_address)
    
    if lat is None or long is None:
        lat, long, ip_info = get_location_ipapi(ip_address)
    
    if lat is not None and long is not None:
        print(Fore.GREEN + f"Latitude: {lat}, Longitude: {long}")
        display_data(ip_info) 
        user_map = create_map(lat, long, ip_info)
        user_map.save("ip_location_map.html")
        print(Fore.GREEN + "Map has been created and saved as 'ip_location_map.html'.")
        input(Fore.BLUE + "Press Enter to exit...")
    else:
        print(Fore.RED + "Failed to retrieve location for the given IP address.")
        input(Fore.BLUE + "Press Enter to exit...")

if __name__ == "__main__":
    main()
