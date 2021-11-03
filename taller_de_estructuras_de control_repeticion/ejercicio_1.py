# Siendo K < N, escriba un programa que imprima N - 1, N - 2...
# y ai sucesivamente hasta alcanzar el valor de K

print("Tenga en cuenta que K < N")
K = int(input("Ingrese el valor de K: "))
N = int(input("Ingrese el valor de N: "))
i = 0

while N >= K:
    print(N)
    N -= 1
    i += 1