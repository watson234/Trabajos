def contar_digitos(n):
    cantidad=1
    while n > 9:
        cantidad = cantidad + 1
        n = n//10
    return cantidad
def main():
    """
    Programa que cuenta los digiatos de un numero entero,
    Entradas y restricciones:
    -n : un entero no negativo
    Salidas:
    La cantidad de digitos de n
    """
    n = int(input("Escriba el numero a analizar: "))
    if n>= 0:
        print("la cantidad de digitos: ", contar_digitos(n))
    else:
        print("Error: n debe ser un entero no negativo")
main()
