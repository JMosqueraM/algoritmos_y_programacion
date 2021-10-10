Algoritmo ejercicio_18
	Escribir "Ingrese su nombre completo"
	Leer nombre
	longitud_nombre <- Longitud(nombre)
	// Convertir el string nombre en el arreglo nombre
	Dimension cadena_nombre[100]
	Para i <- 0 Hasta longitud_nombre Con Paso 1
		cadena_nombre[i] <- Subcadena(nombre, i, i)
	FinPara
	
	Escribir Mayusculas(cadena_nombre(0)) Sin Saltar
	para i <- 1 Hasta longitud_nombre Con Paso 1
		si cadena_nombre(i) == " "
			Escribir Mayusculas(cadena_nombre(i + 1)) Sin Saltar
		FinSi
	FinPara
	
FinAlgoritmo
