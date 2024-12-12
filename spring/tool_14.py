import requests
import subprocess
import socket
import concurrent.futures

def ping_ip(ip):
    try:
        if sys.platform.startswith("win"):
            result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
        elif sys.platform.startswith("linux"):
            result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
        ping = "Succeed" if result.returncode == 0 else "Fail"
    except:
        ping = "Fail"

    print(f"    Ping         : {ping}")

def port_ip(ip):
    open_ports = []

    def scan_port(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {executor.submit(scan_port, ip, port): port for port in range(1, 1001)}
    concurrent.futures.wait(results)

    print(f"    Open Ports   : {open_ports}")

def dns_ip(ip):
    try:
        dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
    except:
        dns = "None"
    print(f"    DNS          : {dns}")

def info_ip(ip):
    try:
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        api = response.json()

        status = api.get('status', 'Invalid')
        country = api.get('country', 'None')
        region = api.get('region', 'None')
        city = api.get('city', 'None')
        latitude = api.get('latitude', 'None')
        longitude = api.get('longitude', 'None')
        isp = api.get('isp', 'None')
        org = api.get('org', 'None')

    except:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        api = response.json()

        status = "Valid" if api.get('status') == "success" else "Invalid"
        country = api.get('country', "None")
        region = api.get('region', "None")
        city = api.get('city', "None")
        latitude = api.get('lat', "None")
        longitude = api.get('lon', "None")
        isp = api.get('isp', "None")
        org = api.get('org', "None")

    print(f"""    Status       : {status}
    Country      : {country}
    Region       : {region}
    City         : {city}
    Latitude     : {latitude}
    Longitude    : {longitude}
    ISP          : {isp}
    Org          : {org}""")

def main():
    ip = input("Enter IP address: ")
    print(f"Retrieving information for IP: {ip}")
    ping_ip(ip)
    dns_ip(ip)
    info_ip(ip)
    port_ip(ip)

if __name__ == "__main__":
    main()