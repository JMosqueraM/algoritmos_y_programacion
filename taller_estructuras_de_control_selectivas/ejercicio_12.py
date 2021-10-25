# Dada una cantidad de pesos colombianos (COP), desglose dicha
# cantidad en los billetes y monedas de curso legal en el pais

cop = int(input("Ingrese una cantidad entera de pesos colombianos (COP): "))
cop_str = str(cop)
billetes = [100_000, 50_000, 20_000, 10_000, 5_000, 2_000, 1_000, 500, 200, 100, 50]
nuevo_cop = 0
cantidad_unidad = [ 0 for i in range(11)]


for i in range(len(billetes)):
    if cop // billetes[i] > 0:
        cantidad_unidad[i] = (cop // billetes[i])
        cop = cop - (cantidad_unidad[i] * billetes[i] )

billetes_cantidades_zip = zip(billetes, cantidad_unidad)
lista_zip = list(billetes_cantidades_zip)
lista_f_ceros = list((lista_zip[i][0] * lista_zip[i][1]) for i in range(11))
lista_f_no_ceros = list(dict.fromkeys(lista_f_ceros))
lista_f_no_ceros.remove(0)

print(*lista_f_no_ceros , sep = ",")

