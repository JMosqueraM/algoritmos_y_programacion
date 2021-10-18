#Calculo calificacion final Computacion.
print("Ingrese las calificaciones de los parciales")
parcial1 = float(input())
parcial2 = float(input())
parcial3 = float(input())
total_parciales = parcial1 + parcial2 + parcial3
prom_parciales = total_parciales / 3

print("Ingrese la calificacion del examen final")
examen_final = float(input())
print("Ingrese la calificacion del trabajo final")
trabajo_final = float(input())

nota_final = (prom_parciales * 0.55) + (examen_final * 0.3) + (trabajo_final * 0.15)

print(f"Su calificacion final para la materia de computacion es {nota_final}")