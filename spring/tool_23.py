import requests
import datetime

BEFORE = ""
AFTER = ""
INPUT = ""
INFO_ADD = ""
secondary = ""
primary = ""
reset = ""
invalid = ""

def current_time_hour():
    return datetime.datetime.now().strftime("%H:%M:%S")

def main():
    print("Roblox User Info")

    try:
        username_input = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Username -> {reset}")
        print(f"{BEFORE + current_time_hour() + AFTER} Recovering user information...{reset}")

        response = requests.post("https://users.roblox.com/v1/usernames/users", json={
            "usernames": [username_input],
            "excludeBannedUsers": "true"
        })

        data = response.json()

        if not data['data']:
            print("User  not found.")
            input("Press Enter to continue...")
            return

        user_id = data['data'][0]['id']

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        user_info = user_info_response.json()

        userid = user_info.get('id', "None")
        display_name = user_info.get('displayName', "None")
        username = user_info.get('name', "None")
        description = user_info.get('description', "None")
        created_at = user_info.get('created', "None")
        is_banned = user_info.get('isBanned', "None")
        external_app_display_name = user_info.get('externalAppDisplayName', "None")
        has_verified_badge = user_info.get('hasVerifiedBadge', "No")

        print("\n" + "="*40)
        print(f"Username            : {username}")
        print(f"Id                  : {userid}")
        print(f"Display Name        : {display_name}")
        print(f"Description         : {description}")
        print(f"Created             : {created_at}")
        print(f"Banned              : {is_banned}")
        print(f"External Name       : {external_app_display_name}")
        print(f"Verified Badge      : {has_verified_badge}")
        print("="*40 + "\n")

        input("Press Enter to continue...")  
    except Exception as e:
        print(f"Error: {str(e)}")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
