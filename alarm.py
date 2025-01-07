import time

# extraction des éléments utiles depuis horloge locale
local_time = time.localtime()
tuple = (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)

def impression(new_tuple):
      print(f"{new_tuple[0]:02} : {new_tuple[1]:02} : {new_tuple[2]:02}", end="\r", flush=True)


def alarm():
    h_alarm = int(input("Veuillez renseigner l'heure :"))
    m_alarm = int(input("Veuillez renseigner les minutes :"))

    print(f"Alarme réglée pour {h_alarm:02} : {m_alarm}")
          
    while True:
            local_time = time.localtime()
            local_hour = local_time.tm_hour
            local_minutes = local_time.tm_min
            local_secondes = local_time.tm_sec

            if h_alarm == local_hour and m_alarm == local_minutes:
                print("Alarm on")

            else:
                  print(f"{local_time.tm_hour:02} : {local_time.tm_min} : {local_time.tm_sec}",end="\r", flush=True)
                  
time.sleep(1)

alarm()


