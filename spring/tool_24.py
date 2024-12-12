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
    }
}


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
        print(f"{BEFORE + current_time_hour() + AFTER} {translations[LANGUAGE]['tool_infos_recovery']}{reset}")

        user_info_response = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
        
        if user_info_response.status_code == 200:
            user_info = user_info_response.json()

            userid = user_info.get('id', "None")
            display_name = user_info.get('displayName', "None")
            username = user_info.get('name', "None")
            description = user_info.get('description', "Aucune")
            created_at = user_info.get('created', "None")
            is_banned = user_info.get('isBanned', "None")
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

        else:
            print(f"{translations[LANGUAGE]['Error']}: Impossible de récupérer les informations pour l'ID {user_id}.")
        
        input(translations[LANGUAGE]['Continue']) 
    except Exception as e:
        print(f"{translations[LANGUAGE]['Error']}: {str(e)}")

if __name__ == "__main__":
    main()