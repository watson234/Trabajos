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
