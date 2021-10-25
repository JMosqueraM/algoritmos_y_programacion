# Calcule el valor final a pagar segun las condiciones de kilometros y el valor a cancelar

kilometros= int(input("Ingrese los kilometros recorrido: "))
monto_base = 50000
cancelar = 0 

if kilometros <= 300:
    cancelar = monto_base

elif kilometros < 1000:
    cancelar = monto_base + 70000 + (30000 * (kilometros - 300))
elif kilometros > 1000:
    cancelar = 150000 + (9000 * (kilometros - 300))

print(f"El monto pagado al cliente sera de: {cancelar:,}$")