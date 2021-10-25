print("Siendo que la funcion de segundo grado tiene la forma: Ax^2 + Bx + 0 = 0, y")
print("el discriminante se calcula con la formula: (B^2) - (4 * A * C).")

A = int(input("Ingrese el valor del coeficiente A: "))
B = int(input("Ingrese el valor del coeficiente B: "))
C = int(input("Ingrese el valor del coeficiente C: "))

D = (B**2) - (4 * A * C)

if D == 0:
    x1 = (-B)/(2 * A)
    print(f"Como D = {D}, entonces x1= x2= {x1}")
elif D > 0:
    x1 = ((-B) + (((B**2)-4*A*C) / (2*A)) ** (1/2))
    x2 = ((-B) - (((B**2) - (4 * A * C) / (2 * A)) ** (1/2)))
    print(f"Siendo D = {D}, entonces x1 = {x1} yy x2 = {x2}")
elif D < 0:
    print(f"Como D = {D} < 0, entonces NO tiene solucion en los reales")