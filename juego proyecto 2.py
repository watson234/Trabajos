#Juego del Piedra, Papel, Tijera, Lagarto, Spock
#Taller a Programación
#Proyecto 0
#Elaborado por: Kendall Amador. Jenny Huang Chen

import random
lista =["R","P","T","L","S","X"]
Opciones_Jugador=[]
letras={"r":"R","p":"P","t":"T","l":"L","s":"S","x":"X"}
veces_usadas={"R":0,"P":0,"T":0,"L":0,"S":0}
ganadas_letra={"Gano":"","Perdio":""}
IA=0
posibles={"R":["P","S"],"S":["P","L"],"P":["T","L"],"L":["T","R"],"T":["R","S"]}
ganadas_Usuario=0
ganadas_Compu=0
rondas_Jugadas=0
rondas_Empatadas=0
Opción_Usuario=""
ganadas={"Usuario":0,"Compu":0,"Empatadas":0}

def Juego():
    """
    Subrutina principal del juego de Piedra, Papel, Tijera, Lagarto, Spock
    Entradas y restricciones:
    ninguna.
    Salidas:
    El juego.
    """
    mensaje_bienvenida()
    limpiar_pantalla()
    global ganadas_Compu,ganadas,rondas_Empatadas,ganadas_Usuario,lista, posibles,Opciones_Jugador, rondas_jugadas  
    iniciar= True
    datos=Datos()
    gano=True    
    while iniciar:
        Opciones_Jugador=[]
        IA=0
        IA=dificultad(IA)
        if IA == "6":
            return mensaje_despedida()
        rondas_Jugadas=0
        ganadas={"Usuario":0,"Compu":0,"Empatadas":0}
        continuar = True
        ganadas_Usuario=0
        ganadas_Compu=0
        rondas_Empatadas=0
        while continuar:
            Imprimir_Ronda(datos,ganadas_Compu, ganadas_Usuario, rondas_Jugadas, rondas_Empatadas)
            partida( IA,posibles, datos)
            rondas_Jugadas+=1
            continuar=seguir()
            if not continuar:
                marcador_final(rondas_Jugadas,lista,datos)
                    
            
            
    mensaje_despedida()

def verificar(continuar):
    """
    Función que verifica el valor de continuar
    Entradas y restricciones:
    -continuar debe ser un string entre n o s
    Salidas:
    -devuelve el continuar como valor permitido
    """
    continuar=continuar.lower()
    permitido=True
    listita="sn"
    while permitido:
        if not continuar in listita:
             continuar=input("Debe ingresar 's' para seguir jugando y 'n' para salir:\n")
        else:
            permitido=False
    return continuar
        
        
def limpiar_pantalla():
    """
    Función que imprime lineas en blanco para limpiar la pantalla.
    Entradas y restricciones: ninguna
    Salidas: 15 lineas
    """
    print("\n" * 15)

def Imprimir_Ronda(datos,ganadas_Compu, ganadas_Usuario, rondas_Jugadas, rondas_Empatadas):
    """
    Esta Función imprime los mensajes de cada ronda junto con sus resultados y la ronda actual"
    Entradas:
    rondas que se han jugado
    rondas ganadas por el jugador y por la maquina
    rondas empatadas
    restricciones:
    -Ninguna
    Salidas:
    Impresion de información en pantalla de la información de ronda
    """
    
    print("\n"*5)
    print("Ronda:",rondas_Jugadas)
    print("Marcador: ",datos, " :", ganadas_Usuario, "IA:",ganadas_Compu, " Empatadas: ", rondas_Empatadas)
    print("\n"*2)
def seguir():
    """
    Función que indique si el jugador o la maquina ya ganaron: 
    entradas:
    -cantidad de partidas ganadas del usuario y la computadora.
    restricciones: ninguna
    salidas:
    -True si el jugador o la maquina no han ganado, seguir jugando 
    -False si el jugador desea abandonar.
    """
    global Opción_Usuario
    if Opción_Usuario=="X":
        return False
    else:
        return True
def Datos():
    """
    Función que hace chequeo de restricción al nombre de usuario
    entrada y restricciones:
    -str que ingresó el usuario, debe estar dentro de la lista, no debe ser números
    salida:
    -si el nombre es inválido:seguir preguntando 
    """
    datos=input("Ingrese su nombre: ")
    datos1=datos.lower()
    datos_letras="abcdefghijklmnopqrxtuvwxyzñáéíóúü"
    hacer=True
    while hacer: 
        if not datos1[0] in datos_letras:
            datos=input("Solo puede contener str \n Ingrese su nombre: ")
            datos1=datos.lower()
        else:
            hacer=False
    return datos

def partida( IA,posibles, datos):
    """
    Función que es la base donde se encuentra el juego:
    Entradas:
    rondas que se han jugado
    rondas ganadas por el jugador y por la maquina
    rondas empatadas
    modo de juego
    restricciones: ninguna
    Salidas: juego
    """
    print("Elija su opción:")
    print("""Piedra : R
Papel  : P
Tijera : T
Lagarto: L
Spock  : S
Salir  : X
         """)
    global Opciones_Jugador, ganadas_Usuario,ganadas_Compu,rondas_Empatadas,gano,ganadas_letra,Opción_Usuario
    Opción_Usuario=input()
    Opción_Usuario=letra(Opción_Usuario)
    if Opción_Usuario=="X":
        return seguir() 
    opción_IA=""
    if IA=="1":
        opción_IA=facil(opción_IA,lista)
    elif IA == "2":
        opción_IA=medio(opción_IA,lista,Opciones_Jugador,posibles)
    elif IA =="3":
        opción_IA=normal(opción_IA,lista,Opciones_Jugador,posibles)
    elif IA == "4":
        opción_IA=dificil(opción_IA,posibles)
    elif IA== "5":
        opción_IA=especial(opción_IA,Opción_Usuario,rondas_Jugadas) 
    else:
        print("no hay selección")
    print("IA")
    arma_IA(opción_IA)
    símbolo_VS()
    print(datos)
    Arma_Usuario(Opción_Usuario)
    Opciones_Jugador.append(Opción_Usuario)
    opciones(Opción_Usuario,opción_IA)
    return ganadas_Compu,rondas_Empatadas,ganadas_Usuario,rondas_Jugadas
    
def letra(Opción_Usuario):
    """
    Función que verifica la validez de la opción de usuario
    entradas y restricciones:
    -Opción de usuario debe ser un str de las opciones permitidas
    salidas:
    -retorna el la opción de usuario en mayuscula o validado
    """
    permitidas=["r","R","p","P","t","T","l","L","s","S","x","X"]
    valor=True
    while valor:
        if type(Opción_Usuario) != str:
            print("Error el valor ingresado debe ser una Letra que se encuentre entre las Opciones")
            Opción_Usuario=input("ingrese su opción: ")
            valor=True
        elif not Opción_Usuario in permitidas:
            print("Error el valor ingresado debe ser una Letra que se encuentre entre las Opciones")
            Opción_Usuario=input("ingrese su opción: ")
            valor=True
        else:
            valor=False
    if Opción_Usuario in letras:
        Opción_Usuario=letras[Opción_Usuario]
    return Opción_Usuario
        
def dificultad(IA): 
    """
    Función para que el jugador elija el modo de juego
    Entradas:
    modos de juegos disponibles
    restricciones:número entero entre 1 y 6
    Salidas: modo de juego seleccionado
    """
    print("elija la dificultad del juego: ")
    print("""
            1- fácil
            2- medio
            3- normal
            4- dificil
            5- especial
            6- Salir
         """)
    IA= input()
    lista1=["1","2","3","4","5","6"]
    while IA != int and not IA in lista1:
        print("Debe elegir nivel de dificultad entre 1 y 6")
        IA=input()
    return IA

        
def facil(opción_IA,lista):
    """ modos de juego disponibles
    entradas y restricciones:
    ninguna
    salidas:
    opción de la maquina
    """
    opción_IA=random.choice(lista)
    return opción_IA

def medio(opción_IA,lista,Opciones_Jugador,posibles):
    """
    Función de dificultad para el jugador esta elije una opción según las más
    comunes
    entradas:
    -Las ya elegidas por el usuario
    -las posibles opciones a elejir
    restricciones: ninguna
    salidas:
    retorna la opción elegida por la maquina
    """
    global veces_usadas
    for i in lista:
        veces_usadas[i]=Opciones_Jugador.count(i)
    opción=max(veces_usadas, key=veces_usadas.get)
    r=veces_usadas[opción]
    if r > 1:
        for l in lista:
            if opción == l:
               opción_IA=random.choice(posibles[opción])
               return opción_IA
    else:
        opción_IA=random.choice(lista)
        return opción_IA
           
def normal(opción_IA,lista,Opciones_Jugador,posibles):
    """
    Función de dificultad para el jugador esta elije una opción según la que le gana al anterior
    entradas:
    -Las ya elegidas por el usuario anteriormente
    -las posibles opciones a elejir
    restricciones: ninguna
    salidas:
    retorna la opción elegida por la maquina
    """
    if len(Opciones_Jugador)!=0:
        p=len(Opciones_Jugador)
        p-=1
        Usuario=Opciones_Jugador[p]
        elejir=posibles[Usuario]
        e=posibles[elejir[0]]+posibles[elejir[1]]
        for i in e:
            letra=e.count(i)
            if letra ==2:
                e.remove(i)
        opción_IA=random.choice(e)
        return opción_IA
    else:
        opción_IA=random.choice(lista)
        return opción_IA

def dificil(opción_IA,posibles):
    """
    Función de dificultad para el jugador esta elije una opción con metedo a win-stay/lose-shif
    entradas:
    -Las ya elegidas por el con la cual gano o perdio
    -las posibles opciones a elejir
    restricciones: ninguna
    salidas:
    retorna la opción elegida por la maquina
    """
    global ganadas_letra
    if  ganadas_letra["Gano"]=="" and  ganadas_letra["Perdio"]=="":
        opción_IA=random.choice(lista)
        return opción_IA
    else:
        if ganadas_letra["Gano"] == "":
            IA_OP=ganadas_letra["Perdio"]
            print("contra esta perdio",IA_OP, ganadas_letra)
            L=posibles[IA_OP]
            elejir=posibles[L[0]]+posibles[L[1]]
            print(elejir)
            Opción_IA=max(elejir)
            return opción_IA
        else:
            Usuario=ganadas_letra["Gano"]
            opción_IA=random.choice(posibles[Usuario])
            print(posibles[Usuario])
            return opción_IA

def especial(opción_IA,Opción_Usuario,rondas_Jugadas):
    """
    Función de dificultad del juego nivel especial, cuando el jugador elige el nivel\
    el sistema retorna opción de orden R,P,T,L,S cuando pierde y retorna la orden inversa cuando gana
    Entrada y restricciones:
    -los posibles 5 opciones a elegir
    Salida:
    cuando gana: sigue orden inversa
    cuando pierda: sigue orden normal 
    """
    global ganadas_letra
    lista1=["R","P","T","L","S"]*2
    lista2=lista1[::-1]*2
    rondas_Jugadas
    if ganadas_letra["Gano"]=="" and  ganadas_letra["Perdio"]=="":
        opción_IA=lista1[rondas_Jugadas-1]
        return opción_IA
    elif ganadas_letra["Gano"]==ganadas_letra["Perdio"]:
        opción_IA=lista2[rondas_Jugadas]
    elif ganadas_letra["Gano"]:
        opción_IA=lista2[rondas_Jugadas]
        return opción_IA
    else:
        ganadas_letra["Perdio"]
        opción_IA=lista1[rondas_Jugadas]
        return opción_IA
              
def opciones(Opción_Usuario,opción_IA):
    """
    Función que define quiene es el ganador de la ronda y emprime un mensaje.
    entradas:
    -Opción del Usuario
    -Opción de la maquina
    restricciones:
    ninguna
    salidas:
    -resultado de las ganas por cada jugador ademas de las empatadas y emprime
    un mensaje de quien gano la ronda.
    """
    global Opciones_Jugador, ganadas_Usuario,ganadas,ganadas_Compu,rondas_Empatadas,ganadas_letra 
    if Opción_Usuario in posibles:
        if opción_IA in posibles[Opción_Usuario]:
            ganadas_Compu+=1
            ganadas_letra["Perdio"]=opción_IA
            ganadas_letra["Gano"]=""
            r=ganadas["Compu"]
            r+=1
            ganadas["Compu"]=r
            mensaje_pierde_rondita()
            return ganadas_Compu,ganadas_letra
        elif opción_IA == Opción_Usuario:
            rondas_Empatadas+=1
            ganadas_letra["Perdio"]=""
            ganadas_letra["Gano"]=""
            r=ganadas["Empatadas"]
            r+=1
            ganadas["Empatadas"]=r
            mensaje_empate_rondita()
            return rondas_Empatadas
        else:
            ganadas_Usuario+=1
            ganadas_letra["Gano"]=Opción_Usuario
            ganadas_letra["Perdio"]=""
            r=ganadas["Usuario"]
            r+=1
            ganadas["Usuario"]=r
            mensaje_gana_rondita()
            return ganadas_Usuario,ganadas_letra
        
def mensaje_bienvenida():
    """
    Funcion que imprime mensaje de bienvenida al jugador
    Entrada y restricciones: no hay
    Salida: mensaje de bienvenida
    """
    print("Bienvenid@ al juego de: Piedra, Papel, Tijera, Lagarto, Spock")
    print(" __________________________________________")
    print("|  ____    ____    _____   _       ____   |")
    print("| |  _ \\  |  _ \\  |_   _| | |     / ___|  |")
    print("| | |_) | | |_) |   | |   | |     \\___ \\  |")
    print("| |  _ <  |  __/    | |   | |___   ___) | |")
    print("| |_| \\_\\ |_|       |_|   |_____| |____/  |")
    print("|_________________________________________|")
def mensaje_despedida():
    """
    Funcion que imprime mensaje de despedida al jugador
    Entrada y restricciones: no hay
    Salida: mensaje de despedida
    """
    print("Gracias por jugar el juego de Piedra, Papel, Tijera, Lagarto, Spock")
    print("¡Nos vemos pronto!")
def mensaje_perdedor():
    """
    Funcion que imprime mensaje de perderdor al jugador
    Entrada y restricciones: no hay
    Salida: mensaje de perderdor
    """
    print("Ha perdido el juego :(")
def mensaje_ganador():
    """
    Funcion que imprime mensaje de ganador al jugador
    Entrada y restricciones: no hay
    Salida: mensaje de ganador
    """
    print("¡FELICIDADES! Ha ganado el juego :)")
def símbolo_piedras():
    """
    Funcion que aparece el símbolo de piedras
    """
    print(" ____   ")
    print("|  _ \\   ")
    print("| |_) |  ")
    print("|  _ <  ")
    print("|_| \\_\\ ")
def símbolo_papel():
    """
    Funcion que aparece el símbolo de papel
    """
    print(" ____   ")
    print("|  _ \\ ")
    print("| |_) | ")
    print("|  __/ ")
    print("|_|    ")
def símbolo_tijeras():
    """
    Funcion que aparece el símbolo de tijeras
    """
    print(" _____  ")
    print("|_   _| ")
    print("  | |   ")
    print("  | |  ")
    print("  |_|  ")
def símbolo_lagarto():
    """
    Funcion que aparece el símbolo de lagarto
    """
    print(" _     ")
    print("| |    ")
    print("| |    ")
    print("| |___ ")
    print("|_____|")
def símbolo_spock():
    """
    Funcion que aparece el símbolo de spock
    """
    print(" ____  ")
    print("/ ___| ")
    print("\\___ \\  ")
    print(" ___) | ")
    print("|____/ ")
def símbolo_VS():
    """
    Función que aparece el símbolo de VS.
    """
    print("VS.")
def mensaje_gana_rondita():
    """
    Función que imprime mensaje de que el usuario ha ganado la rondita
    """
    print("!ESO¡ Ganaste esta rondita! \n Sigue adelante! ")
def mensaje_pierde_rondita():
    """
    Función que imprime mensaje de que el usuario ha perdido la rondita
    """
    print("NOOO :( Perdiste esta rondita \n No se rinde! ")
def mensaje_empate_rondita():
    """
    Función que imprime mensaje de que el usuario ha empatido la rondita
    """
    print("EMPATE:) Usted empató esta rondita \n Vamos Vamos! ")
    
def marcador_final(rondas_Jugadas,lista,datos):
    """
    Función que imprime en resultado total de la partida con todos los valores y promedios
    Entradas y restricciones:
    -valores de las ganadas de los jugadores, las opciones utilizadas por el usuario,
    las rondas totales jugadas
    salidas:
    Marcador final de la ronda.
    """
    global veces_usadas,ganadas
    for i in lista:
        veces_usadas[i]=Opciones_Jugador.count(i)
    promedio={"R":0,"P":0,"T":0,"L":0,"S":0}
    r=0
    for llave in veces_usadas:
        r+=veces_usadas[llave]
    for llave in promedio:
        if r == 0:
            r=1
        else:
            promedio[llave]=veces_usadas[llave]/r*100
    print("Marcador final de la partida\n")
    print("Jugador\t\tResultado")
    print("-" * 25)
    for llave in ganadas:
        if llave != "Empatadas":
            print(f"{llave}\t\t{ganadas[llave]}")
        else:
            print(f"{llave}       {ganadas[llave]}")
    print("\n")
    print("Promedio de uso de cada Opción en la partida\n")
    print("Opción\t\tpromedio")
    print("-" * 30)
    for llave in promedio:
        print(f"{llave}\t\t{promedio[llave]}%")
    print("\n")
    print(f"la cantida de rondas Jugadas fueron: {rondas_Jugadas-1}\n")
    usuario=ganadas["Usuario"]
    compu=ganadas["Compu"]
    if usuario>compu:
        print(f"El ganador de la partida es: {datos}")
    elif usuario==compu:
        print(f"¡La partida a terminado en empate!")
    else:
        print(f"El ganador de la partida es: La Computadora")
    print("\n")
    return 

    
def arma_IA(Opción_IA):
    if Opción_IA == "R":
        return símbolo_piedras()
    if Opción_IA == "P":
        return símbolo_papel()
    if Opción_IA == "T":
        return símbolo_tijeras()
    if Opción_IA == "L":
        return símbolo_lagarto()
    else:
        return símbolo_spock()
def Arma_Usuario(Opción_Usuario):
    if Opción_Usuario == "R":
        return símbolo_piedras()
    if Opción_Usuario == "P":
        return símbolo_papel()
    if Opción_Usuario == "T":
        return símbolo_tijeras()
    if Opción_Usuario == "L":
        return símbolo_lagarto()
    else:
        return símbolo_spock()
    
Juego()
        
        
