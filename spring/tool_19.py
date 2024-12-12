import random
import string

def generer_mot_de_passe(longueur=12):

    caracteres = string.ascii_letters + string.digits + string.punctuation
    

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    
    return mot_de_passe


mot_de_passe = generer_mot_de_passe()
print(f"Votre mot de passe aléatoire est : {mot_de_passe}")
