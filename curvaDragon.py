from turtle import *
from colorsys import *
D="D"
I = "I"
def generar(n):
    if type(n) != int or n < 0:
        raise exception("n debe ser entero no negativo.")
    L=[D]
    for i in range(n):
        pos=0
        actual= D
        while pos <= len(L):
            L.insert(pos, actual)
            pos += 2
            actual = I if actual == D else D
    return L
        
def curva_Dragon(n, tamaño):
    if type(n) != int or n < 0:
        raise exception("n debe ser entero no negativo.")
    if type(tamaño) != int or tamaño < 1:
        raise Exception("Tamaño debe ser entero positivo")
    L= generar(n)
    tracer(0,0)
    hideturtle()
    reset()
    colormode(255)
    #pensize(1)
    bgcolor= (0,0,0)
    hue=0
    for letra in L:
        begin_fill()
        r, g, b= hsv_to_rgb(hue, 1, 255)
        color(int(r), int(g), int(b))
        forward(tamaño)
        hue+=0.005
        if letra == D:
            right(90)
        elif letra == I:
            left(90)
        end_fill()    
    forward(tamaño)
    update()
