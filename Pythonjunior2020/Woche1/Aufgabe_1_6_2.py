# 1.6.2, Woche 1, Block 6, Aufgabe 2

# Import
from turtle import *
import time

# Startpunkt
penup()
goto(-200,10) 
pendown()

# Dreieck
for i in range(0, 3):
    forward(400)
    left(120)

# Pause
time.sleep(3)