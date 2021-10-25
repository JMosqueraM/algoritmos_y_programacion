# Calcule el costo a pagar por concepto de consumo de luz
# electrica y servicio de aseo urbano segun la escala proveida

lectura_actual = int(input("Ingrese el valor de la lectura actual: "))
lectura_anterior = int(input("Ingrese el valor de la lectura anterior: "))
diferencia = abs(lectura_anterior - lectura_actual)
costo = 0

if diferencia >= 0 and diferencia <= 100:
    costo = 4_600

elif diferencia >= 101 and diferencia <= 300:
    costo = 80_000

elif diferencia >= 310 and diferencia <= 500:
    costo = 100_000

elif diferencia >= 501:
    costo = 120_000

costo_final = diferencia * costo
print(costo)
print(f"Siendo que la lectura actual es de {lectura_actual} y la lectura anterior es de {lectura_anterior}, el precio segun la tabla de Kwh es de {costo:,}$, por lo que ha de pagar {costo_final:,} concepto de consumo de luz electrica y el servicio de aseo urbano.")