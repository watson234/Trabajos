Algoritmo calular_segundos
	// algoritmo para que transforma el tiempo en hora minutos y segundos
	// entradas y restricciones: horas, minutos y segundos en real
	// sALIDAS: minutos, horas, segundos
	Definir segundos,minutos, horas como real
	Escribir "Ingrese las horas: "
	Leer horas
	Escribir "ingrese los minutos: "
	Leer minutos
	Escribir "ingrese los segundos: "
	Leer segundos
	segundos = (horas*3600)+minutos*60+segundos
	minutos = segundos/60
	horas = minutos/60
	Escribir "El total de horas es: ",horas
	Escribir "El total de minutos es:", minutos
	Escribir "El total de segundos es:", segundos
FinAlgoritmo
