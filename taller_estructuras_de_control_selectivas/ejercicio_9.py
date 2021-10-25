# Determine el total a precio_final con respecto al descuento efectuado segun los criterios

precio =int(input("Ingrese el precio del producto: "))

if precio <50000:
    precio_final = precio
    descuento = 0
elif precio <= 100000:
    descuento = 5
    precio_final=precio-(precio*0.05)
elif precio <= 700000: 
    descuento = 11
    precio_final=precio-(precio*0.11)
elif precio <= 1500000:
    descuento = 18
    precio_final=precio-(precio*0.18)
elif precio>1500000:
    descuento = 25
    precio_final=precio-(precio*0.25)

print(f"Siendo que el precio del producto es de {precio:,}$ y el descuento es del {descuento}%, entonces el precio final a pagar es de {precio_final:,}$")