import time

def get_local_hour():
    local_time = time.localtime()
    return (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)
   

def alarm():
    h_alarm = int(input("Veuillez renseigner l'heure :"))
    m_alarm = int(input("Veuillez renseigner les minutes :"))

    print(f"Alarme réglée pour {h_alarm:02} : {m_alarm:02}")
          
    while True:
            local_time =get_local_hour()
            local_hour = local_time[0]
            local_minutes = local_time[1]
            local_secondes = local_time[2]

            if h_alarm == local_hour and m_alarm == local_minutes:
                try:
                      while True:
                            print("Alarm !!!!       ",end="\r")
                
                except KeyboardInterrupt:
                       clock()
            else:
                  print(f"{local_hour:02} : {local_minutes:02} : {local_secondes:02}",end="\r", flush=True)
                  
time.sleep(1)

# Fonction horloge
def clock():
    
    tuple = get_local_hour()

    # Valeurs secondes(s), minutes(m), heures(h)
    s = tuple[2]
    m = tuple[1]
    h = tuple[0]

    # Boucle infinie, incrémentée seconde par seconde, possibilité de stop (KeyboardInterrupt)
    try:  
        while True : 

            s += 1
            
            # règles d'incrémentation des secondes, minutes, heures
            if s == 60 :
                s = 0
                m += 1
            
            if m == 60 :
                m = 0
                h += 1   

            if h == 24 :
                h = 0
            
            # Création du tuple
            new_tuple = (h, m, s)

            # Affichage au format HH : MM : SS
            print(f"{new_tuple[0]:02} : {new_tuple[1]:02} : {new_tuple[2]:02}", end="\r")
            
            time.sleep(1)
    
    except KeyboardInterrupt:
                        alarm()
                       


clock()
