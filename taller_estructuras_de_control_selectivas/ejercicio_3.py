#Dados los datos A, B, C y D que representan números enteros; escriba un algoritmo que calcule el resultado de las siguientes expresiones:
A = int(input("Ingrese el valor del numero entero A: "))
B = int(input("Ingrese el valor del numero entero B: "))
C = int(input("Ingrese el valor del numero entero C: "))
D = int(input("Ingrese el valor del numero entero D: "))


if D < 0:
    operacion = (A - C) ** 2
    print(f"Siendo A, B, C y D son iguales a {A}, {B}, {C}, y {D} (respectivamente). La operacion (A - C)^2 = ({A} - {C})^2 = {operacion}")
elif D > 0:
    operacion = ((A - B) ** 3) / D
    print(f"Siendo A, B, C y D son iguales a {A}, {B}, {C}, y {D} (respectivamente). La operacion ((A - B)^3) / D = (({A} - {B})^3) / {D} = {operacion}")
