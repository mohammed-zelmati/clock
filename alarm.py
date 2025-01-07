import time

# extraction des éléments utiles depuis horloge locale
local_time = time.localtime()
tuple = (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)

def impression(new_tuple):
      print(f"{new_tuple[0]:02} : {new_tuple[1]:02} : {new_tuple[2]:02}", end="\r", flush=True)


def alarm(new_tuple, h_alarm, m_alarm):
        
    if h_alarm == new_tuple[0] and m_alarm == new_tuple[1]:
        t = 0
        try:
            t = 0  
            while True:
                    t +=1
                    print("\nALARM !!!")
                    time.sleep(1)
        except KeyboardInterrupt:
            print("\nArrêt alarme")
            impression(new_tuple)        

        return True  
        
    return False


def clock():
    h_alarm = int(input("Veuillez renseigner l'heure :"))
    m_alarm = int(input("Veuillez renseigner les minutes :"))

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
           
           
            impression(new_tuple)
            
            if alarm(new_tuple, h_alarm, m_alarm):
                 break
            
            time.sleep(1)
    
    
    except KeyboardInterrupt:
        print("\nArrêt Horloge")
        impression(new_tuple)



clock()