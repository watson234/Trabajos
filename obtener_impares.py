def es_lista_enteros(L):
    if type(L) !=list:
        return False 
    for x in L:
        if type(x) != int:
            return False
    return True

def es_lista_enteros2(L):
    if type(L) !=list:
        return False 
    for x in L:
        if type(x) != int and type(x) !=float:
            return False
    return True
        
def obtener_impares(L):
    """
    Función que recibe uan lista de enteros y retorna dos listas cpn los pares e imapres separados:
    -L: lista de enteros
    Salidas.
    lista con dos elementos:pares e impares.
    """
    if not es_lista_enteros(L):
        raise Exception("L debe ser lista de enteros.")
    return[x for x in L if x%2==1]

def separar_pares_e_impares(L):
    if not es_lista_enteros(L):
        raise Exception("L debe ser lista de enteros.")
    M=[x for x in L if x%2==1]
    Y=[x for x in L if x%2==0]
    return [M, Y]

def sube_baja(n):
    """
    Funcion que recibe un valor n positivo y entero,
    retorne un valor que inicia desde 0 y sube hasta n y baja hasta 0:
    entradas y restricciones:
    -n= numero entero positivo
    salidas:
    lista que empiece en 0 y suba y baje de n.
    """
    if type(n) !=int and n <= 0:
        raise Exception("debe ser un numero entero possitivo")
    subebaja= [x for x in range(0,n+1)]+[x for x in range(n-1,-1,-1)]
    return subebaja

def Malespín(mensaje):
    """
    función para codificar un string con el lenguaje malespín.
    entradas y restricciones:
    -mensaje= es un string
    Salidas:
    -mensaje codificado con malespín.
    """

    if type(mensaje) !=str:
        raise Exception("El manesaje debe ser un string")
    n=len(mensaje)
    resultado=""
    mensaje=mensaje.lower()
    i=0
    lista=["a","e","b","t","f","g","i","o","m","p","á","é","í","ó"]
    lista2=("eatbgfoipméáíó")
    for i in range(0,n):
        letra=mensaje[i]
        if letra in lista:
            posicion= lista.index(letra)
            letra=lista2[posicion]
            resultado= resultado + letra
        else:
            resultado=resultado+letra
    print(resultado)

def Sumar_y_multiplicar_listas(lista):
    """
    función que sume una 
    lista de números y retorne la suma de todos los elementos
    y que haga los mismo pero con multiplicación
    Entradas y restricciones:
    -lista=lista de numeros enteros.
    restricciones
    -lista= lista debe ser numeros
    """
    if not es_lista_enteros2(lista):
         raise Exception("debe ser lista de enteros.")
    suma=0
    multiplicación=1
    for i in lista:
        suma+=i
    for e in lista:
        multiplicación*=e
    print("el resultado de la multilicación es:",multiplicación, " y es resultado de la suma es:", suma )
    
