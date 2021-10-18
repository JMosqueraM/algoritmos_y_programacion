# Calcular cantidad de dinero para cada area del hospital
presupuesto = int(input("Digite el presupuesto disponible: "))
ginecologia = presupuesto * 0.4
traumatologia = presupuesto * 0.3
pediatria = presupuesto * 0.3
print(f"Para un presupuesto general de {presupuesto:,}$, el presupuesto para el area de ginecologia es {ginecologia:,}")
print(f"Para un presupuesto general de {presupuesto:,}$, el presupuesto para el area de traumatologia es {traumatologia:,}")
print(f"Para un presupuesto general de {presupuesto:,}$, el presupuesto para el area de pediatria es {pediatria:,}")