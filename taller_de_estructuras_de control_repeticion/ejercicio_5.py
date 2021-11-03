# Calcule e imprima el numero de terminos necesarios para que el valor de la sumatoria
# se aproxime lo mas cercanamente a 1000 sin excederlo.
total = 0
i = 0
while total < 1000:
    pre_total = total
    if total < 1000:
        total += ((i + 1)**2 + 1) / (i + 1)
        i += 1
""" for i in range(1, 45, 1):
    total += ((i**2 + 1) / i)
    print(f"Elemento #{i} con sumatoria total = {total}")
print(total) """


print(f"El numero de terminos 'k' necesarios para que el total se aproxime a 1000 sin excederlo es: {i - 1}")
print(f"Ya que la sumatoria realizada hasta el elemento {i - 1} con la formula es igual a: {round(pre_total, 2)}")