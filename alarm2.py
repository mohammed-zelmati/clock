import time

def alarm():
    h_alarm = int(input("Veuillez renseigner l'heure :"))
    m_alarm = int(input("Veuillez renseigner les minutes :"))

    print(f"Alarme réglée pour {h_alarm:02} : {m_alarm:02}")
          
    while True:
            local_time = time.localtime()
            local_hour = local_time.tm_hour
            local_minutes = local_time.tm_min
            local_secondes = local_time.tm_sec

            if h_alarm == local_hour and m_alarm == local_minutes:
                try:
                      while True:
                            print("Alarm !!!!       ",end="\r")
                except KeyboardInterrupt:
                       
                       print(f"{local_time.tm_hour:02} : {local_time.tm_min:02} : {local_time.tm_sec}",end="\r", flush=True)
                       print(f"Alarm Off à: {local_time.tm_hour:02} : {local_time.tm_min:02}")
                       break
            else:
                  print(f"{local_time.tm_hour:02} : {local_time.tm_min:02} : {local_time.tm_sec:02}",end="\r", flush=True)
                  
time.sleep(1)

alarm()


