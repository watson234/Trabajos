def main():
    """
    Programa que combine dos strings.
    Enradas y restricciones:
    - S1, s1: los strings a combinar.
    Salida:
    Dos strings:
    1.La primera mitad de s1 con la segunda de s2
    2.la primera mitad de s2 con la segunda mitad de s1
    """
    
    s1= input("ingrese su frase: ")
    s2=input("ingrese su frase: ")
    n1=s1[:len(s1) //2]+s2[len(s2) //2:]
    n2=s2[:len(s2) //2]+s1[len(s1) //2:]
    print(n1)
    print(n2)

def segmento():
    """
    Programa que combine dos strings.
    Enradas y restricciones:
    - S1, s1: los strings a combinar.
    Salida:
    Dos strings:
    1.tercer segmento de A, primer segmento de b invertido, segundo segmento de A,
    segundo segmento de B invertido,primer segmento de A.
    """
    s1= input("ingrese su frase: ")
    s2=input("ingrese su frase: ")
    f1=s1[:len(s1) //3:3]+s2[len(s2) //2:1:-1]
    n1=s1[:len(s1) //3:3]+s2[len(s2) //2:-1]+s1[len(s1) //3:2:]+s2[len(s2) //2:2:-1]+s1[len(s1) //3::]
    n2=s2[:len(s2) //2]+s1[len(s1) //2:]
    print(f1)
