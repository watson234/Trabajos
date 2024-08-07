
//se importan las librerias necesarias
#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>


using namespace std;

//se crea un estructura
struct cedula {
	int numero;
	char nombre[25];
	bool activo;
};

cedula arreglo[50];// se define como global el arreglo
int cont = 0;

void guardararchivo(cedula Arreglo[], int cont) 
//función que guarda en un archivo los datos
//entradas:
//Arreglo que contiene las cedulas
//cont variable entero
{
	system("CLS");//limpia la pantalla
	cout << endl << endl;
	FILE* archcedulas;//se usa tipo puntero al archivo 
	fopen_s(&archcedulas, "cedulas.txt", "w+")//se abre y asigna a la variable por referencia el archivo cedulas;

		for (int y = 0; y < cont; y++) //se crea un ciclo que se detiene al llegar a ser igual a cont
		{
			if (Arreglo[y].activo == true) {//solo se guardaran aquellas personas que esten activas
				printf("Cedula: %i Nombre:  %s		-guardado- \n", arreglo[y].numero, arreglo[y].nombre);//se imprime en pantalla
				fprintf_s(archcedulas, "%s", Arreglo[y].nombre);//se escribe sobre el archivo de manera string
				if (y == (cont - 1)) { fprintf_s(archcedulas, "\n%i", Arreglo[y].numero); }// se eliminan los enter al final del archivo de texto
				else fprintf_s(archcedulas, "\n%i\n\n", Arreglo[y].numero);// se imprimen enter en el archivo
			}
		}
	fclose(archcedulas);// se cierra el archivo
	cout << endl << " Presione una tecla para continuar..." << endl;
}

void cargararchivo(cedula arreglo[], int &cont) 
/*
* función que carga lo contenido en el archivo
* entradas:
* arreglo que contiene los elementos
* 
*/
{//El arreglo no debe ingresar como referencia, pero el contador si para que su valor cambie respecto a lo que se hace en la funcion
	system("CLS");
	FILE*archcedulas;;//se usa tipo puntero al archivo 
	fopen_s(&archcedulas, "cedulas.txt", "r");// se abre el archivo en modo lectura
	if (archcedulas == NULL) //condición
	{
		cout << "no se encontro el archivo" << endl;
	}
	else {
		while (!feof(archcedulas)) {
			fscanf_s(archcedulas, "%s", arreglo[cont].nombre, 25);//cont al inicio esta en cero
			fscanf_s(archcedulas, "%i", &arreglo[cont].numero);//se lee tipo entero y se agrega a el arreglo
			printf("\n\n  Cedula: %i Nombre:  %s		-cargado- \n", arreglo[cont].numero, arreglo[cont].nombre);
			arreglo[cont].activo = true;// Activa de nuevo a la persona
			cont++;
		}
		fclose(archcedulas);//se cierra el archivo
	}
	cout << endl << " Presione una tecla para continuar..." << endl;
}

void insertar(cedula arreglof[], int &cont) 
/*
* Función que inserta un nuevo usario al arreglo
* 
*/
{
	system("CLS");//se limpia la pantalla
	cout << endl << " ----------------  Ingresar persona  ----------------" << endl;
	cout << endl << " Digite el nombre de la persona: ";
	cin >> arreglof[cont].nombre;//se agrega al arreglo el dato ingresado
	cout << endl << " Digite el numero de cedula: ";
	cin >> arreglof[cont].numero;//se agrega al arreglo la cedula ingresado
	arreglo[cont].activo = true;// activa a la persona
	cont++;
}

void buscar_nombre(cedula arreglo[], int cont) 
/*
* Función que busca un usuario en especifico
* entradas:
* arreglo=contiene los elementos de la estructura
*/
{
	system("CLS");
	cout << endl << " ----------------  Buscar persona por nombre  ----------------" << endl << endl << endl;
	char cual[25];
	cout << " Digite el nombre que desea buscar: ";
	cin >> cual;
	cout << endl << endl;
	int i;
	for (i = 0; i<cont; i++) {
		if ((strcmp(arreglo[i].nombre, cual) == 0) && (arreglo[i].activo == true)) {// compara el nombre y si esta activo
			cout << "El numero de cedula de " << cual << " es: " << arreglo[i].numero << endl;
			break;
		}
	}
	if (i == cont) {
		cout << " El nombre no ha sido ingresado o fue borrado" << endl;
	}
}

void buscar_cedula(cedula arreglo[], int cont, int cual) {
	int i;
	for (i = 0; i<cont; i++) {
		if ((arreglo[i].numero == cual) && (arreglo[i].activo == true)) {
			cout << "El numero de cedula: " << cual << " corresponde a: " << arreglo[i].nombre << endl;
			break;
		}
	}
	if (i == cont) {
		cout << " El numero de cedula no ha sido ingresado o fue borrado" << endl;
	}
}

void listarcedulas(cedula arreglo[], int cont) {
	system("CLS");
	cout << endl << " ----------------  Lista de personas  ----------------" << endl << endl;
	int numerador = 1;
	cout << "		# Cedula		Nombre" << endl << endl;
	if (cont == 0) { cout << endl << "		La lista esta vacia." << endl; }
	else {
		for (int i = 0; i<cont; i++) {
			if (arreglo[i].activo == true) {
				cout << "	" << numerador << "	" << arreglo[i].numero << "		" << arreglo[i].nombre << endl;
				numerador++;
			}
		}
	}
	cout << endl << endl << " ************** Fin de la lista  ***************" << endl;
}

int buscarparaborrar(cedula arreglo[], int &cont) {
	system("CLS");
	cout << endl << " ----------------  Buscar persona para borrar  ----------------" << endl << endl;
	char cual[25];
	cout << " Digite el nombre que desea buscar para eliminar: ";
	cin >> cual;
	cout << endl << endl;
	int i;
	for (i = 0; i<cont; i++) {
		if ((strcmp(arreglo[i].nombre, cual) == 0) && (arreglo[i].activo == true)) {
			cout << endl << " Persona borrada con exito" << endl << endl;
			cont--;//decrementa el contador para que la cuenta de personas sea precisa
			return i;//retorna el numero de lugar en el que esta el nombre en el arreglo
		}
	}
	if (i == cont) {
		cout << " El nombre no ha sido ingresado o ya fue borrado" << endl;
		return -1;//retorna -1 ya q la funcion es tipo entero, y al ser llamada se esper un valor de regreso
	}
	else return -2;//Se escribe para evitar warning
}

void main() {
	bool menu = true;
	while (menu) {
		system("CLS");
		cout << endl << endl << "	-----------------	Menu Principal   -----------------" << endl << endl;
		cout << "		1. Agregar persona" << endl;
		cout << "		2. Buscar por nombre" << endl;
		cout << "		3. Buscar por cedula" << endl;
		cout << "		4. Listar todos" << endl;
		cout << "		5. Borrar una persona" << endl;
		cout << "		6. Guardar Arreglo a archivo" << endl;
		cout << "		7. Cargar Arreglo desde archivo " << endl;
		cout << "		8. Salir" << endl << endl;
		cout << "		Digite una opcion: ";
		int opcion = 0;
		cin >> opcion;
		switch (opcion) {
		case 1: {
			insertar(arreglo, cont);
			cout << endl << endl << " La persona fue ingresada correctamente." << endl << endl;
			cout << " Presione una tecla para continuar..." << endl;
			_getch();
			break;
		}
		case 2: {
			buscar_nombre(arreglo, cont);
			cout << endl << " Presione una tecla para continuar..." << endl;
			_getch();
			break;
		}
		case 3: {
			system("CLS");
			cout << endl << " ----------------  Buscar persona por #cedula  ----------------" << endl << endl << endl;
			int cual;
			cout << " Digite el numero de cedula que desea buscar: ";
			cin >> cual;
			cout << endl << endl;
			buscar_cedula(arreglo, cont, cual);
			cout << endl << " Presione una tecla para continuar..." << endl;
			_getch();
			break;
		}
		case 4: {
			listarcedulas(arreglo, cont);
			cout << endl << " Presione una tecla para continuar..." << endl;
			_getch();
			break;
		}
		case 5: {
			arreglo[buscarparaborrar(arreglo, cont)].activo = false;// desactiva persona
			cout << endl << " Presione una tecla para continuar..." << endl;
			_getch();
			break;
		}
		case 6: {
			guardararchivo(arreglo, cont);
			_getch();
			break;
		}
		case 7: {
			if (cont != 0) {
				cout << endl << endl << "  Se perderan los cambios realizados en esta sesion," << endl;
				cout << "  desea continuar(S/N): ";
				char sino[2];
				cin >> sino;
				if ((strcmp(sino, "S") == 0) || (strcmp(sino, "s") == 0)) {
					cont = 0;
					cargararchivo(arreglo, cont);
				}
				else cout << " No se cargaran datos guardados. " << endl;
			}
			else cargararchivo(arreglo, cont);
			_getch();
			break;
		}

		case 8: {
			menu = false;
			system("CLS");
			cout << endl << endl << endl << endl << "			***********************************" << endl;
			cout << "			*                                 *" << endl;
			cout << "			*   *******  *******   *******    *" << endl;
			cout << "			*      *     *         *          *" << endl;
			cout << "			*      *     *****     *          *" << endl;
			cout << "			*      *     *         *          *" << endl;
			cout << "			*      *     *******   *******    *" << endl;
			cout << "			*                                 *" << endl;
			cout << "			***********************************" << endl << endl << endl;
			cout << " Presione una tecla para salir..." << endl;
			_getch();
			break;
		}
		default: {
			cout << endl << "La opcion digitada no exite" << endl << endl;
			cout << " Presione una tecla para continuar..." << endl;
			_getch();
		}
		}
	}
}
/*
* 
* 

        -----------------       Menu Principal   -----------------

                1. Agregar persona
                2. Buscar por nombre
                3. Buscar por cedula
                4. Listar todos
                5. Borrar una persona
                6. Guardar Arreglo a archivo
                7. Cargar Arreglo desde archivo
                8. Salir

                Digite una opcion:


 ----------------  Ingresar persona  ----------------

 Digite el nombre de la persona: 1

 Digite el numero de cedula: 1


 La persona fue ingresada correctamente.

 Presione una tecla para continuar...



 ----------------  Buscar persona por nombre  ----------------


 Digite el nombre que desea buscar: 1


El numero de cedula de 1 es: 1

 Presione una tecla para continuar...






 ----------------  Buscar persona por #cedula  ----------------


 Digite el numero de cedula que desea buscar: 1


El numero de cedula: 1 corresponde a: 1

 Presione una tecla para continuar...





 ----------------  Lista de personas  ----------------

				# Cedula                Nombre

		1       1               1


 ************** Fin de la lista  ***************

 Presione una tecla para continuar...


 ----------------  Buscar persona para borrar  ----------------

 Digite el nombre que desea buscar para eliminar: 1



 Persona borrada con exito


 Presione una tecla para continuar...











Cedula: 23 Nombre:  2           -guardado-

 Presione una tecla para continuar...







  Cedula: 23 Nombre:  2         -cargado-

 Presione una tecla para continuar...







						***********************************
						*                                 *
						*   *******  *******   *******    *
						*      *     *         *          *
						*      *     *****     *          *
						*      *     *         *          *
						*      *     *******   *******    *
						*                                 *
						***********************************


 Presione una tecla para salir...

*/



