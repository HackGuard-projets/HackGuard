import time
import requests

def download_file(url):
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:  # Si le serveur ne renvoie pas la taille du fichier
        print("Could not retrieve file size.")
        return 0

    total_length = int(total_length)
    downloaded = 0
    start_time = time.time()

    for data in response.iter_content(chunk_size=4096):
        downloaded += len(data)

    end_time = time.time()
    duration = end_time - start_time

    return downloaded, duration

def calculate_speed(downloaded, duration):
    speed_mbps = (downloaded * 8) / (1024 * 1024 * duration)  # Convertir en Mbps
    return speed_mbps

if __name__ == "__main__":
    # URL d'un fichier de test (par exemple, un fichier de 1 Mo)
    url = "http://ipv4.download.thinkbroadband.com/1MB.zip"  # Remplacez par une URL de fichier de test
    downloaded, duration = download_file(url)

    if downloaded > 0 and duration > 0:
        speed = calculate_speed(downloaded, duration)
        print(f"Downloaded: {downloaded / (1024 * 1024):.2f} MB in {duration:.2f} seconds.")
        print(f"Speed: {speed:.2f} Mbps")
    else:
        print("Download failed.")