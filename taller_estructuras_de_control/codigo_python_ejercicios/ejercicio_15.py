#Calculadora de descuento
precio_final = float(input("Digite el precio final: "))
valor_producto = float(input("Digite el precio de venta al publico (PVP): "))
valorf = abs((valor_producto - precio_final) / valor_producto)
descuento = valorf * 100
print(f"El porcentaje de descuento que fue aplicado fue de {descuento}%")