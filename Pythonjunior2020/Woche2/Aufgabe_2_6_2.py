# 2.6.2, Woche 2, Block 6, Aufgabe 2

# Imports
from daten import buchstabenanzahl_ist_gerade

# String als Satz
satz = "Du Suchender hast Mut und wirst die linke Allee nicht einschlagen sondern den Schatz entdecken sonst haben wir ihn gefunden"

# Split String
satz = satz.split(" ")

# IF Statement
for i in range(len(satz)):
    if buchstabenanzahl_ist_gerade(satz[i]) and satz[i][1] == "e":
        # Ausgabe 
        print(satz[i])