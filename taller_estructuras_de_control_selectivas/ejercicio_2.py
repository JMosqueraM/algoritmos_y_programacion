# Escriba  un  algoritmo,  que  dado  como  dato  el  sueldo  de  un  trabajador,  le aplique un aumento del 15%
# si su salario bruto es inferior a $900.000 COP y 12% en caso contrario. Imprima el nuevo sueldo del trabajador.
salario_bruto = float(input("Ingrese el valor del sueldo bruto: "))

if salario_bruto < 900_000:
    aumento_porcentaje = 15
    aumento = salario_bruto * 0.15

elif salario_bruto> 900_000:
    aumento_porcentaje = 12
    aumento = salario_bruto * 0.12

nuevo_sueldo = aumento + salario_bruto
print(f"Si el salario bruto del trabajador es ${salario_bruto:,} le corresponde un aumento del {aumento_porcentaje}% (${aumento:,}), por lo que su nuevo sueldo seria de ${nuevo_sueldo:,}")


