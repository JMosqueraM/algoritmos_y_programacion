# Segun el numero de 4 digitos (entero y positivo) conformado por A, B, C, y D (de la forma ABCD).
# Redondee el numero a la centecima mas cercana

A = int(input("digite el valor A: "))
B = int(input("digite el valor B: "))
C = int(input("digite el valor C: "))
D = int(input("digite el valor D: "))

# Redondear el valor de la variable de la unidad
if D > 5:
    C += 1

# Redondear el valor de la variable de decima
if C > 5:
    B += 1

# Redondear el valor de la variable de centecima
if B > 5:
    A += 1

# Convertir los digitos de las variables en cadenas para crear el numero
A = str(A)
B = str(B)
C = str(C)
D = str(D)

# Creacion del numero sumando los caracteres de las variables A, B, C, y D
num = A + B + C + D
# Redondeo final al numero si en el proceso anterior de redondeo el numero terminaba constando de mas de 4 digitos
if len(num) > 4:
    B = str(int(B) * 0)
    C = str(int(C) * 0)
    D = str(int(D) * 0)
    num = A + B + C + D

# Redondeo final al numero si en el proceso anterior de rendonde el numero terminaba constando mas de 3 digitos
elif len(num) > 3:
    C = str(int(C) * 0)
    D = str(int(D) * 0)
    num = A + B + C + D
print(num)
