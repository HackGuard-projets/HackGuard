import requests
import json
import datetime


LANGUAGE = 'fr' 
translations = {
    'fr': {
        'Username': 'Nom d\'utilisateur',
        'Invalid': 'Invalide',
        'Status': 'Statut',
        'Robux': 'Robux',
        'Premium': 'Premium',
        'Builders Club': 'Club des bâtisseurs',
        'Avatar': 'Avatar',
        'Cookie': 'Cookie',
        'Information Recovery': 'Récupération d\'information',
        'Continue': 'Appuyez sur Entrée pour continuer...',
        'Error': 'Erreur',
        'Wait': 'Veuillez patienter...',
    }
}


BEFORE = ""
AFTER = ""
INPUT = ""
INFO_ADD = ""
secondary = ""
invalid = ""
reset = ""

def current_time_hour():
    return datetime.datetime.now().strftime("%H:%M:%S")

def main():
    print("Roblox Cookie Info")

    try:
        cookie = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Cookie -> {secondary}")
        print(f"{BEFORE + current_time_hour() + AFTER} {translations[LANGUAGE]['Wait']} Information Recovery..{reset}")
        
        response = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
        
        if response.status_code == 200:
            information = response.json()
            status = "Valid"
        else:
            status = "Invalid"
            information = {}

        username_roblox = information.get('User Name', "None")
        user_id_roblox = information.get("User ID", "None")
        robux_roblox = information.get("RobuxBalance", "None")
        premium_roblox = information.get("IsPremium", "None")
        avatar_roblox = information.get("ThumbnailUrl", "None")
        builders_club_roblox = information.get("IsAnyBuildersClubMember", "None")

        print(f"""
        {translations[LANGUAGE]['Status']}        : {secondary}{status}{invalid}
        {translations[LANGUAGE]['Username']}      : {secondary}{username_roblox}{invalid}
        {translations[LANGUAGE]['Id']}            : {secondary}{user_id_roblox}{invalid}
        {translations[LANGUAGE]['Robux']}         : {secondary}{robux_roblox}{invalid}
        {translations[LANGUAGE]['Premium']}       : {secondary}{premium_roblox}{invalid}
        {translations[LANGUAGE]['Builders Club']} : {secondary}{builders_club_roblox}{invalid}
        {translations[LANGUAGE]['Avatar']}        : {secondary}{avatar_roblox}{invalid}
        """)

        input(translations[LANGUAGE]['Continue']) 
    except Exception as e:
        print(f"{translations[LANGUAGE]['Error']}: {str(e)}")

if __name__ == "__main__":
    main()