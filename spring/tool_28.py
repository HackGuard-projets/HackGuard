import os

def file_scanner(directory, file_extension):
    """
    Scanne le répertoire donné et affiche les fichiers avec l'extension spécifiée.

    :param directory: Répertoire à scanner.
    :param file_extension: Extension de fichier à rechercher (ex: .txt).
    """

    if not os.path.exists(directory):
        print(f"Le répertoire {directory} n'existe pas.")
        return

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_extension):
                print(os.path.join(root, file))

if __name__ == "__main__":
    directory_to_scan = input("Entrez le chemin du répertoire à scanner : ")
    extension_to_find = input("Entrez l'extension des fichiers à rechercher (ex: .txt) : ")

    file_scanner(directory_to_scan, extension_to_find)
