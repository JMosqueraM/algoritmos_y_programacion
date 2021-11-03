# Calcule el término doceavo y la suma de los doce primeros términos
# de la sucesión: 6, 11, 16, 21...
sucesion = []
total = 0
for i in range(1, 13):
    num = (5 * i) + 1
    sucesion.append(num)
for i in range(12):
    total += sucesion[i]
print(f"El doceavo elemento de la sucesion 6, 11, 16, 21... es: {sucesion[11]}")
print(f"Y la sumatoria de los elementos de la sucesion es: {total}")
