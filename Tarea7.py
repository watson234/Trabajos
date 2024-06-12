import os
from operator import itemgetter

def busqueda_textual(nombre_archivo):
    """
    Función que busca en el archivo dado
    entradas y restricciones:
     -nombre_archivo: el archivo a analizar
    Salidas:
    aparicion del texto que se busco
    """
    
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = input("Escriba el texto a buscar: ")
            for n, linea in enumerate(archivo):
                if texto in linea:
                    print(f"Línea {n+1}: {linea.strip()}")
    except Exception as e:
        print(f"Error: {e}")

def estadísticas(nombre_archivo):
    """
    Función que muestra las estadísticas del archivo
    Entradas y restricciones:
    -nombre_archivo: el archivo a analizar
    Salidas:
    Las estadísticas del archivo
    """
    conteo_caracteres = {}
    caracteres = 0
    cantidad_lineas = 0
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for n, linea in enumerate(archivo):
                cantidad_lineas = n
                for caracter in linea:
                    caracteres += 1
                    if caracter in conteo_caracteres:
                        conteo_caracteres[caracter] += 1
                    else:
                        conteo_caracteres[caracter] = 1
        top_10 = dict(sorted(conteo_caracteres.items(), key=itemgetter(1), reverse=True)[:10])
        print(f"Nombre del archivo: {nombre_archivo}")
        print(f"Cantidad de líneas: {cantidad_lineas + 1}")
        print(f"Cantidad de caracteres: {caracteres}")
        print("Top 10 caracteres más usados:")
        for llave, valor in top_10.items():
            print(f"{llave}: {valor}")
    except Exception as e:
        print(f"Error: {e}")

def reemplazar(nombre_archivo):
    """
    Función que remplaza partes del archivo
    Entradas y restricciones:
    -nombre_archivo: el archivo a analizar
    Salidas:
    archivo con parámetros reemplazados
    """
    buscado = input("Ingresa el texto a buscar: ")
    reemplazo = input("Ingresa el texto de reemplazo: ")
    modificado = nombre_archivo + ".tmp"
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo_lectura, \
             open(modificado, 'w', encoding='utf-8') as archivo_escritura:
            for linea in archivo_lectura:
                linea_modificada = linea.replace(buscado, reemplazo)
                archivo_escritura.write(linea_modificada)
        os.remove(nombre_archivo)
        os.rename(modificado, nombre_archivo)
    except Exception as e:
        print(f"Error: {e}")

def menu_archivo():
    """
    Muestra el menú para seleccionar un archivo
    entradas y restricciones
    ninguna
    salida:
    archivo seleccionado por el usuario
    """
    try:
        nombre_archivo = input("Escriba el nombre del archivo: ")
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            pass
        return nombre_archivo
    except FileNotFoundError:
        print("El archivo no se encuentra")
    except Exception as e:
        print(f"Error: {e}")
    return None

def menu_principal(nombre_archivo):
    """
    Muestra el menú principal y permite al usuario realizar acciones sobre el archivo
    entradas y restricciones:
    -Nombre_archivo: archivo seleccionado por el usuario
    Salida:
    Menú principal
    """
    while True:
        print("\nIndique qué desea realizar:")
        print("1. Estadísticas de archivo")
        print("2. Búsqueda textual")
        print("3. Reemplazar texto")
        print("4. Volver a elegir archivo")
        print("5. Salir")
        opcion = int(input())
        if opcion == 1:
            estadísticas(nombre_archivo)
        elif opcion == 2:
            busqueda_textual(nombre_archivo)
        elif opcion == 3:
            reemplazar(nombre_archivo)
        elif opcion == 4:
            return
        elif opcion == 5:
            exit()
        else:
            print("Error: debe indicar una opción correcta")

def main():
    """
    Función principal del programa esta muestra el menú principal
    entradas y restricciones:
    -Ninguna
    Salida:
    Menú principal
    """
    while True:
        nombre_archivo = menu_archivo()
        if nombre_archivo:
            menu_principal(nombre_archivo)

main()

