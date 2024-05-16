def Lista_ascendente(n):
    """
    Función recursiva que ordena una lista de manera ascendente hasta n-1
    entradas y restricciones:
    -n: numero entero positivo
    salidas:
    Lista ascendente hasta n-1
    hecho por: kendall y Sebastian
    """
    if type(n) != int or n<0:
        raise Exception("el numero ingresado debe ser un entero positivo")
    return ascendente_aux(n)

def ascendente_aux(n):
    lista=[]
    if n ==0:
        return []
    else:
        i=n-1
        lista=lista+[i]
        return ascendente_aux(n-1)+lista
    
def eliminar_elemento(L,n):
    """
     Función recursiva que elimina todos los elementos n de una lista
     entradas y restricciones:
     -L debe ser una lista
     -n cualquier elemento a eliminar
     salidas:
     lista con elemento eliminado
     hecho por: kendall y Sebastian
     """
    if type(L) != list:
        raise Exception("debe ser una lista")
    return  eliminar_aux(L,n)

def eliminar_aux(L,n):
    if L ==[]:
        return []
    if n != L[0]:
        return [L[0]] + eliminar_aux(L[1:],n)
    else:
        return eliminar_aux(L[1:],n)
        
