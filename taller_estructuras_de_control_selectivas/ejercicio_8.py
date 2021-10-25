# Determine si los valores enteros P y Q satisfacen o  no la expresion P^3 + Q^4 - 2 * P^2 > 680

P = int(input("Ingrese el valor de P: "))
Q = int(input("Ingrese el valor de Q: "))

valor_expresion = (P**3) + (Q**4) - 2 * (P**2)

if valor_expresion > 680:
    print (f"Para los valores de P ({P}) y Q ({Q}) satisfacen la expresión")
else:
    print (f"Para los valores de P ({P}) y Q ({Q}) no satisfacen la expresión")
    