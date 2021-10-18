# Calculo de porcentaje de cobro por recargo de computador en el pago por cuota
p = float(input("Ingrese el valor del computador por decontado: "))
t = float(input("Ingrese el valor de cada cuota: "))

total_cop = t * 12
total_diferencia_p = total_cop - p
porcentaje = (total_diferencia_p*100) / p

print(f"El porcentaje de recargo es {porcentaje}%")