#El siguiente programa indica el color del cuadrado que se encuentra abajo a la derecha de un tablero de ajedrez
f = int(input("Ingrese numero de filas: ")) #Representa el numero de filas en la tabla de ajedrez
c = int(input("Ingrese numero de columnas: "))  #Representa el numero de columnas en la tabla de ajedrez

#Dependiendo de la suma entre f y c, se determina si la casilla de abajo a la derechaes blanca o negra. 
#Dado a que es un patron de "si, no, si, no...", se puede determinar la asignacion del color dependiendo de si la 
#el NUMERO de la casilla es PAR o IMPAR
if ((f or c) > 1000) or ((f or c) < 1):
    if (f or c) > 1000:
        print("El numero de filas o columnas es muy alto")
    if (f or c) < 1:
        print("El numero de filas o columnas es muy bajo")
else:
    if (f + c) % 2 == 0:    #Si la suma del numero de filas y columnas es par, el color de la casilla es blanco
        print("#FFFFFF")
    if (f + c) % 2 == 1:    #Si la suma del numero de filas y columnas es impar, el color de la casilla es negro
        print("#000000")