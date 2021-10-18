#Convertidor de:
#Chelines Austriacos --> Pesetas
#Dracmas Griegos --> Francos Franceses
#Pesetas --> Dolares y Liras Italianas

#Primero se definen las funciones para realizar la conversion de moneda
def chelin_a_peseta(chelin):
    taza =  956.871 / 100
    peseta_convertida = round(chelin * taza, 3)
    return peseta_convertida

def dracma_a_franco(dracma):
    taza_dracma_peseta = 88.607 / 100   #Taza de conversion de Dracmas a Pesetas 
    dracma_peseta = dracma * taza_dracma_peseta #Se convierte Dracmas a Pesetas
    taza = 1 / 20.110   #Taza de de conversion de Peseta a Dracma
    dracma_convertida = round(dracma_peseta * taza, 3)
    return dracma_convertida

def franco_a_dracma(franco):
    taza_franco_peseta = 323.728 / 100
    franco_peseta = franco * taza_franco_peseta
    taza = 100 / 88.607
    franco_convertida = round(franco_peseta * taza, 3)
    return franco_convertida

def peseta_a_dolar(peseta):
    taza = 1 / 122.499
    peseta_dolar_convertida = round(peseta * taza, 3)
    return peseta_dolar_convertida

def peseta_a_lira(peseta):
    taza = 100 / 9.289
    peseta_lira_convertida = round(peseta * taza, 3)
    return peseta_lira_convertida

#Se le solicita al usuario que ingrese el valor de las monedas que desee convertir
chelines = float(input("Ingrese el numero de Chelines que desea convertir a pesetas: "))
dracmas = float(input("Ingrese el numero de Dracmas Griegos que desea convertir a Francos Franceses: "))
pesetas = float(input("Ingrese el numero de Pesetas que desea convertir a Dolares y Liras Italianas: "))

#Se le imprime el resultado de la conversion al usuario
print(f"{chelines} Chelines equivalen a {chelin_a_peseta(chelines)} pesetas")
print(f"{dracmas} Dracmas Griegos equivalen a {dracma_a_franco(dracmas)} Francos Franceses")
print(f"{pesetas} Pesetas equivalen a {peseta_a_dolar(pesetas)} Dolares o {peseta_a_lira(pesetas)} Liras Italianas")
#La siguiente linea funciona para comprobar que el la conversion de Francos Franceses
# print(f"{dracma_a_franco(dracmas)} Francos Franceses equivalen a {franco_a_dracma(dracma_a_franco(dracmas))} Francos Franceses")
