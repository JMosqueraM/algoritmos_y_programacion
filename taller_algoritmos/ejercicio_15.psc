Algoritmo ejercicio_15
	Escribir "Escriba un numero de dos cifras"
	Leer numero 
	numero_str <- ConvertirATexto(numero)
	inverso <- SubCadena(numero_str, 1, 1) + SubCadena(numero_str, 0, 0) 
	Escribir "El numero invertido de " numero " es " inverso
	
FinAlgoritmo
