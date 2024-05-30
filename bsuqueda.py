def busqueda_textual():
    nombre_archivo= input("Escriba el nombre del archivo: ")
    try:
        with open(nombre_archivo, "r", enconding="utf-8") as archivo:
            texto= input("Escriba el Texto a buscar: ")
            for n,linea in enumerate(archivo):
                if texto in linea:
                    print(f"Linea {n+1}: {linea}")
    except Exception as e:
        print(f"{e}")
