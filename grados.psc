Algoritmo Temperatura_en_grados
	// Algoritmo que convierte entre grados fahrenheit y celsius
	// Entradas y restricciones:
	// Unidad: un caracter debe ser "c" o "f"
	// Grados: numero real. debe ser mayor a -273 si es F al que se va a convertir
	// en caso de convertir a C debe ser mayor a -459.67
	// la salida de la conversión de los grados a la otra unidad
	Definir Temperatura Como Real
	Definir unidad Como Cadena
	Escribir 'ingrese en cual unidad de medida quiere el resultado F para convertir fahrenheit y C para convertir a Celsius: '
	Leer unidad
	Si unidad=='F' O unidad=='f" o unidad=='c' O unidad=='C" Entonces
		Si unidad=='F'O unidad=='f" Entonces
			Escribir 'ingrese la temperatura'
			Leer Temperatura
			Si Temperatura >= -459.67 Entonces
				Temperatura <- (Temperatura-32)*5/9
				Escribir 'La temperatura en grados celsius es : ', Temperatura, 'C°'
			SiNo
				Escribir 'error debe ser mayor a -459.67 grados '
			FinSi
		SiNo
			Escribir 'ingrese la temperatura'
			Leer Temperatura
			Si Temperatura >= -273.15 Entonces
				Temperatura <- Temperatura*9/5+32
				Escribir 'La temperatura en grados fahrenheit es: ', Temperatura, 'F°'
			SiNo
				Escribir 'ERROR la temperatura debe ser mayor a -273,15'
			FinSi
		FinSi
	SiNo
		Escribir "error debe ser un caracter ya sea C o F"
	FinSi
FinAlgoritmo
