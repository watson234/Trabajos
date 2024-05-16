from random import randint
from ordenamiento import *

def  generar(tam, maximo):
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
