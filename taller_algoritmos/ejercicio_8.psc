Algoritmo ejercicio_8
	Escribir "Ingrese una cantidad de minutos"
	Leer minutos1
	horas <- trunc(minutos1 / 60)
	Si minutos1 > 60 Entonces
		minutos <- minutos1 - (horas*60)
	SiNo
		minutos <- minutos
	Fin Si
	Escribir minutos1 " minutos son " horas " horas y " minutos " minutos."
	
FinAlgoritmo
