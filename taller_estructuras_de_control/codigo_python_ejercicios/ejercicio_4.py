#Una tienda tiene un descuento del 15%, cuanto pagara en total el cliente?
descuento = 0.15
valor_producto = float(input("Ingrese el valor del producto "))
valor_producto_descuento = valor_producto - (valor_producto * descuento)
print(f"Sin el descuento del 15%, usted pagaria {valor_producto}$, pero con el descuento pagará {valor_producto_descuento}$")
