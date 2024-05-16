Algoritmo Mayor_de_3_numeros
	// 
	Definir A, B, C como real
	Escribir "Ingrese el valor de A: "
	Leer A
	Escribir "Ingrese el valor de B: "
	Leer B
	Escribir "ingrese el valor de C: "
	Leer C
	Si A < B Entonces
		Si B>C Entonces
			Escribir "El mayor es B: ",B 
		SiNo
			Escribir "El mayor es C: ", C
		FinSi
	SiNo
		Si A < C Entonces
			Escribir "el mayor es C: ", C
		SiNo
			Escribir "El mayor es A: ", A
		FinSi
	FinSi
FinAlgoritmo
