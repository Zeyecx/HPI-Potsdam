# 1.6.1, Woche 1, Block 6, Aufgabe 1

# Import
from turtle import *
import time

# Startpunkt
penup()
goto(-200,100) 
pendown()

# Quadrat
for i in range(0,4) :
    forward(400)
    right(90)

# Pause
time.sleep(5)