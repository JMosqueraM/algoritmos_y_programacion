# Desarrolle un programa que permita calcular y mostrar la suma de
# todos los numeros pares comprendidos entre dos numeros (97 y 1003)

A = int(input("Ingrese un numero A: ")) 
B = int(input("Ingrese un numero B: "))
i = 0
total = 0
lista_numeros = []
if A < B:
    i = A
    while i < B:
        if (i % 2) == 0:
            lista_numeros.append(i)
            total += i
        i += 1
    print(f"Los numeros pares entre {A} y {B} son: {lista_numeros} ")
    print(f"Y su sumatoria es igual a: {total}")
if B < A:
    i = B
    while i < A:
        if (i % 2) == 0:
            lista_numeros.append(i)
            total += i
        i += 1
    print(f"Los numeros pares entre {A} y {B} son: {lista_numeros} ")
    print(f"Y su sumatoria es igual a: {total:,}")

    


