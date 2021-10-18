#Determinar el dinero total en un bancon con todas las denominaciones de billetes
mil = 1000
dos_mil = 2000
cinco_mil = 5000
diez_mil = 10000
veinte_mil = 20000
cincuenta_mil = 50000
cien_mil = 100000
cien = 100
quinientos = 500

n1 = int(input("Cuantos billetes N1 hay: "))
n2 = int(input("Cuantos billetes N2 hay: "))
n3 = int(input("Cuantos billetes N3 hay: "))
n4 = int(input("Cuantos billetes N4 hay: "))
n5 = int(input("Cuantos billetes N5 hay: "))
n6 = int(input("Cuantos billetes N6 hay: "))
n7 = int(input("Cuantos billetes N7 hay: "))
n8 = int(input("Cuantos billetes N8 hay: "))

total_dinero = (n1 * cincuenta_mil) + (n2 * veinte_mil) + (n3 * diez_mil) + (n4 * cinco_mil) + (n5 * dos_mil) + (n6 * mil) + (n7 * quinientos) + (n8 * cien)
print(f"Siendo que hay {n1:,}$ billetes N1 que valen {cincuenta_mil:,}$, {n2} billetes N2 que valen {veinte_mil}, {n3} billetes N3 que valen {diez_mil}, {n4} billetes N4 que valen {cinco_mil}, {n5} billetes N5 que valen {dos_mil}, {n6} billetes N6 que valen {mil}, {n7} billetes N7 que valen {quinientos}, y {n8} billetes N8 que valen {cien}")
print(f"En el banco hay un total de {total_dinero:,}$")