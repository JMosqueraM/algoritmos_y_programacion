# Efectua la division de dos numeros enteros utilizando el 
# metodo de restas sucesivas



A = int(input("Ingrese el numero de actuara de dividendo: "))
B = int(input("Ingrese el numero de actuara de divisor: "))
restante = A
i = 0

print(f"Operacion a realizar: {A} / {B}")
print("Restas:")
while restante >= 0:
    resultado = A - B
    if resultado < 0:
        break
    else:
        resultado = A - B
        print(f"{restante} - {B} = {resultado}")
        restante = resultado
        A = resultado
        i += 1

print(f"Ya que se realizaron {i} restas, al evaluar la operacion {A}/{B}, se obtiene como resultado {i}")

