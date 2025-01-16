import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def is_valid_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])

def check_url_accessibility(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error accessing the URL {url}: {e}")
        return None

def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    
    for link in soup.find_all('a', href=True):
        links.add(link['href'])
    
    return links

def print_links(links):
    print("\n" + "="*50)
    print("Links found on the page:")
    print("="*50)
    for link in links:
        print(f"- {link}")
    print("="*50)

def main():
    url = input("Enter the URL to check (e.g., http://example.com): ")
    
    if not is_valid_url(url):
        print("The provided URL is not valid. Please enter a well-formed URL.")
        return
    
    response = check_url_accessibility(url)
    
    if response:
        print(f"\nThe URL {url} is accessible.")
        print(f"HTTP Status Code: {response.status_code}")
        
        links = extract_links(response.text)
        print_links(links)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
