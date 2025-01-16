import requests
import json
import random
import threading
import subprocess
import sys
import time

def current_time_hour():
    return time.strftime("%H:%M:%S")

def send_webhook(webhook_url, embed_content, username_webhook, avatar_webhook):
    payload = {
        'embeds': [embed_content],
        'username': username_webhook,
        'avatar_url': avatar_webhook
    }

    headers = {
        'Content-Type': 'application/json'
    }

    requests.post(webhook_url, data=json.dumps(payload), headers=headers)

def ip_check(webhook_url, username_webhook, avatar_webhook, color_webhook):
    number_valid = 0
    number_invalid = 0

    while True:
        number_1 = random.randint(1, 255)
        number_2 = random.randint(1, 255)
        number_3 = random.randint(1, 255)
        number_4 = random.randint(1, 255)
        ip = f"{number_1}.{number_2}.{number_3}.{number_4}"

        try:
            if sys.platform.startswith("win"):
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=0.1)
            elif sys.platform.startswith("linux"):
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=0.1)

            if result.returncode == 0:
                number_valid += 1
                embed_content = {
                    'title': 'Ip Valid!',
                    'description': f"**__Ip:__**\n```{ip}```",
                    'color': color_webhook,
                    'footer': {
                        "text": username_webhook,
                        "icon_url": avatar_webhook,
                    }
                }
                send_webhook(webhook_url, embed_content, username_webhook, avatar_webhook)
                print(f"[{current_time_hour()}] Logs: {number_invalid} invalid - {number_valid} valid | Status: Valid | Ip: {ip}")
            else:
                number_invalid += 1
                print(f"[{current_time_hour()}] Logs: {number_invalid} invalid - {number_valid} valid | Status: Invalid | Ip: {ip}")

        except Exception as e:
            number_invalid += 1
            print(f"[{current_time_hour()}] Logs: {number_invalid} invalid - {number_valid} valid | Status: Invalid | Ip: {ip}")

def request(webhook_url, username_webhook, avatar_webhook, color_webhook, threads_number):
    threads = []
    for _ in range(threads_number):
        t = threading.Thread(target=ip_check, args=(webhook_url, username_webhook, avatar_webhook, color_webhook))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("IP Generator")

    webhook = input("Webhook (y/n)? -> ")
    webhook_url = None
    if webhook.lower() in ['y', 'yes', 'o', 'oui']:
        webhook_url = input("Webhook URL -> ")

    threads_number = int(input("Number of threads -> "))
    username_webhook = "YourWebhookUsername" 
    avatar_webhook = "YourWebhookAvatarURL"   
    color_webhook = 0x00FF00   

    try:
        while True:
            request(webhook_url, username_webhook, avatar_webhook, color_webhook, threads_number)
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
