# Die Bibliothek ist nur dem der HPI nachgemacht.

# Imports
from random import randint

# Aufgabe 2.1.1
alter = randint(1, 20)

# Aufgabe 2.1.2
namen = ["Alex", "Paul", "Otto", "Tim", "Theresa","Karl"]
name = namen[randint(0, len(namen)-1)]

# Aufgabe 2.1.3
max_anzahl = randint(1, 6)
belegt = randint(0, max_anzahl)

# Aufgabe 2.2.1
orte = ["Wand", "Tür", "Salatbar", "Fenster", "Büffet"]
ort = orte[randint(0, len(orte)-1)]
sitze = randint(1,6)

# Aufgabe 2.2.2
hauptspeisen = ["Nudeln", "Kartoffeln", "Pommes", "Reis"  ]
hauptspeise = hauptspeisen[randint(0, len(hauptspeisen)-1)]
nachtische = ["Obstsalat", "Erdbeerjoghurt", "Schokoladenpudding" ]
nachtisch = nachtische[randint(0, len(nachtische)-1)]

# Aufgabe 2.2.3
formen = ["Dreieck", "Viereck"]
form = formen[randint(0,len(formen)-1)]

# Aufgabe 2.5.2
hinweise = ['Baum', 'Haus', 'Ball']

# Aufgabe 2.6.2 
def buchstabenanzahl_ist_gerade(zeichenkette):
    return len(zeichenkette) % 2 == 0