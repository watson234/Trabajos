import math
def entero_no_negativo(n):
    """
    Subrutima que revisa si un valor ws ntero no negatio.
    Entradas y restricciones:
    -n: el valor a analizar.
    Salidas:
    Ninguna, o error en caso de que no cumpla.
    """
    if type(n) != int or n < 0:
        raise Exception (f"n debe ser entero no negativo. Valor recibido: {n}")
def fact(n):
    """algoritmo que calcula en factorial de un entero
    restricciones y entradas:
    - n: enterono negativo.
    Salidas:
    El calculo del factorial de n."""

    entero_no_negativo(n)
    resultado = 1
    for i in range(1,n+1):
        resultado *=i
    return resultado

def permutaciones(n,r):
    """ Función que calcula las permutaciones de n elementos en r espacios.
        Entradas y Restricciones:
        - n: entero no negativo.
        - r: entero no negativo. r < n
        Salidas:
        El calculo de las permutaciones.
        """
    entero_no_negativo(n)
    if type(r)!= int or r < 0 or r >= n:
        raise Exception (f"n debe ser entero no negativo. Valor recibido: {n}")
    resultado=1
    for i in range (n,n-r,-1):
        resultado *=i
    return resultado

def Histograma(n):
    """
        Función que generar una barra de aca uno de sus digitos:
        Entradas y restricciones:
        Numero entero mayor a 0
        Salidas:
        los numeros de un numero entero representando su valor en barras
    """
    residuo=0
    numeros=("*")
    entero_no_negativo(n)
    while n >-1 :
        residuo=n%10
        n//=10
        if n == 0:
            n=-1
        print(residuo, " : ", numeros*residuo)
    return
        
def Diamante(n):
     """
        Función que imprima un diamante de orden n:
        Entradas y restricciones:
        -n:Numero entero mayor a 0
        Salidas:
        daiamante de formado por *
    """
     if type(n) != int or n < -1:
        raise Exception (f"n debe ser entero no negativo. Valor recibido: {n}")
     i=0
     m=0
     y=n
     if n ==0:
         y=y-1
         print(" "*y+"* "*i)
     else:
         for i in range (0,n+1):
             m+=1
             j=n
             if m==1:
                 print("  "*y+"*")
                 y=y-1
             elif m==2:
                  print("  "*y+"*"+" "+"*"+" "+"*")
                  y=y-1
             elif m==3:
                  print("  "*y+"*"+"1"*(m)+"*"+"1"*(m)+"*")
                  y=y-1
             elif m<=n:
                  print("  "*y+"*"+"1"*(m+1)+"*"+"1"*(m+1)+"*""!")
                  y=y-1
             elif m==n+1:
                  print(" "*y+"* "*(n*2+1)+""*m)
                  y=y-1
         i=1
         y=1
         i=n
         for i in range (n+1,0,-1):
             j=n
             m-=1
             if m==1:
                 print("  "*y+"*")
                 y=y+1
             elif m==3:
                  print("  "*y+"*"+" "*(m)+"*"+" "*(m)+"*")
                  y=y+1
             elif m<=n:
                  print("  "*y+"*"+" "*(m+1)+"*"+" "*(m+1)+"*""!")
                  y=y+1
             m-=1
         return

def ecuacion():
    """
        Función que de como resultado si el año es bisiesto:
        Entradas y restricciones:
        Numero entero
        Salidas:
        Resultado de la solucion
    """
    print("Ingrese los valores de a,b,c")
    a=float(input("A: "))
    b=float(input("B: "))
    c=float(input("C: "))
    discriminante=(b**2)-4*a*c
    if discriminante > 0:
            cuadratica= float((-b + math.sqrt(discriminante))/(2*a))
            cuadratica2= float((-b - math.sqrt(discriminante))/(2*a))
            print(f"la solución 2 es: {cuadratica} y la solución 1 es: {cuadratica2}")
    elif discriminante == 0:
        cuadratica= float(-b/(2*a))
        print(f"la solución es: {cuadratica}")
    else:
        print(f"no hay solución")

def año_bisiesto(n):
    """
        Función que calcula las soluciones reales de una ecuacion:
        Entradas y restricciones:
        Numero entero
        Salidas:
        Resultado de la solucion
        hecho por Kendall Amador
    """
    if type(n) != int or n < 1582:
        raise Exception (f"Debe ser un año mayor a 1582 dc. Valor recibido: {n}")
    if n % 4 ==0 and (not (n%100==0) or n %400==0):
                      print("el año es bisiesto")
    else:
        print("El año no es bisiesto")


