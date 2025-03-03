import time
from playsound import playsound

# Get the current local time
def obtenir_heure_locale():
    t = time.localtime()
    return t.tm_hour, t.tm_min, t.tm_sec

# Increment the hours, minutes, and seconds
def incrementer_heure(h, m, s):
    s += 1
    if s == 60:  # If seconds reach 60, reset and increment minutes
        s = 0
        m += 1
    if m == 60:  # If minutes reach 60, reset and increment hours
        m = 0
        h += 1
    if h == 24:  # If hours reach 24, reset
        h = 0
    return h, m, s

# Display the time in HH:MM:SS format
def afficher_heure(h, m, s):
    print(f"{h:02} : {m:02} : {s:02}", end="\r")

# Convert 24-hour time to AM/PM format
def convertir_AM_PM(h, m, s):
    mode = "AM"
    if h >= 12:
        mode = "PM"
        if h > 12:
            h -= 12
    elif h == 0:
        h = 12
    return h, m, s, mode

# Manage the alarm and main time display logic
def gerer_et_definir_alarme(h, m, s, format_24h, alarme_h, alarme_m):
    try:
        while True:
            h, m, s = incrementer_heure(h, m, s)
            if format_24h:
                afficher_heure(h, m, s)
            else:
                h_12h, m_12h, s_12h, mode = convertir_AM_PM(h, m, s)
                print(f"{h_12h:02} : {m_12h:02} : {s_12h:02} {mode}", end="\r")
            # Check if the current time matches the alarm time
            if h == alarme_h and m == alarme_m:
                print("\n\n═══════ ALARM RINGING!!! ═══════\n\n")
                while True:
                    playsound('alarme.mp3')  # Play the alarm sound
                    stop = input("Type 'S' to stop the alarm: ").upper()
                    if stop == "S":
                        return  # Exit after stopping the alarm
            time.sleep(1)
    except KeyboardInterrupt:
        choix_options(h, m, s, format_24h)

# Display the clock in a loop
def horloge(h, m, s, format_24h=True):
    print("\n═════════════════════════════════════")
    print("************  Clock  ************")
    print("═════════════════════════════════════")
    print("        CTRL + C for options        ")
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

# Display options and handle user choice
def choix_options(h, m, s, format_24h):
    print("\n=====================================")
    print("************  Options  ************")
    print("=====================================")
    choix = input(" Set an alarm: Type A \n Switch to AM/PM Mode: Type B \n Return to clock: Type anything \n").upper()
    if choix == "A":
        definir_alarme(h, m, s, format_24h)
    elif choix == "B":
        horloge(h, m, s, not format_24h)
    else:
        horloge(h, m, s, format_24h)

# Set and manage a new alarm
def definir_alarme(h, m, s, format_24h):
    print("=====================================")
    print("************  Alarm  ************")
    print("=====================================")
    h_alarme = int(input("Enter the alarm hour: "))
    m_alarme = int(input("Enter the alarm minutes: "))
    print(f"Alarm set for {h_alarme:02} : {m_alarme:02}")
    gerer_et_definir_alarme(h, m, s, format_24h, h_alarme, m_alarme)

# Main function to start the clock
def main():
    h, m, s = obtenir_heure_locale()
    horloge(h, m, s)

# Entry point of the script
if __name__ == "__main__":
    main()
