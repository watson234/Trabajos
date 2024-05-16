from random import *
from tabulate import *

def crear_matriz_valor(filas, cols, valor=0):
    """
    Función que rea una matriz rectangular inicializada
    con el valor indicado
    Entradas y restricciones:
    - filas: Entero positivo
    - cols: entero positivo
    - valor: cualquier valor
    Salidas:
    La matriz inicializada
    """
    if type(filas)!= int or filas <1:
        raise Exception("Filas debe ser entero positivo.")
    if type(cols) != int or cols<1:
        raise Exception("Cols debe ser un entero positivo")
    M = []
    for f in range(filas):
        fila=[valor for c in range(cols)]
        M.append(fila)
    return M

def Matrix2(filas, cols, valor=0):
    if type(filas)!= int or filas <1:
        raise Exception("Filas debe ser entero positivo.")
    if type(cols) != int or cols<1:
        raise Exception("Cols debe ser un entero positivo")
    M=[[valor for c in range(cols)] for f in range(filas)]
    
def crear_matrix_random(filas, cols, minimo, maximo):
    """
    Función que rea una matriz rectangular inicializada
    con el valor indicado
    Entradas y restricciones:
    - filas: Entero positivo
    - cols: entero positivo
    - minimo: entero
    -maximo: entero mayor o igual a minimo
    Salidas:
    La matriz inicializada
    """
    if type(filas)!= int or filas <1:
        raise Exception("Filas debe ser entero positivo.")
    if type(cols) != int or cols<1:
        raise Exception("Cols debe ser un entero positivo")
    if type(minimo)!= int:
        raise Exception("minimo debe ser entero")
    if type(maximo) != int or maximo<minimo:
        raise Exception("maximo debe ser un entero positivo mayor o igual a minimo")
    return[[randint(minimo,maximo) for c in range(cols)] for f in range(filas)]

def validar(M):
    """
    Función booleana que dice si M  es una matriz valida.
    Entradas y restriciiones:
    M=objeto a validar
    Salidas:
    True si es una matriz valida,
    False si no
    """
    if type(M) !=list:
        return False
    for fila in M:
        if type(fila) != list:
            return False
        if len(fila) != len(M[0]):
            return False
    return True

def imprimir(M):
    """
    Función que imprime una matriz en consola
    Entradas y restricciones:
    - M : Matriz valida
    Salidas:
    Impresión de M en la pantalla
    """
    if not validar(M):
        raise Exception("M debe ser una matriz válida.")
    print(tabulate(M, tablefmt= "rounded_grid"))

def filas(M):
    return len(M)

def cols(M):
    return len(M[0])

def suma(A, B):
    """
    Función que suma dos matrices.
    entrdas y restricciones:
    -A,B: dos matrices con las mismas dimenesiones
    Salidas:
    Resultado de A+B
    """
    if not validar(A) or not validar(B):
        raise Exception("A y B deben ser una matrices válida.")
    if filas(A) == filas(B):
        raise Exception("A y B debe tener las mismas dimensiones")
    C = crear_matriz_valor(filas(A), cols(A),0)
    for f in range(filas(A)):
        for c in range(cols(A)):
            C[f][c]=A[f][c]+B[f][c]
    return imprimir(C)

def multi(A,e):
    """
    Función que multiplica A por un escalar.
    entrdas y restricciones:
    -A: matriz valida
    - e = valor numerico
    Salidas:
    Resultado de e *A
    """
    if not validar(A):
         raise Exception("A debe ser una matriz válida.")
    if type(e) not in(int, float):
        raise Exception("e debe ser un valor numerico")
    C = crear_matriz_valor(filas(A), cols(A),0)
    imprimir(A)
    for f in range(filas(A)):
        for c in range(cols(A)):
            C[f][c]=A[f][c]*e
    return imprimir(C)
