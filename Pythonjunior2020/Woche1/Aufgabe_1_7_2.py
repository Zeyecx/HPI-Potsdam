# 1.7.2 Woche 1, Block 7, Aufgabe 2

# Import
from turtle import *
from random import randint

# Malen Settings
speed(10)
bgcolor('black')

x = 1
while x < 400:

    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    colormode(255)
    pencolor(r, g, b)
    fd(50 + x)
    rt(90.911)

    x += 1

exitonclick()