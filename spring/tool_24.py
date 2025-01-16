import requests
import datetime

BEFORE = ""
AFTER = ""
INPUT = ""
INFO_ADD = ""
secondary = ""
primary = ""
reset = ""

def current_time_hour():
    return datetime.datetime.now().strftime("%H:%M:%S")

def main():
    print("Roblox User Info")

    try:
        user_id = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} ID -> {reset}")
        print(f"{BEFORE + current_time_hour() + AFTER} Recovering user information...{reset}")

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        
        if user_info_response.status_code == 200:
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
            print(f"{'Username': <20}: {username}")
            print(f"{'Id': <20}: {userid}")
            print(f"{'Display Name': <20}: {display_name}")
            print(f"{'Description': <20}: {description}")
            print(f"{'Created': <20}: {created_at}")
            print(f"{'Banned': <20}: {is_banned}")
            print(f"{'External Name': <20}: {external_app_display_name}")
            print(f"{'Verified Badge': <20}: {has_verified_badge}")
            print("="*40 + "\n")

        else:
            print(f"Error: Unable to retrieve information for ID {user_id}.")
        
        input("Press Enter to continue...") 
    except Exception as e:
        print(f"Error: {str(e)}")
        input("Press Enter to continue...")  

if __name__ == "__main__":
    main()
