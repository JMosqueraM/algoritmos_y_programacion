archivo = open("paises.txt", "r")
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""

# print(archivo.read())
lista = []
lista_temp = []

with open("paises.txt", "r") as archivo:
    for linea in archivo:
        linea = linea[:-1]
        #print(linea)
        pais, ciudad = linea.split(": ")
        lista_temp.append(pais)
        lista_temp.append(ciudad)
        lista.append(lista_temp.copy())
        #print(lista_temp)
        lista_temp.pop()
        lista_temp.pop()

#Cuente e imprima cuantas ciudades inician con la letra M  
""" contadorCiuM = 0
ciudadesM = []
for i in range(len(lista)):
  if list(lista[i][1])[0] == 'M':
    contadorCiuM += 1
    ciudadesM.append(lista[i][1])
print(f"--> Hay {contadorCiuM} ciudades que inician con la letra M, y estas son:")
for i in range(len(ciudadesM)):
  print(f"- {ciudadesM[i]}")
print("") """

#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
""" print("--> Lista de los paises cuyo inicio sea con la letra U:")
for i in range(len(lista)):
  if list(lista[i][0])[0] == 'U':
    print(f"- {lista[i][0]}")
print("")

print("--> Lista de las ciudades cuyo inicio sea con la letra U:")
for i in range(len(lista)):
  if list(lista[i][1])[0] == 'U':
    print(f"- {lista[i][1]}")
print() """

#Cuente e imprima cuantos paises que hay en el archivo
""" print(f"--> Hay {len(lista)} paises en el archivo, y estos son:")
for i in range(len(lista)):
  print(f"- {lista[i][0]}")
print() """

#Busque e imprima la ciudad de Singapur
""" for i in range(len(lista)):
  for j in range(2):
    if lista[i][j] == "Singapur":
      print(f"--> Singapur esta en la posicion {i + 1}")
      print(f"    Pais ID #163: {lista[i][0]}")
      break
print() """

#Busque e imprima el pais de Venezuela y su capital
""" for i in range(len(lista)):
  for j in range(2):
    if lista[i][j] == "Venezuela":
      print(f"--> Venezuela esta en la posicion {i + 1}")
      print(f"    Pais ID #{i + 1}: {lista[i][0]}. ")
      print(f"    Ciudad ID #{i + 1}: {lista[i][1]}. ")
print() """

#Cuente e imprima las ciudades que su pais inicie con la letra E
""" contadorCiuE = 0
ciudadesE = []
for i in range(len(lista)):
  if list(lista[i][1])[0] == 'E':
    contadorCiuE += 1
    ciudadesE.append(lista[i][1])
print(f"--> Hay {contadorCiuE} ciudades que inician con la letra E, y estas son:")
for i in range(len(ciudadesE)):
  print(f"- {ciudadesE[i]}")
print("") """

#Busque e imprima la Capiltal de Colombia
""" for i in range(len(lista)):
  for j in range(2):
    if lista[i][j] == "Colombia":
      print(f"--> Colombia esta en la posicion {i + 1}")
      print(f"    Pais ID #{i + 1}: {lista[i][0]}. ")
      print(f"    Ciudad ID #{i + 1}: {lista[i][1]}. ")
print() """

#imprima la posicion del pais de Uganda
""" for i in range(len(lista)):
  for j in range(2):
    if lista[i][j] == "Uganda":
      print(f"--> Uganda esta en la posicion {i + 1}")
print() """

#imprima la posicion del pais de Mexico
""" for i in range(len(lista)):
  for j in range(2):
    if lista[i][j] == "Mexico":
      print(f"--> Mexico esta en la posicion {i + 1}")
print() """

"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo
de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde
se vaya contento por su trabajo. Utilice un For para cambiar ese Dato.
"""
""" archivo = open("paises.txt", "r")
lineas = archivo.readlines()
for i in range(len(lista)):
  for j in range(2):
    if lista[i][j] == "Madagascar":
      if lista[i][1] != "Antananarivo":
        print(f"{lista[i][0]}: {lista[i][1]} NO es la informacion correcta...")
        print("La capital de Madagascar es Antananarivo... INFORMACION ACTUALIZADA EN EL ARCHIVO")
        lineas[i] = "Madagascar: Antananarivo\n"
        lista[i][1] = "Antananarivo"
        archivo = open("paises.txt", "w")
        archivo.writelines(lineas)
        print(f"{lista[i][0]}: {lista[i][1]} ES es la informacion correcta...")
print() """


#Agregue un país que no esté en la lista 
""" print("Lista ORIGINAL de paises:")
for i in range(len(lista)):
  print(f"- {lista[i][0]}")

pais = input("Ingrese el nombre de un pais que no se encuentre en la lista: ")

archivo = open("paises.txt", "r")
lineas = archivo.readlines()
lineas.append(f"\n{pais}: ")
lista.append([])
lista[-1].append(f"{pais}")
archivo = open("paises.txt", "w")
archivo.writelines(lineas)

print("Lista ACTUALIZADA de paises:")
for i in range(len(lista)):
  print(f"- {lista[i][0]}") """


archivo.close()