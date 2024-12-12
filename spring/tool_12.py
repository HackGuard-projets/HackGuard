import dns.resolver
import requests
import re
import datetime


LANGUAGE = 'fr' 
translations = {
    'fr': {
        'Domain': 'Domaine',
        'Email': 'Email',
        'Name': 'Nom',
        'Tld': 'Tld',
        'Domain All': 'Domaine Complet',
        'Servers': 'Serveurs',
        'Spf': 'SPF',
        'Dmarc': 'DMARC',
        'Workspace': 'Espace de travail',
        'Mailgun': 'Validation Mailgun',
        'Information Recovery': 'Récupération des informations...',
        'Continue': 'Appuyez sur Entrée pour continuer...',
        'Invalid Email': 'Adresse e-mail invalide.',
    }
}


BEFORE = ""
AFTER = ""
INPUT = ""
INFO_ADD = ""
primary = ""
secondary = ""
reset = ""

def current_time_hour():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_email_info(email):
    info = {}
    try:
        domain_all = email.split('@')[-1]
        name = email.split('@')[0]
        domain = re.search(r"@([^@.]+)\.", email).group(1)
        tld = f".{email.split('.')[-1]}"


        try:
            mx_records = dns.resolver.resolve(domain_all, 'MX')
            info["mx_servers"] = [str(record.exchange) for record in mx_records]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            info["mx_servers"] = None

 
        try:
            spf_records = dns.resolver.resolve(domain_all, 'SPF')
            info["spf_records"] = [str(record) for record in spf_records]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            info["spf_records"] = None


        try:
            dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
            info["dmarc_records"] = [str(record) for record in dmarc_records]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            info["dmarc_records"] = None


        if info.get("mx_servers"):
            for server in info["mx_servers"]:
                if "google.com" in server:
                    info["google_workspace"] = True
                elif "outlook.com" in server:
                    info["microsoft_365"] = True

       
        try:
            response = requests.get(
                f"https://api.mailgun.net/v4/address/validate?address={email}",
                auth=("api", "YOUR_MAILGUN_API_KEY")  
            )
            data = response.json()
            info["mailgun_validation"] = data
        except Exception as e:
            info["mailgun_validation"] = {"error": str(e)}

        return info, domain_all, domain, tld, name

    except Exception as e:
        print(f"{translations[LANGUAGE]['Invalid Email']}: {e}")
        return None, None, None, None, None

def main():
    email = input(f"\n{BEFORE + current_time_hour() + AFTER} {translations[LANGUAGE]['Email']} -> {reset}")
    
    print(f"{BEFORE + current_time_hour() + AFTER} {translations[LANGUAGE]['Information Recovery']}..{reset}")
    info, domain_all, domain, tld, name = get_email_info(email)

    if info is None:
        return


    mx_servers = ' / '.join(info.get("mx_servers", ["Aucun"]))
    spf_records = ' / '.join(info.get("spf_records", ["Aucun"]))
    dmarc_records = ' / '.join(info.get("dmarc_records", ["Aucun"]))
    google_workspace = info.get("google_workspace", False)
    mailgun_validation = info.get("mailgun_validation", {}).get('is_valid', 'Inconnu')

é
    print(f"""
    {INFO_ADD} {translations[LANGUAGE]['Email']}      : {secondary}{email}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Name']}       : {secondary}{name}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Domain']}     : {secondary}{domain}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Tld']}        : {secondary}{tld}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Domain All']} : {secondary}{domain_all}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Servers']}    : {secondary}{mx_servers}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Spf']}        : {secondary}{spf_records}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Dmarc']}      : {secondary}{dmarc_records}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Workspace']}  : {secondary}{google_workspace}{primary}
    {INFO_ADD} {translations[LANGUAGE]['Mailgun']}    : {secondary}{mailgun_validation}{primary}
    {reset}""")

    input(translations[LANGUAGE]['Continue'])  

if __name__ == "__main__":
    main()