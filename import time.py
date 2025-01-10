import time

# Fonction pour obtenir l'heure locale
def obtenir_heure_locale():
    heure_locale = time.localtime()
    return (heure_locale.tm_hour, heure_locale.tm_min, heure_locale.tm_sec)

# Règles d'incrémentation des secondes, minutes, heures
def incrementation_heure(s, m, h):
    # Pour les secondes
    if s == 60:
        s = 0
        m += 1

    # Pour les minutes
    if m == 60:
        m = 0
        h += 1

    # Pour les heures
    if h == 24:
        h = 0

    # Retourner les valeurs mises à jour
    return s, m, h

# Conversion de l'heure au format 12h
def convertir_en_12h(tuple):
    h, m, s = tuple
    # Par défaut, la période est AM (matin)
    periode = "AM"  
    
    # Passage au PM
    if h >= 12:
        periode = "PM"
        # Convertir en 12H
        if h > 12:
            h -= 12
    # Si l'heure est minuit, on la met à 12
    elif h == 0:
        h = 12

    # Retourne l'heure convertie
    return (h, m, s, periode)

#  Horloge 24h
def horloge_24h(tuple):
    try:
        while True:
            # Décomposer le tuple en heures, minutes et secondes
            h, m, s = tuple
            # Incrémentation des secondes
            s += 1

            # Mise à jour des secondes, minutes et heures si nécessaire
            incrementation_heure(s, m, h)

            # Nouveau tuple avec l'heure mise à jour
            nouveau_tuple = (h, m, s)

            # Affichage de l'heure au format HH : MM : SS
            print(f"{nouveau_tuple[0]:02} : {nouveau_tuple[1]:02} : {nouveau_tuple[2]:02}", end="\r")

            # Attente d'une seconde avant de réactualiser l'heure
            time.sleep(1)
    except KeyboardInterrupt:
        # Si Control+c passage en mode alarme
        alarme()

# Fonction pour afficher l'horloge en format 12h
def horloge_12h(tuple):
    try:
        while True:
            # Décomposer le tuple en heures, minutes et secondes
            h, m, s = tuple
            # Incrémentation des secondes
            s += 1

            # Mise à jour des secondes, minutes et heures si nécessaire
            incrementation_heure(h, m, s)

            # Conversion de l'heure au format 12h
            nouveau_tuple = convertir_en_12h((h, m, s))

            # Affichage de l'heure au format HH : MM : SS AM/PM
            print(f"{nouveau_tuple[0]:02} : {nouveau_tuple[1]:02} : {nouveau_tuple[2]:02} {nouveau_tuple[3]}", end="\r")

            # Attente d'une seconde avant de réactualiser l'heure
            time.sleep(1)
    except KeyboardInterrupt:
       # Si Control+c retour au main()
        main()

# Fonction pour gérer l'alarme
def alarme():
    # Demander l'heure et les minutes de l'alarme
    print("Mode Alarme")
    h_alarme = int(input("Veuillez renseigner l'heure :"))
    m_alarme = int(input("Veuillez renseigner les minutes :"))

    # Affichage de l'heure de l'alarme
    print(f"Alarme réglée pour {h_alarme:02} : {m_alarme:02}")

    while True:
        # Récupérer l'heure locale actuelle
        heure_locale = obtenir_heure_locale()
        h_locale = heure_locale[0]
        m_locale = heure_locale[1]
        s_locale = heure_locale[2]

        # Si l'heure locale correspond à l'heure de l'alarme, afficher "Alarme"
        if h_alarme == h_locale and m_alarme == m_locale:
            try:
                while True:
                    # Affichage continu du message "Alarme"
                    print("Alarme !!!!       ", end="\r")
            except KeyboardInterrupt:
                # En cas d'interruption (Ctrl+C), retourner à la fonction principale
                main()
        else:
            # Sinon, afficher l'heure actuelle en attente de l'alarme
            print(f"{h_locale:02} : {m_locale:02} : {s_locale:02}", end="\r", flush=True)

# Fonction principale
def main():
    # Récupérer l'heure locale au démarrage
    tuple = obtenir_heure_locale()

    # Demander à l'utilisateur s'il veut afficher l'heure au format PM/AM
    choix_format = input("Veux-tu le format PM/AM ? \nSi oui, tape O. Sinon, tape n'importe quoi. \n").upper()

    # Si l'utilisateur choisit PM/AM, afficher l'horloge en format 12h, sinon en format 24h
    if choix_format == "O":
        horloge_12h(tuple)
    else:
        horloge_24h(tuple)

# Lancer main() correctement
if __name__ == "__main__":
    main()