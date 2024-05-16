def eliminar_elemento_cola(L,n):
    if type(L) != list:
        raise Exception("debe ser una lista")
    return  eliminar_elemento_aux([],L,n)


def eliminar_elemento_aux(L1,L,n):
    if not n in L:
        return L1
    else:
        if n==L[0]:
            return L1+L[1:]

        else:
            return eliminar_elemento_aux(L1+[L[0]],L[1:],n)
def inserción_lista_ordenada_cola(L,n):
    if type(L) != list:
        raise Exception("debe ser una lista")
    return  inserción_aux_cola(L,n,[])

def inserción_aux_cola(L,n,L1):
    if n in L1:
        return L1
    else:
        if n>L[0] and n<L[1]:
            return inserción_aux_cola(L,n,L1+[[L[0]]+[n]+[L[1:]]])
        else:
            return inserción_aux_cola(L,n,L1)

def concordancia(L1,L2,L3):
    if type(L1) != list:
        raise Exception("debe ser una lista")
    if type(L2) != list:
        raise Exception("debe ser una lista")
    if type(L3) != list:
        raise Exception("debe ser una lista")
    return concordancia_aux(L1,L2,L3,[],0,len(L3))

def concordancia_aux(L1,L2,L3,resultado,n,h):
    if L3==[]:
        return resultado
    elif L1[n] in L3:
            if L3[0]==L1[n]:
                s=L2[L1.index(L1[0])]
                return concordancia_aux(L1,L2,L3[1:],resultado+[s],n,h)
            else:
                return concordancia_aux(L1,L2,L3[1:],resultado+[L3[0]],n,h)
        else:
            return concordancia_aux(L1,L2,L3,resultado,n+1,h)             
