# Segun la tabla de Categorias | Aumentos | Salarios brutos, muestre la categoria
# del trabajador, y su nuevo salario

categoria = int(input("Ingrese la categoria del trabajador: "))
salario_bruto = int(input("Ingrese el salario bruto del trabajador: "))
aumento = 0
nuevo_salario = 0

if categoria == 1:
    aumento = 1.10

if categoria == 2:
    aumento = 1.15

if categoria == 3:
    aumento = 1.20

if categoria == 4:
    aumento = 1.40

if categoria == 5:
    aumento = 1.60

str_aumento = str(round(((aumento - 1.00)) * 100)) + "%"
nuevo_salario = round(salario_bruto * aumento, 3)
print(f"Siendo que el trabajador esta en la categoria {categoria}, tiene un salario bruto de {salario_bruto:,}$, y le corresponde un aumento del {str_aumento}. Su nuevo salario bruto será de {nuevo_salario:,}$")


