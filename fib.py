def fib(n):
    a,b=0,1
    resultado=[a]
    for i in range (n):
        resultado.append(b)
        a, b = b, a+b
    return resultado
