import requests
from bs4 import BeautifulSoup
import whois

def check_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        print(f"\nThe website {url} is accessible.\n")
        return response
    except requests.exceptions.RequestException as e:
        print(f"\nError accessing the website {url}: {e}\n")
        return None

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    
    for link in soup.find_all('a', href=True):
        links.add(link['href'])
    
    return links

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]  
        return {
            'domain': domain_info.domain_name,
            'creation_date': creation_date,
            'expiration_date': domain_info.expiration_date,
            'registrar': domain_info.registrar,
            'status': domain_info.status,
        }
    except Exception as e:
        print(f"Error retrieving WHOIS information for {domain}: {e}")
        return None

def print_http_headers(headers):
    print("\n" + "="*50)
    print("HTTP Response Headers:")
    print("="*50)
    for key, value in headers.items():
        print(f"{key}: {value}")
    print("="*50)

def print_links(links):
    print("\n" + "="*50)
    print("Links found on the website:")
    print("="*50)
    for link in links:
        print(f"- {link}")
    print("="*50)

def print_whois_info(whois_info):
    print("\n" + "="*50)
    print(f"WHOIS information for {whois_info['domain']}:")
    print("="*50)
    print(f"Creation Date: {whois_info['creation_date']}")
    print(f"Expiration Date: {whois_info['expiration_date']}")
    print(f"Registrar: {whois_info['registrar']}")
    print(f"Status: {whois_info['status']}")
    print("="*50)

def main():
    url = input("Enter the URL of the website to scan (e.g., http://example.com): ")
    
    response = check_website(url)
    
    if response:
      
        print_http_headers(response.headers)
        
     
        links = extract_links(response.text)
        print_links(links)
        
 
        domain = url.split("//")[-1].split("/")[0]  
        whois_info = get_whois_info(domain)
        
        if whois_info:
            print_whois_info(whois_info)


    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
