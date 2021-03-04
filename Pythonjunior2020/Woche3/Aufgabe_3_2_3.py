# 3.2.3, Woche 3, Block 2, Aufgabe 3

# Import 
from daten import punkte_liste
from turtle import *

# Funktionen
def gehe_wenn_nah(pointer):
        if distance(pointer) < 100:
            goto(pointer)
        else:
            goto(0,0)

# Main 
for i in range(0,len(punkte_liste)):
    gehe_wenn_nah(punkte_liste[i])