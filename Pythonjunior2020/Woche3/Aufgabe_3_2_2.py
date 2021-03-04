# 3.2.2, Woche 3, Block 2, Aufgabe 2

# Import 
from daten import liste
from daten import anzahl
from daten import buchstabe

# Funktionen 
def stadt_mit(l,b,a):
    for i in range(0,len(l)):
        if l[i][0] == b and len(l[i]) == a:        
            print(l[i]) 

# Main
stadt_mit(liste,buchstabe,anzahl)