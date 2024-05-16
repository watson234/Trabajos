factorial_memo={}

def factorial(n):
    """Funciónb qur calcula el factprial de un entero:
       Entradas y restricciones:
       n: entero no negativo.
       Salidas:
       El factorial de n
    """
    if type(n) != int or n<0:
        raise Exception("n debe ser entero no negativo")
    if  n in factorial_memo:
        return factorial_memo[n]
    resultado=1
    for i in range(1,n+1):
        resultado+=i
    factorial_memo[n]=resultado
    return resultado

sumar_m_n_memo={}   
def sumar_m_n(m,n):
    """
    Función que suma los enteros en el rango [m...n]
    Entradas y restricciones:
    - m: número entero.
    - n: número entero, mayor o igual que m
    salidas:
    La suma de los enteros en el rango.
    """
    if type(m) != int:
        raise Exception("m debe ser un entero")
    if type(n) != int or n<m:
        raise Exception("n debe ser un numero entero mayor o igual a m")
    if (m,n) in sumar_m_n_memo:
        return sumar_m_n_memo[(m,n)]
    resultado=0
    for i in range(m, n+1):
        resultado+=i
    sumar_m_n_memo[(m,n)]= resultado
    return resultado

fib_memo={}
def fib(n):
    """
    Función que cacula el numero de fibonacci
    entradas:
    n numero entero
    restricciones:
    ninguna
    salidas:
    numero de fibonacci
    """
    a,b=0,1
    if (n) in fib_memo:
        return fib_memo[n]
    resultado=[a]
    for i in range (n):
        resultado.append(b)
        a, b = b, a+b
    fib_memo[n]=resultado
    return resultado

contar_digitos_memo={}
veces={}
def contar_digitos(n):
    """
    función para contar la cantidad de digitos en un numero
    entradas y restricciones:
    n:numero entero
    salidas:
    cantidad de digitos.
    """
    r=1
    if n in veces:
        r=veces[n]
        veces[n]=r+1
    else:
        veces[n]=1
    cantidad=1
    m=abs(n)
    if n in contar_digitos_memo:
        return contar_digitos_memo[n]
    while m > 9:
        cantidad = cantidad + 1
        m = m//10
    contar_digitos_memo[n]=cantidad
    return cantidad

def transformar(n):
    n=abs(n)
    m=str(n)
    h=len(m)
    i=0
    for i in range(h+1):
        n=n*10
        print(n)
