import threading
import time
import socket

def current_time_hour():
    return time.strftime("%H:%M:%S")

def ping_ip(hostname, port, bytes):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        start_time = time.time()
        sock.connect((hostname, port))
        data = b'\x00' * bytes
        sock.sendall(data)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f'{current_time_hour()} Ping to {hostname}: time={elapsed_time:.2f}ms port={port} bytes={bytes} status=succeed')
    except Exception as e:
        elapsed_time = 0
        print(f'{current_time_hour()} Ping to {hostname}: time={elapsed_time}ms port={port} bytes={bytes} status=fail')

def request(hostname, port, bytes, threads_number):
    threads = []
    for _ in range(int(threads_number)):
        t = threading.Thread(target=ping_ip, args=(hostname, port, bytes))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Ip Pinger")

    hostname = input("Ip -> ")
    port_input = input("Port (enter for default) -> ")
    port = int(port_input) if port_input.strip() else 80

    bytes_input = input("Bytes (enter for default) -> ")
    bytes = int(bytes_input) if bytes_input.strip() else 64

    threads_input = input("Number of threads (enter for default) -> ")
    threads_number = int(threads_input) if threads_input.strip() else 1

    while True:
        request(hostname, port, bytes, threads_number)