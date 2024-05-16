Algoritmo contar_digitos
	// Algoritmo para contar digitos de un numero n
	// entradas y restricciones
	// numero n debe ser entero
	// salida: numero de digitos
	Definir n, contador Como Entero
	Escribir 'ingrese valor del numero n'
	Leer n
	Si n >= 0 Entonces
		contador <- 1
		Mientras n>=10 Hacer
			n <- n/10
			contador <- contador+1
		FinMientras
		Escribir 'la cantidad de digitos del numero es ', contador
	SiNo
		Escribir "debe ser un numero entero mayor o igual a 0"
	FinSi
FinAlgoritmo
