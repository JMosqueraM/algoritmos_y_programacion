#Calcular porcentaje de hombres y mujeres en un grupo de estudiantes
num_estudiantes = int(input("Ingrese el numero de estudiantes en el salon: "))
num_hombres = int(input("Ingrese el numero de estudiantes hombres en el salon: "))
num_mujeres = int(input("Ingrese el numero de estudiantes mujeres en el salon: "))
porcentaje_hombres = round(((num_hombres * 100) / num_estudiantes), 2)
porcentaje_mujeres = round(((num_mujeres * 100) / num_estudiantes), 2)

print(f"En un salon de {num_estudiantes} estudiantes, donde hay {num_hombres} hombres y {num_mujeres} mujeres, se puede determinar que:")
print(f"El {porcentaje_hombres}% de los estudiantes de la clase son hombres, y {porcentaje_mujeres}% de los estudiantes de la clase son mujeres.")