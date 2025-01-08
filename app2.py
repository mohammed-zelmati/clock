import time

def obtenir_heure_systeme(): 
    t = time.localtime()  # Récupère l'heure locale actuelle sous forme de struct_time 
    return (t.tm_hour, t.tm_min, t.tm_sec)

def afficher_heure(heure_actuelle, alarme):
    while True:
        heure_formatee = f"{heure_actuelle[0]:02d}:{heure_actuelle[1]:02d}:{heure_actuelle[2]:02d}"
        print(f"\r{heure_formatee}", end="\r", flush=True)
        time.sleep(1)
        heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)  #incrémenter les secondes
        if heure_actuelle[2] >= 60:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)  #incrémenter les minutes
        if heure_actuelle[1] >= 60:
            heure_actuelle = (heure_actuelle[0] + 1, 0, heure_actuelle[2])  #incrémenter les heures
        if heure_actuelle[0] >= 24:
            heure_actuelle = (0, heure_actuelle[1], heure_actuelle[2])
        
        if alarme and heure_actuelle == alarme:
            print("\nAlarme !")  # Affiche "Alarme !" sur une nouvelle ligne

        return heure_actuelle

def regler_alarme(heures, minutes, secondes):
    alarme = (heures, minutes, secondes) 
    print(f"Alarme réglée pour {alarme[0]:02d}:{alarme[1]:02d}:{alarme[2]:02d}")
    return alarme

def main():
    # Initialiser l'heure actuelle avec l'heure locale 
    heure_actuelle = obtenir_heure_systeme()

    # Demander à l'utilisateur d'entrer l'heure, les minutes et les secondes pour l'alarme :
    heures = int(input("Entrez l'heure pour l'alarme : ")) 
    minutes = int(input("Entrez les minutes pour l'alarme : ")) 
    secondes = int(input("Entrez les secondes pour l'alarme : "))

    # L'affichage de l'alarme est à quelle heure :
    alarme = regler_alarme(heures, minutes, secondes)

    # Lancer l'affichage de l'heure
    while True:
        heure_actuelle = afficher_heure(heure_actuelle, alarme)

# Démarrer le programme en appelant la fonction main
if __name__ == "__main__":
    main()