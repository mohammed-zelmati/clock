i+------------------------+
|  Lancement du programme |
|  principal (main)       |
+------------------------+
          |
          v
+------------------------+
|  obternir_heure_locale |
|  (Récupérer l'heure    |
|   locale actuelle)     |
+------------------------+
          |
          v
+------------------------+
|  incrementer_heure     |
|  et afficher_heure     |
|  (Incrémentation de     |
|   l'heure et affichage)|
+------------------------+
          |
          v
+------------------------+     (CTRL + C)
|  time.sleep(1)         |  ------------------------->
|  (Pause de 1 seconde)  |                        |
+------------------------+                        |
          |                                       v
          v                             +-----------------------+
+------------------------+             |   choix_options       |
|  Vérification de l'heure|             |  (Choisir une option) |
|  locale et de l'alarme  |             +-----------------------+
|  (mode_alarme)          |                     |
+------------------------+                     v
          |                            +---------------------+
          v                            |  mode_alarme        |
+------------------------+            |  (Mode Alarme)      |
|  Sonner l'alarme ?     |            +---------------------+
|  (Sonner l'alarme)     |                     |
+------------------------+                     v
          |                            +---------------------+
          v                            |  horloge_24h        |
+------------------------+            |  (Retour à l'horloge)|
|  Retour à l'horloge    |            +---------------------+
|  24h ou AM/PM          |                  
|  (horloge_12h)         |                  
+------------------------+
