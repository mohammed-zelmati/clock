import time

def get_local_hour():
    local_time = time.localtime()
    return (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)
   
def convertir_en_12H(tuple):
        h, m, s = tuple
        periode = "AM"
        if h >= 12:
            periode = "PM"
            if h > 12:
                 h -= 12
        elif h == 0:
                h= 12
        return (h, m, s, periode)
def clock_24h(tuple):
        try:  
                    while True : 
                        h, m, s = tuple
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
def clock_12h(tuple):
            try:  
                                while True : 
                                    h, m, s = tuple
                                    s += 1
                                    
                                    # règles d'incrémentation des secondes, minutes, heures
                                    if s == 60 :
                                        s = 0
                                        m += 1
                                    
                                    if m == 60 :
                                        m = 0
                                        h += 1   

                                    if h == 12:
                                        h = 0
                                    new_tuple = convertir_en_12H((h, m, s))

                                    # Affichage au format HH : MM : SS
                                    print(f"{new_tuple[0]:02} : {new_tuple[1]:02} : {new_tuple[2]:02} {new_tuple[3]}", end="\r")
                                    
                                    time.sleep(1)
                            
            except KeyboardInterrupt:
                main()

                      # Boucle infinie, incrémentée seconde par seconde, possibilité de stop (KeyboardInterrupt)
        
def alarm():
    print("Mode Alarme  ")
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
                       main()
            else:
                  print(f"{local_hour:02} : {local_minutes:02} : {local_secondes:02}",end="\r", flush=True)


# Fonction horloge
def main():
    tuple = get_local_hour()
    
    format_choice = input("Veux-tu le format PM/AM ? \nSi oui, tape simplement O, si non tape sur n'importe quoi. \n").upper()
            # Valeurs secondes(s), minutes(m), heures(h)
    s = tuple[2]
    m = tuple[1]
    h = tuple[0]
    
    if format_choice == "O":
        
        clock_12h(tuple)
        
    else:
       clock_24h(tuple)
        
            

main()
