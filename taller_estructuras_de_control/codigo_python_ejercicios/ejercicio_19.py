# Calcule el porcentaje de ganancia obtenido porla inversion
precio_lote = float(input("Ingrese el precio del lote de naranjas: "))
precio_docena = float(input("Ingrese el precio de la docena: "))
num_ventas = int(input("Ingrese el numero de ventas: "))
porcentaje_lote = precio_lote / precio_docena
ganancia_naranjas = porcentaje_lote + precio_lote
porcentaje_ganancias = round(num_ventas / ganancia_naranjas, 2)
print(f"Comprando el lote de naranjas a {precio_lote}$, y teniendo en cuenta que la docena se vende a {precio_docena}$. Si el mayorista realizo {num_ventas}, entonces el porcentaje de ganancia fue de {porcentaje_ganancias}%")
