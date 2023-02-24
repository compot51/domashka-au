from turtle import *
import math

ang = 100
div = 3  # во сколько раз меньше будет следующий проход рекурсии

def frac(scale, move):
    forward(move / div)
    if scale > 1:
        frac(scale - 1, move / div)
    forward(move / div)
    left(ang)
    forward(move / div)
    if scale > 1:
        frac(scale - 1, move / div)
    forward(move / div)
    right(ang)
    forward(move / div)
    if scale > 1:
        frac(scale - 1, move / div)
    forward(move / div)
    right(ang)
    forward(move / div)
    if scale > 1:
        frac(scale - 1, move / div)
    forward(move / div)
    left(ang)
    forward(move / div)
    if scale > 1:
        frac(scale - 1, move / div)
    forward(move / div)

# speed(0.01)
penup()
goto(-150, 0)
pendown()
frac(4, 50)
penup()
