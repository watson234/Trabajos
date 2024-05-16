Algoritmo perimetro_triangulo_rectangulo
	// Algoritmo que calcula el perimetro de un triangulo rectangulo
	// entrdas y resticciones base:real positivo, Altura: Real positiv
	// Salida:perimetro del triangulo rectangulo
	definir base, altura, hipotenusa, perimetro como real
	Escribir "Digite el valor de la base :"
	Leer base
	Si base > 0 Entonces
		Escribir "Digite el valor de la altura"
		Leer altura
		Si altura > 0 Entonces
			hipotenusa = rc(base^2+altura^2)
			perimetro = base+altura+hipotenusa
			Escribir "El perimetro es: ", perimetro
		SiNo
			Escribir "la altura debe ser real positivo"
		FinSi
	SiNo
		Escribir "error la base debe ser real positivo"
	FinSi
FinAlgoritmo
