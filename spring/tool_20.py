import os
from datetime import datetime


LANGUAGE = 'en' 
translations = {
    'en': {
        'AddDB1': 'Adding database folder',
        'NoDB': 'No database found in',
        'Search': 'Search',
        'DBSearch': 'Searching in database...',
        'ErrorReadFile': 'Error reading file',
        'NoResultSearch': 'No results found for',
        'TotalSearchFile': 'Total files searched',
        'ErrorSearch': 'Error during search'
    }
}


class Color:
    YELLOW = '\033[93m'
    PRIMARY = '\033[0m'
    SECONDARY = '\033[94m'
    BEFORE = '\033[92m'
    AFTER = '\033[0m'
    INFO = '[INFO]'
    WAIT = '[WAIT]'
    ERROR = '[ERROR]'
    INPUT = '[INPUT]'
    
reset = Color.AFTER
primary = Color.PRIMARY
secondary = Color.SECONDARY
before = Color.BEFORE
after = Color.AFTER
info = Color.INFO
wait = Color.WAIT
error = Color.ERROR
input_prompt = Color.INPUT

current_language = LANGUAGE

def tr(key):
    return translations[current_language].get(key, key)

def current_time_hour():
    return datetime.now().strftime("%H:%M:%S")

def Title(text):
    print(f"\n=== {text} ===")

def Continue():
    input(f"{input_prompt} Press Enter to continue...")

def Reset():
    print(reset)

def Error(e):
    print(f"{before}{error} {e}{after}")

Title("Search DataBase")

try:
    folder_database_relative = "./2-Input/DataBase"
    folder_database = os.path.abspath(folder_database_relative)

    print(f"""
{before + current_time_hour() + after} {info} {tr('AddDB1')} "{secondary}{folder_database_relative}{primary}".
{before + current_time_hour() + after} {info} {tr('NoDB')} "{secondary}{folder_database}{primary}".""")
    search = input(f"\n{before + current_time_hour() + after} {input_prompt} {tr('Search')} -> {reset}")

    print(f"{before + current_time_hour() + after} {wait} {tr('DBSearch')}")

    def TitleSearch(files_searched, element):
        Title(f"Search DataBase | Total: {files_searched} | File: {element}")

    try:
        files_searched = 0

        def check(folder):
            global files_searched
            results_found = False
            print(f"{before + current_time_hour() + after} {wait} Search in {secondary}{folder}")
            for element in os.listdir(folder):
                chemin_element = os.path.join(folder, element)
                if os.path.isdir(chemin_element):
                    check(chemin_element)
                elif os.path.isfile(chemin_element):
                    try:
                        with open(chemin_element, 'r', encoding='utf-8') as file:
                            line_number = 0
                            files_searched += 1
                            TitleSearch(files_searched, element)
                            for line in file:
                                line_number += 1
                                if search in line:
                                    results_found = True
                                    line_info = line.strip().replace(search, f"{Color.YELLOW}{search}{secondary}")
                                    print(f"""{primary}
- Folder : {secondary}{folder}{primary}
- File   : {secondary}{element}{primary}
- Line   : {secondary}{line_number}{primary}
- Result : {secondary}{line_info}
    """)
                    except UnicodeDecodeError:
                        try:
                            with open(chemin_element, 'r', encoding='latin-1') as file:
                                files_searched += 1
                                line_number = 0
                                TitleSearch(files_searched, element)
                                for line in file:
                                    line_number += 1
                                    if search in line:
                                        results_found = True
                                        line_info = line.strip().replace(search, f"{Color.YELLOW}{search}{secondary}")
                                        print(f"""{primary}
- Folder : {secondary}{folder}{primary}
- File   : {secondary}{element}{primary}
- Line   : {secondary}{line_number}{primary}
- Result : {secondary}{line_info}
    """)
                        except Exception as e:
                            print(f"{before + current_time_hour() + after} {error} {tr('ErrorReadFile')} \"{secondary}{element}{primary}\": {secondary}{e}")
                    except Exception as e:
                        print(f"{before + current_time_hour() + after} {error} {tr('ErrorReadFile')} \"{secondary}{element}{primary}\": {secondary}{e}")
            return results_found

        results_found = check(folder_database)
        if not results_found:
            print(f"{before + current_time_hour() + after} {info} {tr('NoResultSearch')} \"{secondary}{search}{primary}\".")

        print(f"{before + current_time_hour() + after} {info} {tr('TotalSearchFile')} {secondary}{files_searched}")

    except Exception as e:
        print(f"{before + current_time_hour() + after} {error} {tr('ErrorSearch')} {secondary}{e}")

    Continue()
    Reset()
except Exception as e:
    Error(e)
