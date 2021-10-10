Algoritmo ejercicio_11
	Escribir "Ingrese la calificacion del primer parcial"
	Leer parcial1
	Escribir "Ingrese la calificacion del segundo parcial"
	Leer parcial2
	Escribir "Ingrese la calificacion del segundo parcial"
	Leer parcial3
	promedio_parciales <- (parcial1 + parcial2 + parcial3) / 3
	Escribir "Ingrese la calificacion del examen final"
	Leer examen_final
	Escribir "Ingrese la calificacion del trabajo final"
	Leer trabajo_final
	nota_final <- (promedio_parciales * 0.55) + (examen_final * 0.3) + (trabajo_final * 0.15)
	Escribir "Su calificacion final en la materia de Algoritmos es: " nota_final

FinAlgoritmo
