def cargar_distritos():
    distritos={}
    try:
        archivo = open("distelec.txt", "r", encoding="ANSI")
        for linea in archivo:
            linea= linea.strip()
            datos= linea.split(",")
            distrito=dict(zip(["provincia","cantón","distrito"],datos[1:]))
            distritos[datos[0]]=distrito
        archivo.close()
    except FileNotFoundError as e:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Ocurrió un error:{e}")
    return distritos
def cargar_Padron():
    padron = {}
    try:
        archivo = open("PADRON_COMPLETO.txt","r", encoding="ANSI")
        for linea in archivo:
            datos= linea.split(",")
            persona={}
            persona["código"]=datos[1]
            persona["nombre"]=datos[5].strip()
            persona["apellido1"] = datos[6].strip()
            persona["apellido2"] = datos[7].strip()
            padron[datos[0]] = persona
        archivo.close()
    except FileNotFoundError as e:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Ocurrió un error:{e}")
    return padron

def imprimir_persona(cedula, padron, distritos):
    if cedula in padron:
        print(f"Cédula:\t{cedula}")
        persona = padron[cedula]
        print(f"Nombre:\t{persona['nombre']}, {persona['apellido1']},{persona['apellido2']}")
        distrito=distritos[persona["código"]]
        print(f"Provincia:\t{distrito['provincia']}")
        print(f"Cantón:   \t{distrito['cantón']}")
        print(f"Distrito: \t{distrito['distrito']}")
            
    else:
        print("Cédula no encontrada")
