from turtle import *
from random import *
Rel=7/8
ang=25
RAND = 30
RANDT = 80
GROSORTRONCO = 0
TAMINIC = 20
tHoja = 25
aHoja = 35
prof = 6
Ctronco =(100,80,0)
Ctroncovar = 30
Chojas = (66,190,9)
ChojasVar =100
Cfondo = (255, 255, 255)

def arbol(t,d):
    """
    Función recursiva que dibuja el arbol con sus parametros
    Entradas y restricciones:
    parametros del arbol deben ser un numero entero positivo
    salidas:
    Dibujo del arbol
    """
    if d==0:
        forward(t)
        hoja(tHoja, aHoja)
        penup()
        back(t)
        pendown()
        return
    else:
        angulo1= ang+randrange(-RAND, RAND+1)
        angulo2= ang+randrange(-RAND, RAND+1)
        tamaño= t+t*randrange(-RANDT, RANDT+1)/100
        color_Tronco = variación_color(Ctronco, Ctroncovar)
        color(color_Tronco)
        pensize(d+GROSORTRONCO)
        forward(tamaño)
        left(angulo1)
        arbol(t*Rel,d-1)
        right(angulo1+angulo2)
        arbol(t*Rel, d-1)
        color(color_Tronco)
        left(angulo2)
        penup()
        back(tamaño)
        pendown()
        
    
def hoja(tHoja, aHoja):
    """
    Función que define los parametros de la Hoja y la dibuja
    Entradas y restricciones:
    Los valores de la Hoja
    salidas:
    Dibujo de la Hoja"""
    color(variación_color(Chojas, ChojasVar))
    begin_fill()
    right(aHoja/2)
    circle(tHoja,aHoja)
    left(180-aHoja)
    circle(tHoja, aHoja)
    left(180-aHoja/2)
    end_fill()

def variación_color(color, var):
    Rd = randrange(-var, var+1)
    Gd = randrange(-var, var+1)
    Bd = randrange(-var, var+1)
    R, G, B = color
    R += Rd
    G += Gd
    B += Bd
    if R > 255:
        R = 255
    elif R < 0:
        R = 0
    if G > 255:
        G = 255
    elif G < 0:
        G = 0
    if B > 255:
        B = 255
    elif B < 0:
        B = 0
    return R, G, B

def init(TAMANIC,Chojas):
    tracer(0,0)
    colormode(255)
    penup()
    pendown()
    hideturtle()
    color(Ctronco)
    bgcolor(Cfondo)
    arbol(TAMINIC, prof)
    #done()
    update()

def bosque():
    """
    Función principal del arbol
    entradas y restricciones:
    Largo del arbol: valor entero positivo
    prof: profundidad del arbol entero positivo
    Salidas:
    Bosque de arboles según los parametros ingresados
    """
    r=-1
    s=0
    arboles=int(input("Ingrese la cantidad de arboles: "))
    n=arboles
    prueba= True
    while prueba:
        if type(arboles) != int and arboles>0:
            arboles=int(input("Error debe ser un numero entero positivo mayor\
                              a 30 por favor volver a ingresar valor: "))
            prueba = True
        else:
            prueba = False
    return bosque_aux(arboles,n,s,r)

def bosque_aux(arboles,n,s,r):
        global TAMINIC
        global Chojas
        penup()
        amarillo=(255,255,0)
        rojo=(255,0,0)
        verde=(0,143,57)
        rosado=(234,137,154)
        morado=(87,35,100)
        if s <2 or (s>13 and s<=15) :
            Chojas=amarillo
        elif s<4 or (s>11 and s<=13):
            Chojas=rojo
        elif s <6 or (s>9 and s<=11):
            Chojas=verde
        elif s <8:
            Chojas=rosado
        else:
            Chojas=morado
        TAMINIC=randrange((10-r),(20-r))
        back(15)
        pendown()
        if arboles ==0:
            return
        elif arboles==n:
            penup()
            left(90)
            back(225)
            pendown()
            init(TAMINIC,Chojas)
            return bosque_aux(arboles-1,n,s,r)
        else:
            if arboles %2!=0:
                s+=1
                if s == 15:
                    s=0
                    r+=1
                    penup()
                    home()
                    left(90)
                    forward(75*r-120)
                    pendown()
                    TAMINIC-=1
                penup()
                left(90)
                back(75*s)
                right(90)
                pendown()
                init(TAMINIC,Chojas)
                return bosque_aux(arboles-1,n,s,r)
            if arboles %2==0:
                s+=1
                if s == 15:
                    s=0
                    r+=1
                    penup()
                    home()
                    left(90)
                    forward(75*r-120)
                    pendown()
                    TAMINIC-=1
                penup()
                left(90)
                forward(75*s)
                right(90)
                pendown()
                init(TAMINIC,Chojas)
                return bosque_aux(arboles-1,n,s,r)
    
bosque()
