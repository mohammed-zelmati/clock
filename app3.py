import time
import threading
from playsound import playsound
import tkinter as tk

# Variables globales pour l'heure actuelle, l'alarme et le format d'affichage
heure_actuelle = (0, 0, 0)
alarme = None
format_24_heures = True  # Par défaut, utilisation du format 24 heures
en_pause = False  # Variable pour contrôler l'état de pause

def obtenir_heure_systeme():
    t = time.localtime()  # Récupère l'heure actuelle sous forme de struct_time
    return (t.tm_hour, t.tm_min, t.tm_sec)

def afficher_heure():
    global heure_actuelle, en_pause
    while True:
        time.sleep(1)
        if not en_pause:
            heure_actuelle = (heure_actuelle[0], heure_actuelle[1], heure_actuelle[2] + 1)  # incrémenter les secondes de 1
            if heure_actuelle[2] >= 60:
                heure_actuelle = (heure_actuelle[0], heure_actuelle[1] + 1, 0)
            if heure_actuelle[1] >= 60:
                heure_actuelle = (heure_actuelle[0] + 1, 0, heure_actuelle[2])
            if heure_actuelle[0] >= 24:
                heure_actuelle = (0, heure_actuelle[1], heure_actuelle[2])
        
            if alarme and heure_actuelle == alarme:
                playsound('alarme.mp3')  # Lire le fichier audio de l'alarme
        
            # Mise à jour de l'heure affichée dans l'interface Tkinter
            heure_formatee = formatter_heure(heure_actuelle)
            label_heure.config(text=heure_formatee)

def formatter_heure(heure):
    global format_24_heures
    if format_24_heures:
        return f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}"
    else:
        heures = heure[0] % 12
        if heures == 0:
            heures = 12
        periode = "AM" if heure[0] < 12 else "PM"
        return f"{heures:02d}:{heure[1]:02d}:{heure[2]:02d} {periode}"

def regler_heure(heure):
    global heure_actuelle
    heure_actuelle = heure



def regler_alarme():
    global alarme
    heures = int(entree_heures.get())
    minutes = int(entree_minutes.get())
    secondes = int(entree_secondes.get())
    alarme = (heures, minutes, secondes)
    print(f"Alarme réglée pour {alarme[0]:02d}:{alarme[1]:02d}:{alarme[2]:02d}")

def changer_format_heure():
    global format_24_heures
    format_24_heures = (format_24_heures_choice.get() == "24H")
    heure_formatee = formatter_heure(heure_actuelle)
    label_heure.config(text=heure_formatee)

def mettre_en_pause():
    global en_pause
    en_pause = True
    print("Horloge mise en pause")

def relancer():
    global en_pause
    en_pause = False
    print("Horloge relancée")

def main():
    global label_heure, entree_heures, entree_minutes, entree_secondes, format_24_heures_choice

    # Initialiser l'heure actuelle
    regler_heure(obtenir_heure_systeme())

    # Création de la fenêtre Tkinter
    fenetre = tk.Tk()
    fenetre.title("Horloge")

    # Création du label pour afficher l'heure avec des couleurs personnalisées
    label_heure = tk.Label(fenetre, font=("Helvetica", 48), bg="white", fg="brown")
    label_heure.pack()

    # Création des champs d'entrée pour régler l'alarme avec des couleurs personnalisées et des polices
    frame_alarme = tk.Frame(fenetre, bg="lightgrey")
    frame_alarme.pack(pady=20)
    tk.Label(frame_alarme, text="HH", font=("Helvetica", 12), bg="lightgrey", fg="brown").pack(side=tk.LEFT)
    entree_heures = tk.Entry(frame_alarme, width=3, font=("Helvetica", 12))
    entree_heures.pack(side=tk.LEFT)
    tk.Label(frame_alarme, text="MM", font=("Helvetica", 12), bg="lightgrey", fg="brown").pack(side=tk.LEFT)
    entree_minutes = tk.Entry(frame_alarme, width=3, font=("Helvetica", 12))
    entree_minutes.pack(side=tk.LEFT)
    tk.Label(frame_alarme, text="SS", font=("Helvetica", 12), bg="lightgrey", fg="brown").pack(side=tk.LEFT)
    entree_secondes = tk.Entry(frame_alarme, width=3, font=("Helvetica", 12))
    entree_secondes.pack(side=tk.LEFT)
    bouton_regler_alarme = tk.Button(frame_alarme, text="Régler l'alarme", command=regler_alarme, font=("Helvetica", 12), fg="brown")
    bouton_regler_alarme.pack(side=tk.LEFT, padx=10)

    # Création du menu déroulant pour choisir le format d'affichage de l'heure avec des couleurs personnalisées et des polices
    frame_format_heure = tk.Frame(fenetre, bg="lightgrey")
    frame_format_heure.pack(pady=20)
    tk.Label(frame_format_heure, text="Format 12H/24H", font=("Helvetica", 12), bg="lightgrey", fg="brown").pack(side=tk.LEFT)
    format_24_heures_choice = tk.StringVar(value="24H")
    choix_format_heure = tk.OptionMenu(frame_format_heure, format_24_heures_choice, "24H", "12H", command=lambda _: changer_format_heure())
    choix_format_heure.pack(side=tk.LEFT)
    choix_format_heure.config(font=("Helvetica", 12), fg="brown")

    # Création des boutons pour mettre en pause et relancer l'horloge avec des couleurs personnalisées et des polices
    frame_control = tk.Frame(fenetre, bg="lightgrey")
    frame_control.pack(pady=20)
    bouton_pause = tk.Button(frame_control, text="Pause", command=mettre_en_pause, font=("Helvetica", 12), fg="brown")
    bouton_pause.pack(side=tk.LEFT, padx=10)
    bouton_relancer = tk.Button(frame_control, text="Relancer", command=relancer, font=("Helvetica", 12), fg="brown")
    bouton_relancer.pack(side=tk.LEFT, padx=10)

    # Lancer l'affichage de l'heure dans un thread séparé
    thread_affichage = threading.Thread(target=afficher_heure)
    thread_affichage.daemon = True
    thread_affichage.start()

    # Démarrer la boucle principale de Tkinter
    fenetre.mainloop()

# Appel de la fonction main pour démarrer le programme
if __name__ == "__main__":
    main()
