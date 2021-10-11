#Un individuo desea saber cuanto dinero ganará despues de un mes, si el banco paga a rezon del 2% mensual
deposito = float(input("Cuanto dinero deposito al inicio del mes? "))
ganancia_mensual = 0.02 * deposito
print("Despues de un mes, usted ganará", str(ganancia_mensual) + "$")