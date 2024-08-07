

//importa las librerias
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <conio.h>
#pragma warning(disable:4996)//Quita los errores de "Function is insecure"

using namespace std;

/*esta es la estructura de los datos que poseen los Productos*/
typedef struct T_Producto {
	int Codigo;
	char Descripcion[50];
	float Precio;
	int Disponible;
	bool Activo;
} X;//se define un puntero

const int Max = 1000;// se crea una variable constante
int Ultimo = 0;//se crea una variable para el ultimo elemento que se va agregar

void CargaAutomaticaDatosProducto(int NCodigo, int NDescripcion, float NPrecio, int NDisponible, T_Producto& Pieza)//función que captura los elementos
{
	cout << "agregando...";// se imprime un mensaje continuo
	char descripcion[50];//se crea una variable tioo char con un largo de 50
	char des[20]="Producto_";
	
	

	_itoa_s(NDescripcion, descripcion, 50, 10);//se convierte los digitos a ascii
	strcat_s(des, descripcion);// se hace un con cantenación
	strcpy_s(Pieza.Descripcion, 50, des);//se agrega a pieza.descripcion lo contenido en des

	Pieza.Codigo = NCodigo;//se asigna el valor contenido a la ubicación de la estructura
	Pieza.Precio = NPrecio;
	Pieza.Disponible = NDisponible;
	Pieza.Activo = true;
}

void Listar(T_Producto Inventario[Max]) 
/*
* Función que lista los elementos creados
* Entradas:
* Inventario: arreglo que contiene los elementos
*/
{
	system("CLS");//se limpia la consola
	int conta = 0;//se crea una variable tipo entero
	cout << "Listado de  Productos" << endl;//se imprime en pantalla
	for (int i = 0; i<Ultimo; i++) // inicia un ciclo for
	{
		if (Inventario[i].Activo) // se verifica si el articulo esta activo y si no no se imprime
		{
			cout << Inventario[i].Codigo << " " << Inventario[i].Descripcion << " " << Inventario[i].Precio << " "
				<< Inventario[i].Disponible << " " << endl;//se imprime los datos del elemento i del inventario
			conta++;
			if (conta == 7) // se va imprimiendo de 7 en 7
			{
				cout << "-----------------------------------" << endl;
				cout << "Presione cualquier tecla para continuar..." << endl;
				system("pause");
				system("CLS");

				conta = 0;
			}
		}
	}
	system("pause");
}



int BuscarElemento(T_Producto Inventario[Max], int Cual)
/*
* Función que busca un elemento en especifico
* Entradas:
* Inventario- arreglo que contiene los elementos
* cual: elemento que se busca
*/
{
	bool Encontro = false;//variable booleana que indica si ya se encontro el elemento
	int Cont = 0;

	while ((!Encontro) && (Cont<Ultimo))//ciclo que se termina si se encuentra el elemento o si se llego al ultimo
	{
		if ((Inventario[Cont].Activo == true) && (Inventario[Cont].Codigo == Cual))//se verifica si es el elemento que se busca
			Encontro = true;//se asigna un nuevo valor
		else
			Cont++;//se suma al cont
	}

	if (Encontro == true)//verifica si encontro es True
		return Cont;
	else
		return -1; // si no lo encontro devuelve -1

}
void InsertarElemento(T_Producto Inventario[Max], T_Producto Unidad)
//Funcion que inserta un elemento
//entradas:inventario=arreglo, unidad= producto a agregar
{
	Inventario[Ultimo] = Unidad;//se agrega al final del arreglo el elemento
	cout << Inventario[Ultimo].Codigo << "   -   " << Inventario[Ultimo].Descripcion << endl;//imprime el elemento agregado
	Ultimo++;// se le suma a ultimo
}

void BorrarElemento(T_Producto Inventario[Max], int Cual)
/*
* funcion que borra un elemento en especifico
* Entradas:
* inventario=arreglo
cual= elemento a borrar
*/
{
	int PorBorrar;
	PorBorrar = BuscarElemento(Inventario, Cual);//llamada a la función para buscar el elemento

	if (PorBorrar != -1)//si el elemento si se encuentra
		Inventario[PorBorrar].Activo = false;//se cambia su valor de activo

}


void main() 
/*
* Función principal del programa esta carga el menu de opciones
*/
{

	T_Producto PiezasFerreteria[Max];//se crea un arreglo de tipo t_producto
	T_Producto Elemento;// se crea una avriable para los elementos de la estructura
	int opcion = 0;//variable que va a contener la opcion del usuario

	while (opcion<4) //ciclo que se termina si opción es 4
	{

		system("cls");//limpia la pantalla
		cout << "******Menu principal******" << endl;
		cout << "1. Insertar Pieza" << endl;
		cout << "2. Listar Piezas " << endl;
		cout << "3. Borrar Piezas " << endl;
		cout << "4. Salir " << endl;
		cin >> opcion;//captura el numero introducido

		switch (opcion) //se evalua la opción segun los casos
		{

		case 1:
			system("cls");
			for (int contador = 0; contador < 51; contador++)//ciclo for que agrega 51 elementos
			{
				CargaAutomaticaDatosProducto(contador, contador, contador, contador, Elemento);//se hace un llamado a la función para agregar el elemento
				InsertarElemento(PiezasFerreteria, Elemento);//se inserta el elemento
			}
			system("Pause");
			break;

		case 2:
			system("cls");
			Listar(PiezasFerreteria);//llamado a la función listar
			break;
		case 3:
			system("CLS");
			int CodigoEscogido;//variable que va a almacenar el dato ingresado
			cout << "Digite el codigo del Producto a Borrar" << endl;
			cout << "" << endl;
			cout << "CodidoProducto:" << endl;
			cin >> CodigoEscogido;//se agrega a la variable el dato digitado por el usuario
			BorrarElemento(PiezasFerreteria, CodigoEscogido);//llamado a la función con diferentes parametros
			break;

		}
	}
}
/*
* ******Menu principal******
1. Insertar Pieza
2. Listar Piezas
3. Borrar Piezas
4. Salir





* agregando...0   -   Producto_0
agregando...1   -   Producto_1
agregando...2   -   Producto_2
agregando...3   -   Producto_3
agregando...4   -   Producto_4
agregando...5   -   Producto_5
agregando...6   -   Producto_6
agregando...7   -   Producto_7
agregando...8   -   Producto_8
agregando...9   -   Producto_9
agregando...10   -   Producto_10
agregando...11   -   Producto_11
agregando...12   -   Producto_12
agregando...13   -   Producto_13
agregando...14   -   Producto_14
agregando...15   -   Producto_15
agregando...16   -   Producto_16
agregando...17   -   Producto_17
agregando...18   -   Producto_18
agregando...19   -   Producto_19
agregando...20   -   Producto_20
agregando...21   -   Producto_21
agregando...22   -   Producto_22
agregando...23   -   Producto_23
agregando...24   -   Producto_24
agregando...25   -   Producto_25
agregando...26   -   Producto_26
agregando...27   -   Producto_27
agregando...28   -   Producto_28
agregando...29   -   Producto_29
agregando...30   -   Producto_30
agregando...31   -   Producto_31
agregando...32   -   Producto_32
agregando...33   -   Producto_33
agregando...34   -   Producto_34
agregando...35   -   Producto_35
agregando...36   -   Producto_36
agregando...37   -   Producto_37
agregando...38   -   Producto_38
agregando...39   -   Producto_39
agregando...40   -   Producto_40
agregando...41   -   Producto_41
agregando...42   -   Producto_42
agregando...43   -   Producto_43
agregando...44   -   Producto_44
agregando...45   -   Producto_45
agregando...46   -   Producto_46
agregando...47   -   Producto_47
agregando...48   -   Producto_48
agregando...49   -   Producto_49
agregando...50   -   Producto_50
Presione una tecla para continuar . . .


Listado de  Productos
0 Producto_0 0 0
1 Producto_1 1 1
2 Producto_2 2 2
3 Producto_3 3 3
4 Producto_4 4 4
5 Producto_5 5 5
6 Producto_6 6 6
-----------------------------------
Presione cualquier tecla para continuar...
Presione una tecla para continuar . . .

******Menu principal******
1. Insertar Pieza
2. Listar Piezas
3. Borrar Piezas
4. Salir
4

C:\Users\usuario\source\repos\Lab 2\x64\Debug\Lab 2.exe (proceso 14832) se cerró con el código 0.
Presione cualquier tecla para cerrar esta ventana. . .

*/


