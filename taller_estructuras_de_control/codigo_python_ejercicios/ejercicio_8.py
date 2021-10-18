#Calcular el area de un triangulo en funcion de las longitudes de sus lados
a = float(input("Ingrese el lado 'a' del triangulo: "))
b = float(input("Ingrese el lado 'b' del triangulo: "))
c = float(input("Ingrese el lado 'c' del triangulo: "))

s = (a + b + c) / 2 #Semiperimetro del triangulo
area = round((s * (s - a) * (s - b) * (s - c)) ** (1 / 2), 2) #Area del triangulo

print(f"El traignulo con lados a({a}), b({b}), y c({c}) tiene un semiperimetro de {s}, por lo que su area es de {area}")