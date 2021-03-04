# Aufgabe 3.1.4, Woche 3, Block 1, Aufgabe 4

# Imports 
from turtle import *

# Dekleration
winkel = 90

# Funktionen
def dreieck():
    winkel = 120
    forward(100)
    left(winkel)
    forward(100)
    winkel = 120
    left(winkel)
    forward(100)
    ausgabe = 'Dreieck'
    len = 3
    print(ausgabe)
    return 'Quadrat'



dreieck()

def quadrat( ):
 # Eine Variable, deren Name mit einem Unterstrich _ beginnt, wird nicht als unbenutzt angezeigt (siehe Tipp oben).    
 for _durchlauf in range (4):
  forward(50)
  forward(50)
  right(winkel)
 if (winkel == winkel):
  return "Quadrat"   

rueckgabe = quadrat()
print(rueckgabe)
'Ende der Zeichnung'
