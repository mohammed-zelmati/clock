
import time

# extraction des éléments utiles depuis horloge locale
local_time = time.localtime()
tuple = (local_time.tm_hour, local_time.tm_min, local_time.tm_sec)

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
            print(f"{new_tuple[0]:02} : {new_tuple[1]:02} : {new_tuple[2]:02}", end="\r")
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        print(f"Arrêt horloge à {new_tuple[0]:02} : {new_tuple[1]:02} : {new_tuple[2]:02}")



import tkinter as tk
import math
import time

def update_clock():
    """Met à jour les aiguilles de l'horloge en fonction de l'heure actuelle."""
    # Obtenir l'heure actuelle
    now = time.localtime()
    hours = now.tm_hour % 12  # Convertir en format 12 heures
    minutes = now.tm_min
    seconds = now.tm_sec

    # Calculer les angles des aiguilles
    hour_angle = math.radians((hours + minutes / 60) * 30 - 90)  # 30° par heure
    minute_angle = math.radians((minutes + seconds / 60) * 6 - 90)  # 6° par minute
    second_angle = math.radians(seconds * 6 - 90)  # 6° par seconde

    # Déplacer les aiguilles
    canvas.coords(hour_hand, 
                  200, 200, 
                  200 + 50 * math.cos(hour_angle), 
                  200 + 50 * math.sin(hour_angle))
    canvas.coords(minute_hand, 
                  200, 200, 
                  200 + 70 * math.cos(minute_angle), 
                  200 + 70 * math.sin(minute_angle))
    canvas.coords(second_hand, 
                  200, 200, 
                  200 + 90 * math.cos(second_angle), 
                  200 + 90 * math.sin(second_angle))

    # Planifier la prochaine mise à jour
    root.after(1000, update_clock)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Horloge Analogique")

# Créer un canvas pour dessiner l'horloge
canvas = tk.Canvas(root, width=400, height=400, bg="beige")
canvas.pack()

# Dessiner le cadran de l'horloge
canvas.create_oval(50, 50, 350, 350, outline="black", width=2)  # Cercle extérieur

# Ajouter les chiffres romains
roman_numerals = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI",
    7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII"
}
for hour, numeral in roman_numerals.items():
    angle = math.radians(hour * 30 - 90)  # Positionner les chiffres
    x = 200 + 130 * math.cos(angle)
    y = 200 + 130 * math.sin(angle)
    canvas.create_text(x, y, text=numeral, font=("Helvetica", 14, "bold"))

# Dessiner les graduations pour les minutes/heures
for i in range(60):
    angle = math.radians(i * 6)
    x_start = 200 + 140 * math.cos(angle)
    y_start = 200 + 140 * math.sin(angle)
    x_end = 200 + 150 * math.cos(angle)
    y_end = 200 + 150 * math.sin(angle)
    width = 2 if i % 5 == 0 else 1  # Les heures sont plus épaisses
    canvas.create_line(x_start, y_start, x_end, y_end, fill="black", width=width)

# Ajouter les aiguilles
hour_hand = canvas.create_line(200, 200, 200, 150, width=6, fill="black")
minute_hand = canvas.create_line(200, 200, 200, 120, width=4, fill="black")
second_hand = canvas.create_line(200, 200, 200, 110, width=2, fill="black")

# Lancer la mise à jour de l'horloge
update_clock()

# Démarrer la boucle principale de tkinter
root.mainloop()

clock()