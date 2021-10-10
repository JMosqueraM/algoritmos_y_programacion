Algoritmo ejercicio_17
	Escribir "Ingrese la distancia (en km) entre los dos vehiculos"
	Leer distancia
	Escribir "Ingrese la velocidad (en km/h) del vehiculo que se encuentra atras (el mas rapido)"
	Leer vehiculo1
	Escribir "Ingrese la velocidad (en km/h) del vehiculo que se encuentra adelante (el mas lento)"
	Leer vehiculo1
	tiempo_para_encuentro<-distancia/(vehiculo1-vehiculo2)
	tiempo_en_minutos<-tiempo_para_encuentro*60
	escribir "El tiempo en minutos que se demora un vehiculo en alcanzar al otro es de " tiempo_en_minutos " minutos"
	
	
FinAlgoritmo

