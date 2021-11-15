lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt

with open("frutas.txt", "r") as archivo:
  lista_frutas_temp = archivo.readlines()
  archivo.close()
  for fruta in lista_frutas_temp:
    fruta = fruta[:-1]
    lista_frutas.append(fruta)

#print(lista_frutas)

""" for fruta in lista_frutas:
  print(fruta) """

with open("numeros.txt", "r") as archivo:
  lista_numeros_temp = archivo.readlines()
  archivo.close()
  for numero in lista_numeros_temp:
    numero = numero[:-1]
    lista_numeros.append(numero)

""" for numero in lista_numeros:
  print(numero) """


#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas: (list: LISTA QUE VA A SER MODIFICADA, str: CARACTER QUE VA A SER ELIMINADO)
Salidas: La lista ingresada pero ahora modificada (con el caracter especifico eliminado en cada uno de sus elementos)

NOTA: Vale recalcar que al ser un caracter "especifico", se distingue entre mayusculas y 
minusculas. De modo que eliminar el caracter 'a' no es lo mismo que liminar el caracter 'A' 
"""
def eliminar_un_caracter_de_toda_la_lista(lista, caracter_eliminar):
  lista_eliminar_caracter = []
  for i in lista:
    a=i.replace(caracter_eliminar,"")
    lista_eliminar_caracter.append(a)
    lista = lista_eliminar_caracter.copy()
  return lista


#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas: (lista: LISTA QUE VA A SER COPIADA)
Salidas: Una copia de la lista ingresada
"""
def copia_lista(lista):
  return lista.copy() 


#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas: (lista: LISTA DE NUMEROS)
Salidas: Lista con los numero PARES de la LISTA DE NUMEROS ingresada
"""  
def numeros_pares(lista):
  lista_numeros_pares = []
  for i in range(0,len(lista)-1):
            if float(lista[i]) % 2 == 0:
              numero_par = lista[i]
              lista_numeros_pares.append(numero_par)
  return lista_numeros_pares  # RetornaUnaLista


#Realizar una funcion que elimine un elemento de una lista
"""
Entradas: (lista: LISTA QUE VA A SER MODIFICADA, elemento_eliminar: ELEMENTO DE LA LISTA QUE SE DESEA ELIMINAR)
Salidas: La lista original con el elemento_eliminar eliminado de ella
"""  
def elimina_elemento_lista(lista, elemento_eliminar):
  lista_elemento_eliminado = []
  for elemento in lista:
    if elemento == elemento_eliminar:
          pass
    else: 
      lista_elemento_eliminado.append(elemento)
  return lista_elemento_eliminado

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas: (lista: LISTA QUE SE DESEA FILTRAR, caracter_filtro; CARACTER POR EL CUAL LA LISTA SERA FILTRADA)
Salidas: La lista ingresada filtrada por el elemento "caracter_filtro"
"""  
def letra(lista, caracter_filtro):
    elementos_filtrados = []
    lista_filtrada = []
    for i in lista:
          if i[0] == caracter_filtro:
                lista_filtrada.append(i)
          else: 
            elementos_filtrados.append(i)
    lista_filtrada.extend(elementos_filtrados)
    return lista_filtrada


#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas: (lista: LISTA QUE SE DESEA INSPECCIONAR)
Salidas: Numero entero positivo con el numero de elementos que posee la lista inspeccionada
"""   
def tamano_lista(lista):
  return len(lista)


#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas: (lsita: LISTA QUE SE DESEA INSPECCIONAR)
Salidas: Numero positivo que indica el numero de elementos que poseee la lista inspeccionada, y el tipo de
         datos contenidos en la lista
"""  
def informacion_lista(lista):
  tamano = len(lista)
  tipos = []
  for i in range(len(lista)):
    if type(lista[i]) not in tipos:
      tipos.append(type(lista[i]))
    else:
      continue
  tamano = f"La lista tiene un tamaño de: {tamano}"
  tipos = f"Y sus elementos son de tipo: {tipos}"
  return tamano, tipos


#Retornar una lista con los numero negativos  
"""
Entradas: lista: LISTA CON NUMEROS REALES COMO ELEMENTOS
Salidas: La lista original ingresada, pero unicamente con los elementos negaivos indexados
"""  
def numeros_negativos(lista):
  lista_original = []
  for numero in lista: 
    lista_original.append(int(float(numero)))
  lista_negativos = lista_original.copy()
  for numero in lista_original: 
    if numero < 0:
        lista_original = lista_original
    elif numero >= 0: 
      lista_negativos.remove(numero)
    else: 
      lista_original = lista_original
  return lista_negativos


#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas: (lista, LISTA QUE VA A SER INSPECCIONADA, elemento_buscado: ELEMENTO QUE SE VA A BUSCAR EN LA LSITA INSPECCIONADA)
Salidas: Indice del elemento buscado en la lista inspeccionada
"""  
def posicion_elemento(lista, elemento_buscado):
  posicion = 0
  for elemento in lista:
    elemento_name = elemento
    if elemento == elemento_buscado:
          posicion +=1
          break
    else: 
      posicion += 1
  return posicion, elemento_name


#realizar una funcion que agregue al final de archivo frutas una fruta
"""
Entradas: (elemento: FRUTA QUE SE DESEA AGREGAR AL ARCHIVO FRUTAS)
Salidas: elemento agregado al archivo frutas.txt
"""  
def frutas(elemento):
  lista = []
  archivo = open("frutas.txt", "r")
  lineas = archivo.readlines()
  lineas.append(f"{elemento}\n")
  lista.append([])
  lista[-1].append(f"{elemento}")
  archivo = open("frutas.txt", "w")
  archivo.writelines(lineas)


#Realizar una funcion que cuente el numero de veces que se repite un elemento  
"""
Entradas: (elemento: ELEMENTO QUE SE DESEA BUSCAR )
Salidas: Numero de veces que aparece el elemento en la lista numeros
"""  
def repetir(elemento):
  veces_en_lista = 0
  for i in lista_numeros:
    if i == elemento:
      veces_en_lista += 1
  return veces_en_lista


  
""" if __name__ == "__main__":
  lista=[1,2,3,4,4]
  copy=copia_lista(lista)
  print(copy) """


""" # Al activar esta seccion, se llama a la funcion eliminar_un_caracter_de_toda_la_lista(), pasandole en dos
# instancias distintas las dos listas que se tienen, eliminando los caracteres 'a' y 2 respectivamente
if __name__ == "__main__":
  lista_mod1 = eliminar_un_caracter_de_toda_la_lista(lista_frutas, "a")
  lista_mod2= eliminar_un_caracter_de_toda_la_lista(lista_numeros, '2')
  print(lista_mod1)
  print(lista_mod2) """


""" # Al activar esta seccion, se llama a la funcion copia_lista(), pasandole como argumento (en dos instancias distintas) la lista
# que se desea copiar. Finalmente, se muestra la lista copiada y la lista original.
if __name__ == "__main__":
    lista_copiada1 = copia_lista(lista_frutas)
    print(f"Esta es la lista de frutas COPIADA: \n --> {lista_copiada1}")
    print("\n")
    print(f"Esta es la lista de frutas ORIGINAL: \n --> {lista_frutas}")
    print("\n")
    lista_copiada2 = copia_lista(lista_numeros)
    print(f"Esta es la lista de numeros COPIADA: \n --> {lista_copiada2}")
    print("\n")
    print(f"Esta es la lista de numeros ORIGINAL: \n --> {lista_numeros}")
    print("\n") """


""" # Al activar esta seccion, se llama a la funcion numeros_pares(), pasandole como argumento (en dos instancias distintas) la lista
# de numeros deseada. Finalmente, se muestra la nueva lista de numeros PARES proveniente de la
# lista de numeros ingresada.
if __name__ == "__main__":
  lista_numeros_pares = numeros_pares(lista_numeros)
  print(lista_numeros_pares) """


""" # Al activar esta seccion, se llama a la funcion elimina_elemento_lista(), pasandole como argumento (en dos instancias distintas) lista_frutas
# y lista_numeros, y eliminando los elementos "Fresa" y "123" respectivamente.
if __name__ == "__main__":
  lista_elemento_eliminado1 = elimina_elemento_lista(lista_frutas, "Fresa")
  print(lista_elemento_eliminado1)
  lista_elemento_eliminado2 = elimina_elemento_lista(lista_numeros, "123")
  print(lista_elemento_eliminado2) """


""" # Al activar esta seccion, se llama a la funcion letra(), pasandole como argumento (en dos instancias distintas) la lista_frutas y lista_numeros,
# filtrando cada lista por los caracteres "A" y "2" respectivamente
if __name__ == "__main__":
    lista_frutas_filtrada = letra(lista_frutas, "A")
    print(lista_frutas_filtrada)
    lista_numeros_filtrada = letra(lista_numeros, "2")
    print(lista_numeros_filtrada) """


""" # Al activar esta seccion, se llama a la funcion tamano_lista(), pasandole como argumento (en dos instancias distintas) la lista_frutas y lista_numeros,
# e imprimiendo el tamaño de cada lista respectivamente
if __name__ == "__main__":
  tamano_lista1 = tamano_lista(lista_frutas)
  print(f"El tamaño de la lista frutas es: {tamano_lista1}")
  tamano_lista2 = tamano_lista(lista_numeros)
  print(f"El tamaño de la lista numeros es: {tamano_lista2}") """


""" # Al activar esta seccion, se llama a la funcion informacion_lista(), pasandole como argumento (en dos instancias distintas) la lista_frutas y lista_numeros,
# y se obtiene la informacion sobre el tamaño y el tipo de datos contenidos en cada lista de forma correspondiente
if __name__ == "__main__":
  informacion_lista_frutas = informacion_lista(lista_frutas)
  print(informacion_lista_frutas[0])
  print(informacion_lista_frutas[1])
  informacion_lista_numeros = informacion_lista(lista_numeros)
  print(informacion_lista_numeros[0])
  print(informacion_lista_numeros[1]) """


""" # Al activar esta seccion, se llama a la funcion numeros_negativos(), pasandole como argumento la lista_numeros,
# y obteniendo como resultado la lista original conteniendo unicamente los numeros negativos
if __name__ == "__main__":
  print(numeros_negativos(lista_numeros)) """


""" # Al activar esta seccion, se llama a la funcion posicion_elemento(), pasandole como argumento (en dos instancias distintas) la lista_frutas y lista_numeros,
# y elemento que se esta buscando (en cada lista). Como resultado, se obtiene el indice (en su lista correspondiente) del elemento.
if __name__ == "__main__":
  posicion_elemento_fruta = posicion_elemento(lista_frutas ,"Aguacate")
  elemento_name = "Aguacate"
  print(f'El elemento "{elemento_name}" en la lista "lista_frutas" se encuentra en la posicion #{posicion_elemento_fruta}')
  posicion_elemento_numero = posicion_elemento(lista_numeros ,"12312")
  elemento_name = "12312"
  print(f'El elemento "{elemento_name}" en la lista "lista_numeros" se encuentra en la posicion #{posicion_elemento_numero}') """


""" # Al activar esta seccion, se llama a la funcion frutas(), pasandole como argumento un elemento. Como resultado, este elemento
# es agregado al final del archivo frutas.txt
if __name__ == "__main__":
  elemento = input("Ingrese el elemento que desee agregar a la lista: ")
  frutas(elemento) """


""" # Al activar esta seccion, se llama la funcion repetir(), pasandole como argumento el elemento que se desea contar en la lista. Como resultado,
# se obtiene el numero de apariciones del elemento en la lista
if __name__ == "__main__":
  buscar_elemento = input("Que elemento desea buscar en la lista? ")
  veces_en = (repetir(buscar_elemento))
  print(f'"{buscar_elemento}" aparece {veces_en} veces') """