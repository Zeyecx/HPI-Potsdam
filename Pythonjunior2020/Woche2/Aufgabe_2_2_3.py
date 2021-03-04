# 2.2.3, Woche 2, Block 2, Aufgabe 3

# Import
from daten import form
from turtle import *

# SetUp
penup()
goto(-200,100) 
pendown()


# IF - Statement
if form == "Dreieck" : 
    # Dreieck
    for i in range(0, 3):
        forward(100)
        left(120)
elif form == "Viereck":
    # Viereck
    for i in range(0, 4):
        forward(100)
        left(90)
else: 
    print("Error")
