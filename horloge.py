import time

# extraction des éléments utiles depuis horloge locale
local_time = time.localtime()
tuple = (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)

def impression(new_tuple):
      print(f"{new_tuple[0]:02} : {new_tuple[1]:02} : {new_tuple[2]:02}", end="\r", flush=True)

# Fonction horloge
def clock():

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
            
            time.sleep(1)
    
    except KeyboardInterrupt:
                  print()
                  impression(new_tuple)


  

                        


clock()