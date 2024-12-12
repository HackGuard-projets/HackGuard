import requests
import datetime


LANGUAGE = 'fr' 
translations = {
    'fr': {
        'Username': 'Nom d\'utilisateur',
        'DisplayName': 'Nom d\'affichage',
        'Created': 'Créé',
        'Banned': 'Banni',
        'VerifBadge': 'Badge vérifié',
        'tool_infos_recovery': 'Récupération des informations de l\'utilisateur...',
        'Error': 'Erreur',
        'Continue': 'Appuyez sur Entrée pour continuer...',
        'User NotFound': 'Utilisateur non trouvé.',
    }
}


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
        print(f"{BEFORE + current_time_hour() + AFTER} {translations[LANGUAGE]['tool_infos_recovery']}{reset}")

        response = requests.post("https://users.roblox.com/v1/usernames/users", json={
            "usernames": [username_input],
            "excludeBannedUsers": "true"
        })

        data = response.json()

        if not data['data']:
            print(translations[LANGUAGE]['User NotFound'])
            input(translations[LANGUAGE]['Continue'])
            return

        user_id = data['data'][0]['id']

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        user_info = user_info_response.json()


        userid = user_info.get('id', "Aucune")
        display_name = user_info.get('displayName', "Aucune")
        username = user_info.get('name', "Aucune")
        description = user_info.get('description', "Aucune")
        created_at = user_info.get('created', "Aucune")
        is_banned = user_info.get('isBanned', "Aucune")
        external_app_display_name = user_info.get('externalAppDisplayName', "Aucune")
        has_verified_badge = user_info.get('hasVerifiedBadge', "Non")

  
        print("\n" + "="*40)
        print(f"{translations[LANGUAGE]['Username']: <20}: {username}")
        print(f"{'Id': <20}: {userid}")
        print(f"{translations[LANGUAGE]['DisplayName']: <20}: {display_name}")
        print(f"{'Description': <20}: {description}")
        print(f"{translations[LANGUAGE]['Created']: <20}: {created_at}")
        print(f"{translations[LANGUAGE]['Banned']: <20}: {is_banned}")
        print(f"{'External Name': <20}: {external_app_display_name}")
        print(f"{translations[LANGUAGE]['VerifBadge']: <20}: {has_verified_badge}")
        print("="*40 + "\n")

        input(translations[LANGUAGE]['Continue'])  
    except Exception as e:
        print(f"{translations[LANGUAGE]['Error']}: {str(e)}")

if __name__ == "__main__":
    main()