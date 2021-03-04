# 3.1.2, Woche 3, Block 1, Aufgabe 2
# 3.1.2, Woche 3, Block 1, Aufgabe 2

# Imports
from turtle import *
import time

# Dekleration
durchlaeufe = 3

# Funktionen
def baum():
    setheading(90)
    forward(30)
    left(90)
    forward(30)
    right(120)
    forward(60)
    right(120)
    forward(60)
    right(120)
    forward(30)

def tanne():
    baum()
    baum()
    baum()

def zeichnen(x):
    for i in range(x):
        tanne()
        penup()
        goto((i+1)*75,0)
        pendown()


# Programm
zeichnen(durchlaeufe)

# Ende
time.sleep(10)