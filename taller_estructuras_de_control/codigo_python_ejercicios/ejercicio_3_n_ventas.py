#Un vendedor recibe un sueldo base, más un 10% extra por comisiones de sus ventas
sueldo_base = float(input("Ingrese su sueldo base "))
ventas_mes = int(input("Cuantas ventas hizo en el mes? "))
total_ventas_mes = 0

#Este loop capta el valor de cada una de las ventas realizadas en el mes, y guarda el total de las comisiones ganada de cada venta
for i in range(ventas_mes):
    globals()['venta_comision%s' % i] = 0
    print(f"Ingrese el valor de la venta {i +1}")
    globals()['venta_comision%s' % i] = float(input()) * 0.1
    total_ventas_mes += globals()['venta_comision%s' % i]

print(f"Teniendo en cuenta que el salario del vendedor es de {sueldo_base}$, realizó {ventas_mes} ventas en el mes, y tuvo un acumulado total de {total_ventas_mes}$ de las ganancias por comisiones")
print(f"Su ganancia total en el mes es de {total_ventas_mes + sueldo_base}$ ")