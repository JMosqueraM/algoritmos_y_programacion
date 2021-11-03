# Escriba un programa que registre el tipo de combustible comprado
# por los clientes. 1) Alcool 2) Gasoline 3) Diesel 4)End. Cualquier
# numero por fuera del rango (1 - 4) pedira un input del usuario (nombre)
# de la cueta

Alcool=0
Gasolina=0
Diesel=0

while True:
    num = int(input(""))
    if num == 1:
        Alcool += 1 
    elif num == 2:
        Gasolina += 1
    elif num == 3:
        Diesel += 1
    elif num == 4:
        break
    else:
        num == num

print(f"""MUITO OBRIGADO
Alcool: {Alcool}
Gasolina: {Gasolina}
Diesel: {Diesel}""")