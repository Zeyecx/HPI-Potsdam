# 2.4.2, Woche 2, Block 4, Aufgabe 2

# Listen anlegen
erste_Gruppe = ["Schere", "Stift", "Regenjacke","Lampe"]
zweite_Gruppe = ["Regenschirm", "Schaufel", "Schreibblock"]

# Liste ergaenzen
Gruppe = []
Gruppe += erste_Gruppe
Gruppe += zweite_Gruppe

# Liste Ausgeben
for i in range(len(Gruppe)) :
    print(Gruppe[i])

# Leange
print("Die Liste Gruppe hat",len(Gruppe)," Elemente")