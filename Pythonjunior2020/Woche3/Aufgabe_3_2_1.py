# 3.2.1, Woche 3, Block 2, Aufgabe 1

# Import 
from daten import anzahl_hinfahrt, anzahl_rueckfahrt

# Funktionen
def berechne_anzahl(x,y):
    return x+y
    
# Main 
calc = berechne_anzahl(anzahl_hinfahrt,anzahl_rueckfahrt)
print(anzahl_hinfahrt,"+",anzahl_rueckfahrt,"=",calc)