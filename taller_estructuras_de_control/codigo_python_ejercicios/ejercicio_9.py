#Calcular el salario neto de un tnrabajador en fucion del numero de horas trabajadas, el precio de la hora
#y el descuento fijo al sueldo base por concepto de impuestos del 20%

horas = float(input("Ingrese el numero de horas trabajadas: "))
precio_hora = float(input("Ingrese el precio por hora trabajada: "))
sueldo_base = float(input("Ingrese el valor del sueldo base: "))
pago_hora = horas * precio_hora
impuesto = 0.2
salario_neto = pago_hora + (sueldo_base * 0.8)

print(f"Si el trabajador tiene un sueldo base de {sueldo_base}$ (al cual se le descuenta un 20% por impuestos), trabaja {horas} horas, y la hora se le paga a {precio_hora}$.")
print(f"El salario neto del trabajador es de {salario_neto}$")