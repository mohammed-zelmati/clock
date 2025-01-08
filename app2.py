import time

# Variables globales pour l'heure actuelle et l'alarme
heure_actuelle = (0, 0, 0)
alarme = None

def obtenir_heure_systeme(): 
    t = time.localtime() # Récupère l'heure locale actuelle sous forme de struct_time 
    return (t.tm_hour, t.tm_min, t.tm_sec)

def afficher_heure():
    global heure_actuelle
    while True:
        heure_formatee = f"{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}"
        print(f"\r{heure_formatee}", end="", flush=True)
        time.sleep(1)
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)
        if heure_actuelle[2] >= 60:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
        if heure_actuelle[1] >= 60:
            heure_actuelle = (heure_actuelle[0] + 1, 0, heure_actuelle[2])
        if heure_actuelle[0] >= 24:
            heure_actuelle = (0, heure_actuelle[1], heure_actuelle[2])
        
        if alarme and heure_actuelle == alarme:
            print("\nAlarme !")  # Affiche "Alarme !" sur une nouvelle ligne

def regler_heure(heures, minutes, secondes):
    global heure_actuelle
    heure_actuelle = (heures, minutes, secondes)

def regler_alarme(heures, minutes, secondes):
    global alarme
    alarme = (heures, minutes, secondes) 
    print(f"Alarme réglée pour {alarme[0]:02d}:{alarme[1]:02d}:{alarme[2]:02d}")

# Initialiser l'heure actuelle avec l'heure locale 
heure_actuelle = obtenir_heure_systeme()

# Demander à l'utilisateur d'entrer l'heure, les minutes et les secondes pour l'alarme  :
heures = int(input("Entrez l'heure pour l'alarme : ")) 
minutes = int(input("Entrez les minutes pour l'alarme : ")) 
secondes = int(input("Entrez les secondes pour l'alarme : "))

# L'affichage de l'alarme est à quelle heure :
regler_alarme(heures, minutes, secondes)

# Lancer l'affichage de l'heure
afficher_heure()
