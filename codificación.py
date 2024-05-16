def cesar_cod(mensaje,desp):
    """
    Función que codifica un mensaje segun el desplazamiento indicado:
    entradas y restricciones:
    Mensaje: debe ser un string
    desp: debe ser un entero
    salidas:
    mensaje codificado.
    """
    if type(mensaje) != str:
        raise Exception("Error el mensaje debe ser un string")
    if type(desp) != int:
        raise Exception("Error el mensaje debe ser un entero")
    mensaje=mensaje.lower()
    resultado=""
    n=len(mensaje)
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","r","o","p","q","r","s","t","v","w","x","y","z"]
    alfabeto3=alfabeto_cod(alfabeto,desp)
    for i in range(0,n):
        letra=mensaje[i]
        if letra in alfabeto:
            posicion= alfabeto.index(letra)
            letra=alfabeto3[posicion]
            resultado= resultado + letra
        else:
            resultado=resultado+letra
    print(resultado)
    

def cesar_dec(mensaje,desp):
    """
    Función que decodifica un mensaje segun el desplazamiento indicado:
    entradas y restricciones:
    Mensaje: debe ser un string
    desp: debe ser un entero
    salidas:
    mensaje decodificado.
    """
    mensaje=mensaje.lower()
    resultado=""
    n=len(mensaje)
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","v","w","x","y","z"]
    alfabeto3=alfabeto_cod(alfabeto,desp)
    for i in range(0,n):
        letra=mensaje[i]
        if letra in alfabeto3:
            posicion= alfabeto3.index(letra)
            letra=alfabeto[posicion]
            resultado= resultado + letra
        else:
            resultado=resultado+letra
    print(resultado)
    

def alfabeto_cod(alfabeto,desp):
    """
    Función que crea un alfabeto según el desplazamiento inidcado
    entradas y restricciones:
    dezplamiento: entero no negativo
    Salidas:
    devuelve eñ alfabeto nuevo según el desplazamiento
    """
    alfabeto2=[]
    h=len(alfabeto)
    for i in range(desp,h):
        letra=alfabeto[i]
        if h == len(alfabeto2):
            return alfabeto2
        alfabeto2.append(letra)
    if h != len(alfabeto2):
        alfabeto2.extend(alfabeto[:desp])
    return alfabeto2

