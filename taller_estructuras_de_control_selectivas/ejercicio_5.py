# Determine el nuevo sueldo a pagar a partir de los criterios definidos para los incentivos
# de incremento de procuctividad

sueldo = int(input("Ingrese el salario bruto mensual: "))
venta_A = int(input("Ingrese el valor de ventas del departamento A: "))
venta_B = int(input("Ingrese el valor de ventas del departamento B: "))
venta_C = int(input("Ingrese el valor de ventas del departamento V: "))

total_ventas = venta_A + venta_B + venta_C
porcentaje_limite = total_ventas * 0.33

if venta_A > porcentaje_limite:
    sueldo_A = sueldo + (sueldo * 0.20)
else:
    sueldo_A = sueldo

if venta_B > porcentaje_limite:
    sueldo_B = sueldo + (sueldo * 0.20)
else:
    sueldo_B = sueldo

if venta_C > porcentaje_limite:
    sueldo_C = sueldo + (sueldo * 0.20)
else:
    sueldo_C = sueldo

print(f"Siendo que los vendedores del departamento A realizaron un acumulado de ventas de {venta_A:,}$ y el 33% de las ventas totals equivalen a {porcentaje_limite}, los trabajadores recibiran un sueldo de {sueldo_A}") 
print(f"Siendo que los vendedores del departamento B realizaron un acumulado de ventas de {venta_B:,}$ y el 33% de las ventas totals equivalen a {porcentaje_limite}, los trabajadores recibiran un sueldo de {sueldo_B}") 
print(f"Siendo que los vendedores del departamento C realizaron un acumulado de ventas de {venta_C:,}$ y el 33% de las ventas totals equivalen a {porcentaje_limite}, los trabajadores recibiran un sueldo de {sueldo_C}") 
