import matplotlib.pyplot as plt
from random import randint
from time import time
import random

bubbleSortN =[ ]
bubbleSortT = []
insertion_sortN=[]
insertion_sortT=[]
mezclaT=[]
mezclaN=[]
quicksortN=[]
quicksortT=[]
selection_SortN=[]
selection_SortT=[]
maximo=500

def main():
    global maximo
    tam=100
    r=0
    while r <5:
        i=0
        bubbleSortN.append(tam)
        m=0
        while i <10:
            m+=medir_Tiempo(ordenamiento_burbuja, tam)
            i+=1
        r=(m/10)
        bubbleSortT.append(m/10)
        tam+=500
        maximo=maximo*2
    r=0
    tam=100
    maximo=500
    while r<5:
        i=0
        insertion_sortN.append(tam)
        m=0
        while i <10:
            m+=medir_Tiempo(insertion_sort, tam)
            i+=1
        r=(m/10)
        insertion_sortT.append(m/10)
        tam+=500
        maximo=maximo*2
    r=0
    tam=100
    maximo=500
    while r <5:
        i=0
        selection_SortN.append(tam)
        m=0
        while i <10:
            m+=medir_Tiempo(selection_Sort, tam)
            i+=1
        r=(m/10)
        selection_SortT.append(m/10)
        tam+=500
        maximo=maximo*2
    tam=100
    maximo=20000
    r=0
    while tam<100000:
        i=0
        mezclaN.append(tam)
        m=0
        while i <10:
            m+=medir_Tiempo(mezcla, tam)
            i+=1
        mezclaT.append(m/10)
        tam+=10000
        maximo=maximo*2
    r=tam
    tam=100
    maximo=20000
    while tam<100000:
        i=0
        quicksortN.append(tam)
        m=0
        while i <10:
            m+=medir_Tiempo(quicksort, tam)
            i+=1
        quicksortT.append(m/10)
        tam+=10000
        maximo=maximo*2
    plt.plot(selection_SortN,selection_SortT, label="selection_Sort")
    plt.plot(insertion_sortN,insertion_sortT, label="insertion_sort")
    plt.plot(bubbleSortN,bubbleSortT, label="BubbleSort")
    plt.plot(mezclaN,mezclaT, label="Merge")
    plt.plot(quicksortN,quicksortT, label="quicksort")
    plt.xlabel("Elementos")
    plt.ylabel("Segundos")
    plt.legend()
    plt.show()



def medir_Tiempo(funcion, n):
    L=generar(n)
    t1=time()
    funcion(L)
    t2 = time()
    return t2-t1


def  generar(tam):
    global maximo
    return [randint(0,maximo)for x in range(tam)]

def insertion_sort(L):
    """

    """
    if type(L) != list:
        raise Exception("Debe ser una lista")
    i=1
    while i<len(L):
        j=i
        while j>0 and L[j]<L[j-1]:
            L[j-1],L[j]=L[j],L[j-1]
            j=j-1
        i+=1
    return L

def mezcla(L):
    """
    """
    if len(L)==1:
        return L
    else:
        izq=L[:len(L)//2]
        der=L[len(L)//2:]
        izq=mezcla(izq)
        der=mezcla(der)
        return union(izq,der)
def union(L1,L2):
    resultado=[]
    while len(L1)>0 and len(L2)>0:
        if L1[0]<L2[0]:
            resultado.append(L1.pop(0))
        else:
            resultado.append(L2.pop(0))
    resultado.extend(L1+L2)
    return resultado

def quicksort(L):
    if len(L)<=1:
        return L
    else:
        pivote=L.pop(len(L)//2)
        menores=[x for x in L if x<pivote]
        mayores=[x for x in L if x>=pivote]
        return quicksort(menores)+[pivote]+quicksort(mayores)

def ordenamiento_burbuja(L):
    """
    Función que ordena una lista con metodo burbuja
    entradas y restricciones:
    L debe ser una lista de numeros enteros
    salidas:
    Las lista ordenada
    """
    intercambios=True
    i=0
    while i<len(L)-1 and intercambios:
        intercambios=False
        for j in range(0,len(L)-1-i,1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
                intercambios=True
        i=i+1
    return L

def selection_Sort(L):
    """
    Función que ordena una lista con metodo ordenamiento de selección
    entradas y restricciones:
    L debe ser una lista de numeros enteros
    salidas:
    Las lista ordenada
    """
    i=0
    def buscar_menor_posicion(L,i):
        menor =i
        for j in range(i+1,len(L)):
            if L[j] < L[menor]:
                menor= j
        return menor
    for i in range(0,len(L)-1):
        menor=buscar_menor_posicion(L,i)
        L[i],L[menor]=L[menor],L[i]
    return L

main()
