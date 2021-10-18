#Calcular y mostrar el monto total a pagar de electricidad
num_lectura = int(input("Ingrese el numero actual de la lectura: "))
num_lectura_pasada = int(input("Ingrese el numero actual de la lectura pasada: "))
costo_kilovatio = float(input("Ingrese el costo del kilovatio por hora: "))
total = num_lectura - num_lectura_pasada
total_pagar = total * costo_kilovatio
print(f"El total a pagar de la eletricidad es de {total_pagar}$")