# Imprima los enteros positivos impares menores que 100 omitiendose aquellos que sean divisibles por 7
i = 0
while i < 100:
    if (i % 7) != 0:
        if (i % 2) != 0:
            print(i)
    i += 1
