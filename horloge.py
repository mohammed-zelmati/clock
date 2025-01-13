import time
from playsound import playsound

# Obtient l'heure locale actuelle
def obtenir_heure_locale():
    t = time.localtime()
    return t.tm_hour, t.tm_min, t.tm_sec

# Incrémente l'heure, les minutes et les secondes
def incrementer_heure(h, m, s):
    s += 1
    if s == 60:  # Si les secondes atteignent 60, les réinitialise et incrémente les minutes
        s = 0
        m += 1
    if m == 60:  # Si les minutes atteignent 60, les réinitialise et incrémente les heures
        m = 0
        h += 1
    if h == 24:  # Si les heures atteignent 24, les réinitialise
        h = 0
    return h, m, s

# Affiche l'heure formatée HH : MM : SS
def afficher_heure(h, m, s):
    print(f"{h:02} : {m:02} : {s:02}", end="\r")

# Convertit l'heure de 24h en format AM/PM
def convertir_AM_PM(h, m, s):
    mode = "AM"
    if h >= 12:
        mode = "PM"
        if h > 12:
            h -= 12
    elif h == 0:
        h = 12
    return h, m, s, mode

# Gère l'alarme et la logique principale de l'affichage de l'heure
def gerer_et_definir_alarme(h, m, s, format_24h, alarme_h, alarme_m):
    try:
        while True:
            h, m, s = incrementer_heure(h, m, s)
            if format_24h:
                afficher_heure(h, m, s)
            else:
                h_12h, m_12h, s_12h, mode = convertir_AM_PM(h, m, s)
                print(f"{h_12h:02} : {m_12h:02} : {s_12h:02} {mode}", end="\r")
            # Vérifie si l'heure actuelle correspond à l'heure d'alarme
            if h == alarme_h and m == alarme_m:
                print("\n\n═══════ ALARME SONNE !!! ═══════\n\n")
                while True:
                    playsound('alarme.mp3')  # Joue le son de l'alarme
                    stop = input("Tapez 'S' pour arrêter l'alarme : ").upper()
                    if stop == "S":
                        return  # ne retourne rien après l'arrêt de l'alarme
            time.sleep(1)
    except KeyboardInterrupt:
        choix_options(h, m, s, format_24h)

# Affiche l'horloge en boucle
def horloge(h, m, s, format_24h=True):
    print("\n═════════════════════════════════════")
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
                h_12h, m_12h, s_12h, mode = convertir_AM_PM(h, m, s)
                print(f"{h_12h:02} : {m_12h:02} : {s_12h:02} {mode}", end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        choix_options(h, m, s, format_24h)

# Affiche les options et gère le choix de l'utilisateur
def choix_options(h, m, s, format_24h):
    print("\n=====================================")
    print("************  Options  ************")
    print("=====================================")
    choix = input(" Programmer une alarme: Tape A \n Passer en Mode AM/PM: Tape B \n Retour à l'horloge: Tape n'importe quoi \n").upper()
    if choix == "A":
        definir_alarme(h, m, s, format_24h)
    elif choix == "B":
        horloge(h, m, s, not format_24h)
    else:
        horloge(h, m, s, format_24h)

# Définit et gère une nouvelle alarme
def definir_alarme(h, m, s, format_24h):
    print("=====================================")
    print("************  Alarme  ************")
    print("=====================================")
    h_alarme = int(input("Veuillez renseigner l'heure de l'alarme : "))
    m_alarme = int(input("Veuillez renseigner les minutes de l'alarme : "))
    print(f"Alarme réglée pour {h_alarme:02} : {m_alarme:02}")
    gerer_et_definir_alarme(h, m, s, format_24h, h_alarme, m_alarme)

# Fonction principale qui démarre l'horloge
def main():
    h, m, s = obtenir_heure_locale()
    horloge(h, m, s)

# Point d'entrée du script
if __name__ == "__main__":
    main()