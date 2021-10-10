Algoritmo sin_titulo
	Escribir "Ingrese el sueldo base del vendedor"
	Leer sueldo
	comision_ventas <- 0.1
	Escribir "Ingrese la primera venta del mes"
	Leer primera_venta
	Escribir "Ingrese la segunda venta del mes"
	Leer segunda_venta
	Escribir "Ingrese la tercera venta del mes"
	Leer tercera_venta
	total_comisiones <- ((primera_venta * comision_ventas) + (segunda_venta * comision_ventas) + (tercera_venta * comision_ventas))
	total <- sueldo + total_comisiones
	Escribir "Por comisiones realizadas en el mes (" total_comisiones ") y el sueldo base (" sueldo "), el vendedor recibira: $" total
FinAlgoritmo

