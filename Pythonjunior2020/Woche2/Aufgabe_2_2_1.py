# 2.2.1, Woche 2, Block 2, Aufgabe 1

# Import 
from daten import ort
from daten import sitze

# IF-Statement
if sitze == 4 and ort == "Fenster" :
    print("Juhu, den Tisch nehmen wir.")
elif  sitze == 4 and ort == "Tür":
    print("Juhu, den Tisch nehmen wir.")
elif sitze != 4:
    print("Wir brauchen einen Tisch mit genau 4 Sitzen.")
else:
    print("Der Tisch hat zwar die richtige Größe, ist aber weder am Fenster noch an der Tür.")