import time
from playsound import playsound

# Obtenir l'heure locale actuelle
def obtenir_heure_locale():
    t = time.localtime()
    return (t.tm_hour, t.tm_min, t.tm_sec)

# Règles d'incrémentation
def incrementer_heure(h, m, s):
    s += 1      
    if s == 60:
        s = 0
        m += 1
    
    if m == 60:
        m = 0
        h += 1   
    if h == 24:
        h = 0
    
    return h, m, s

# Afficher l'heure dans le format HH:MM:SS
def afficher_heure(h, m, s):
    print(f"            {h:02} : {m:02} : {s:02}", end="\r")

# Convertir l'heure en format 12 heures (AM/PM)
def convertir_AM_PM(h, m, s):
    periode = "AM"
    if h >= 12:
        periode = "PM"
        if h > 12:
            h -= 12
    elif h == 0:
        h = 12
    return (h, m, s, periode)

# Fonction horloge pour afficher l'heure en format 24 heures ou 12 heures (AM/PM)
def horloge(h, m, s, format_24h=True, alarme_h=None, alarme_m=None):
    print("")
    print("═════════════════════════════════════")
    print("************  Horloge  ************")
    print("═════════════════════════════════════")
    print("        CTRL + C pour les options        ")
    print("═════════════════════════════════════")
        
    try:
        while True:
            h, m, s = incrementer_heure(h, m, s)
            
            if format_24h:
                afficher_heure(h, m, s)
            else:
                nouveau_tuple = convertir_AM_PM(h, m, s)
                print(f"          {nouveau_tuple[0]:02} : {nouveau_tuple[1]:02} : {nouveau_tuple[2]:02} {nouveau_tuple[3]}", end="\r")
            
            # Vérification de l'alarme
            if alarme_h is not None and alarme_m is not None:
                if h == alarme_h and m == alarme_m:
                    print("\n\n═══════ ALARME SONNE !!! ═══════\n\n")
                    playsound('alarme.mp3')  # Lire le fichier audio de l'alarme
                    break

            # Pause d'une seconde
            time.sleep(1)  

    except KeyboardInterrupt:
        choix_options(h, m, s, format_24h)

def choix_options(h, m, s, format_24h):
    print("=====================================")
    print("************  Options  ************")
    print("=====================================")
    choix = input(" Programmer une alarme: Tape A \n Passer en Mode AM/PM: Tape B \n Retour à l'horloge: Tape n'importe quoi \n").upper()

    if choix == "A":
        mode_alarme(h, m, s, format_24h)
    elif choix == "B":
        horloge(h, m, s, not format_24h)
    else:
        main()

# Fonction pour gérer le mode alarme
def mode_alarme(h, m, s, format_24h):
    print("=====================================")
    print("************  Alarme  ************")
    print("=====================================")
    
    h_alarme = int(input("Veuillez renseigner l'heure : "))
    m_alarme = int(input("Veuillez renseigner les minutes : "))
    
    print(f"Alarme réglée pour {h_alarme:02} : {m_alarme:02}")
    
    horloge(h, m, s, format_24h, alarme_h=h_alarme, alarme_m=m_alarme)

# Fonction principale pour lancer l'horloge
def main():
    # Récupère l'heure actuelle
    h, m, s = obtenir_heure_locale()
    
    # Appel de l'horloge
    horloge(h, m, s)  

# Lance la fonction proprement
if __name__ == "__main__":
    main()