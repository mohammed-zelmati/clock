import time

# Obtenir l'heure locale actuelle
def obtenir_heure_locale():
    local_time = time.localtime()
    return (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)

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
def afficher_heure(h, m, s, choix):
    choix = input("Veux-tu le format PM/AM ? \nSi oui, tape simplement O, sinon tape sur n'importe quoi. \n").upper()
 
    periode = ""
    
    if choix =="O":
        periode = "PM"
        if h >= 12:
            periode = "PM"
            if h > 12:
                h -= 12
        elif h == 0:
            h = 12
            print(f"          {h:02} : {m:02} : {s:02} {periode}", end="\r")
                
    else:
        print(f"          {h:02} : {m:02} : {s:02} {periode}", end="\r")


# Convertir l'heure en format 12 heures (AM/PM)
def convertir_en_12H(h, m, s):
    periode = "AM"
    if h >= 12:
        periode = "PM"
        if h > 12:
            h -= 12
    elif h == 0:
        h = 12
    return (h, m, s, periode)

# Heure en format 24 heures
def horloge_24h(h, m, s, choix):
    
    print("")
    print("═════════════════════════════════════")
    print("************  Horloge  ************")
    print("═════════════════════════════════════")
    print("      CTRL + C pour les options      ")
    print("═════════════════════════════════════")
        
    try:
        while True:
            h, m, s = incrementer_heure(h, m, s)
            
            afficher_heure(h, m, s,choix)

            # Pause d'une seconde
            time.sleep(1)  
    # Control + C => mode alarme
    except KeyboardInterrupt:
            choix_options(h,m,s)


    
# Fonction pour afficher l'heure en format 12 heures
def horloge_12h(h, m, s):
    print("")
    print("═════════════════════════════════════")
    print("************  Horloge  ************")
    print("═════════════════════════════════════")
    print("        CTRL + C pour sortir        ")
    print("═════════════════════════════════════")
        
    try:
        while True:
            h, m, s = incrementer_heure(h, m, s)
            
            # Conversion et affichage au format 12 heures
            nouveau_tuple = convertir_en_12H(h, m, s)
            
            print(f"          {nouveau_tuple[0]:02} : {nouveau_tuple[1]:02} : {nouveau_tuple[2]:02} {nouveau_tuple[3]}", end="\r")
            
            # Pause d'une seconde
            time.sleep(1)  
    
    except KeyboardInterrupt:
        main()  # Control + C => retour à la fonction principale
def choix_options(h,m,s):
    print("=====================================")
    print("************  Options  ************")
    print("=====================================")
    choix = input(" Programmer une alarme: Tape A \n Passer en Mode AM/PM: Tape B \n Retour à l'horloge: Tape n'importe quoi \n") .upper()

    if choix == "A":
        mode_alarme()
    if choix == "B":
        afficher_heure(h, m, s)
            
    else:
        main()
# Fonction pour gérer le mode alarme
def mode_alarme():
    
    print("=====================================")
    print("************  Alarme  ************")
    print("=====================================")
    
    h_alarme = int(input("Veuillez renseigner l'heure :"))
    m_alarme = int(input("Veuillez renseigner les minutes :"))
    
    try:
        print(f"Alarme réglée pour {h_alarme:02} : {m_alarme:02}")
        
        # Vérification de la correspondance Heure = Heure alarme
        while True:
            heure_locale, minute_locale, seconde_locale = obtenir_heure_locale()  
            if h_alarme == heure_locale and m_alarme == minute_locale:
                try:
                    while True:
                        print("Alarme !!!!       ") 
                # Control +C = relance la fonction principale                        
                except KeyboardInterrupt:
                    main()  
            else:
                # Affichage de l'heure locale 
                print(f"{heure_locale:02} : {minute_locale:02} : {seconde_locale:02}", end="\r", flush=True)
    
    # Control +C = relance la fonction principale
    except KeyboardInterrupt:
        main()  

# Fonction principale pour lancer l'horloge
def main():

    # Récupère l'heure actuelle
    tuple_heure = obtenir_heure_locale()  
    
    
     # Assigne des valeurs aux variables utilisées
    s = tuple_heure[2]
    m = tuple_heure[1]
    h = tuple_heure[0]
    choix = input("Veux-tu le format PM/AM ? \nSi oui, tape simplement O, sinon tape sur n'importe quoi. \n").upper()
    #Appel de l'horloge
    horloge_24h(h, m, s, choix) 

# Lance la fonction proprement
if __name__ == "__main__":
    main()
