import time

def obtenir_heure_systeme(): 
    t = time.localtime()  # Récupère l'heure locale actuelle sous forme de struct_time 
    return (t.tm_hour, t.tm_min, t.tm_sec)

def convertir_en_12H(heure):
    heures, minutes, secondes = heure
    periode = "AM"
    if heures > 12:
        periode = "PM"
        if heures > 12:
            heures -= 12
    elif heures == 0:
        heures = 0
    return (heures, minutes, secondes, periode)

def afficher_heure(heure_actuelle, alarme, choisir_12H_24H):
    while True:
        if choisir_12H_24H == 12:
            heures, minutes, secondes, periode = convertir_en_12H(heure_actuelle)
            heure_formatee = f"{heures:02d}:{minutes:02d}:{secondes:02d} {periode}"
        else:
            heure_formatee = f"{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}"
        
        print(f"{heure_formatee}", end="\r", flush=True)
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

        return heure_actuelle

def regler_alarme(heures, minutes, secondes, choisir_12H_24H):
    alarme = (heures, minutes, secondes) 
    if choisir_12H_24H == 12:
        heures, minutes, secondes, periode = convertir_en_12H(alarme)
        alarme_formatee = f"{heures:02d}:{minutes:02d}:{secondes:02d} {periode}"
    else:
        alarme_formatee = f"{alarme[0]:02d}:{alarme[1]:02d}:{alarme[2]:02d}"
    print(f"Alarme réglée pour {alarme_formatee}")
    return alarme

def main():
    # Initialiser l'heure actuelle avec l'heure locale 
    heure_actuelle = obtenir_heure_systeme()

    # Demander à l'utilisateur de choisir le format d'affichage de l'heure
    choisir_12H_24H = int(input("Entrez 12 pour le format 12 heures ou 24 pour le format 24 heures : "))

    # Demander à l'utilisateur d'entrer l'heure, les minutes et les secondes pour l'alarme :
    heures = int(input("Entrez l'heure pour l'alarme : ")) 
    minutes = int(input("Entrez les minutes pour l'alarme : ")) 
    secondes = int(input("Entrez les secondes pour l'alarme : "))

    # L'affichage de l'alarme est à quelle heure :
    alarme = regler_alarme(heures, minutes, secondes, choisir_12H_24H)

    # Lancer l'affichage de l'heure
    while True:
        heure_actuelle = afficher_heure(heure_actuelle, alarme, choisir_12H_24H)

# Démarrer le programme en appelant la fonction main
if __name__ == "__main__":
    main()