
def Borrado_Recursivo(L,e):
    """
    Función recursiva que recibe una lista de cualquier tipo, un valor a
    borrar y retorna la lista sin ese valor
    Entradas y Restricciones:
    -lista: lista de valores
    -e: valor a borrar
    Salidas:
    lista sin el valor
    """
    if type(L) != list:
        raise Exception(" Error L debe ser una lista")
    return borrado_Anidado(L,e)

def  borrado_Anidado(L,e):
    if L==[]:
        return []
    elif type(L[0])==list:
        return [borrado_Anidado(L[0], e)]+borrado_Anidado(L[1:],e)
    elif L[0]==e:
        return borrado_Anidado(L[1:], e)
    else:
        return [L[0]]+borrado_Anidado(L[1:], e)
