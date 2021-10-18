#Un vendedor recibe un sueldo base, más un 10% extra por comisiones de sus ventas
sueldo_base = float(input("Ingrese su sueldo base "))

venta1 = float(input("Ingrese el valor de la primera venta: ")) * 0.1
venta2 = float(input("Ingrese el valor de la segunda venta: ")) * 0.1
venta3 = float(input("Ingrese el valor de la tercera venta: ")) * 0.1
total_ventas_mes = venta1 + venta2 + venta3

print(f"Teniendo en cuenta que el salario del vendedor es de {sueldo_base}$, y tuvo un acumulado total de {total_ventas_mes}$ de las ganancias por comisiones de sus ventas en el mes.")
print(f"Su ganancia total en el mes es de {total_ventas_mes + sueldo_base}$ ")
