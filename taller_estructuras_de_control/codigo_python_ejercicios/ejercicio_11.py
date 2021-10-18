# Calcular las asignaciones, deducciones y el sueldo neto de un 
# trabajador para el mes de Diciembre

#Entradas
nombre = input("Ingrese el nombre del trabajador: ")
num_horas = float(input("Ingrese el numero de horas trabajadas por el trabajador: "))
pago_horas = float(input("Ingrese el precio por hora trabajada: "))
numero_horas_extra = float(input("Ingrese el numero de horas extra trabajadas por el trabajador: "))
sueldo_base = float(input("Ingrese el valor del sueldo base del trabajador: "))
num_hijos = int(input("Ingrese el numero de hijos del trabajador: "))

#Calculo valores
pago_horas_extra = pago_horas * 1.25
pago_forzoso = sueldo_base * 0.05
politica_habitacional = round(sueldo_base * 0.02, 2)
caja_ahorro = round(sueldo_base * 0.07, 2)
acta_academica = 250000
subsidio_hijo = round(173_000 * num_hijos, 2)
prima_hogar = 180_000
sueldo_semi_neto = round((pago_horas * num_horas) + (numero_horas_extra * pago_horas_extra) + sueldo_base, 2)

# Asignaciones, Deducciones, y Sueldo Neto del trabajador
asignaciones = round(acta_academica + subsidio_hijo + prima_hogar, 2)
deducciones = round(pago_forzoso + politica_habitacional + caja_ahorro ,2)
sueldo_neto = round(sueldo_semi_neto - deducciones, 2)

print(f"Teniendo en cuenta que el acta academica vale {acta_academica}$, el subsidio para los hijos del trabajador es {subsidio_hijo} $, y la prima del hogar es {prima_hogar}$, las asignaciones para el trabajador equivalen a un total de {asignaciones}$ ")
print(" ")
print(f"Si el salario base del trabajador es {sueldo_base}$, el pago forzoso equivale al 5% ({pago_forzoso}$), la politica habitacional equivale al 2% ({politica_habitacional}$), y la caja de ahorro equivale al 7%({caja_ahorro}$). Entonces las deducciones equivalen a un total de {deducciones}$ ")
print(" ")
print(f"Si el sueldo del trabajador (antes de las deducciones) es de {sueldo_semi_neto}$, entonces su sueldo neto luego de las deducciones (que quivalen a ({deducciones}$)) es de {sueldo_neto}$")
