import time

def convertir_AM_PM(h, m, s):
    periode = "AM"
    if h >= 12:
        periode = "PM"
        if h > 12:
            h -= 12
    elif h == 0:
        h = 12
    return h, m, s, periode

def clock(h, m, s, format_AM):
    try:
        while True:
            s += 1
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1
            
            if format_AM:
                if h == 12:
                    h = 0
                h, m, s, periode = convertir_AM_PM(h, m, s)
                print(f"{h:02} : {m:02} : {s:02} {periode}", end="\r")
            else:
                if h == 24:
                    h = 0
                print(f"{h:02} : {m:02} : {s:02}", end="\r")
                
            time.sleep(1)
    except KeyboardInterrupt:
        alarm(format_AM)

def alarm(format_AM):
    print("Mode Alarme")
    h_alarm = int(input("Veuillez renseigner l'heure :"))
    m_alarm = int(input("Veuillez renseigner les minutes :"))
    print(f"Alarme réglée pour {h_alarm:02} : {m_alarm:02}")

    while True:
        local_hour, local_minutes, local_secondes = affiche_heure()
        if h_alarm == local_hour and m_alarm == local_minutes:
            try:
                end_time = time.time() + 30  # 30 secondes de sonnerie d'alarme
                while time.time() < end_time:
                    print("Alarm !!!!       ", end="\r")
                    # Ajoutez un son d'alarme ici si nécessaire
                    time.sleep(1)
                break
            except KeyboardInterrupt:
                main()
        else:
            print(f"{local_hour:02} : {local_minutes:02} : {local_secondes:02}", end="\r", flush=True)
    
    # Afficher l'heure actuelle après 30 secondes de sonnerie
    h, m, s = affiche_heure()
    if format_AM:
        h, m, s, periode = convertir_AM_PM(h, m, s)
        print(f"Heure actuelle : {h:02} : {m:02} : {s:02} {periode}")
    else:
        print(f"Heure actuelle : {h:02} : {m:02} : {s:02}")

def affiche_heure():
    t = time.localtime()
    return t.tm_hour, t.tm_min, t.tm_sec

def main():
    h, m, s = affiche_heure()
    format_choix = input("Veux-tu le format PM/AM ? \nSi oui, tape simplement O, sinon tape sur n'importe quoi. \n").upper()
    format_AM = (format_choix == "O")
    clock(h, m, s, format_AM)

if __name__ == "__main__":
    main()
