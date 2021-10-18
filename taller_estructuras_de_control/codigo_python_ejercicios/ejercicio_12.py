#Calcular y mostrar la nota final para cada materia, y el promedio general de las tres materias
def calc_matematicas(examen, tarea1, tarea2, tarea3):
    valor_examen = examen * 0.9
    total_tareas = tarea1 + tarea2 + tarea3
    promedio_tareas = total_tareas / 3
    valor_tareas = promedio_tareas * 0.1
    final_matematicas = round(valor_examen + valor_tareas, 2)
    return final_matematicas

def calc_fisica(examen, tarea1, tarea2):
    valor_examen = examen * 0.8
    total_tareas = tarea1 + tarea2
    promedio_tareas = total_tareas / 2
    valor_tareas = promedio_tareas * 0.20
    final_fisica = round(valor_examen + valor_tareas, 2)
    return final_fisica

def calc_quimica(examen, tarea1, tarea2, tarea3):
    valor_examen = examen * 0.85
    total_tareas = tarea1 + tarea2 + tarea3
    promedio_tareas = total_tareas / 3
    valor_tareas = promedio_tareas * 0.15
    final_quimica = round(valor_examen + valor_tareas, 2)
    return final_quimica


examen_matematicas = float(input("Ingrese el resultado del examen de Matematicas: "))
tarea1_matematicas = float(input("Ingrese el valor de la tarea #1 de Matematicas: "))
tarea2_matematicas = float(input("Ingrese el valor de la tarea #2 de Matematicas: "))
tarea3_matematicas = float(input("Ingrese el valor de la tarea #3 de Matematicas: "))

examen_fisica = float(input("Ingrese el resultado del examen de Fisica: "))
tarea1_fisica = float(input("Ingrese el valor de la tarea #1 de Fisica: "))
tarea2_fisica = float(input("Ingrese el valor de la tarea #2 de Fisica: "))

examen_quimica = float(input("Ingrese el resultado del examen de Quimica: "))
tarea1_quimica = float(input("Ingrese el valor de la tarea #1 de Quimica: "))
tarea2_quimica = float(input("Ingrese el valor de la tarea #2 de Quimica: "))
tarea3_quimica = float(input("Ingrese el valor de la tarea #3 de Quimica: "))

promedio_total = round(((calc_matematicas(examen_matematicas, tarea1_matematicas, tarea2_matematicas, tarea3_matematicas) + calc_fisica(examen_fisica, tarea1_fisica, tarea2_fisica) + calc_quimica(examen_quimica, tarea1_quimica, tarea2_quimica, tarea3_quimica)) / 3), 2)
print(f"Si la nota de Matematicas es {calc_matematicas(examen_matematicas, tarea1_matematicas, tarea2_matematicas, tarea3_matematicas)}, la de Fisica es {calc_fisica(examen_fisica, tarea1_fisica, tarea2_fisica)}, y la de Quimica es {calc_quimica(examen_quimica, tarea1_quimica, tarea2_quimica, tarea3_quimica)}. Entonces el promedio de las materias es {promedio_total}")
