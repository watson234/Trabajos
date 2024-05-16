def main():
    """
    Función que recibe dos listas y retorna una lista con cada llave con sus factores
    Entradas y Restricciones:
    -Enteros: lista de enteros positiva
    -Factores: lista de enteros positivos
    Salidas:
    Diccionario con las llaves y sus divisbles
    """
    n= input("""Por favor ingrese dos listas una con los numeros enteros y otra con 
las que quiera hacer su divisibilidad: """ )
    lista=["0","1","2","3","4","5","6","7","8","9","[","]",","," "]
    for e in n:
            if e in lista:
               continue
            else:
                raise Exception(" Error el valor ingresado deben ser dos listas de numeros entero positivo")
    n=eval(n)
    if len(n)==2:
        if type(n[1])!=list:
            print(1)
            raise Exception(" Error a deben haber dos listas de numeros entero positivo")
        else:
            pass
    else:
        raise Exception(" Error a deben haber dos listas de numeros entero positivo")
    enteros=n[0]
    factores=n[1]
    return familias_aux(enteros, factores)
    
def familias(enteros, factores):
    family={}
    for r in factores:
        L=[]
        for i in enteros:
            if i%r==0:
                L.append(i)
                family[r]=L
    return family
