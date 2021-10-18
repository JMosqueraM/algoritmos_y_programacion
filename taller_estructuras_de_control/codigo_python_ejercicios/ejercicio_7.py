#Convertir metros a pies y pulgadas
#Tenga en cuenta que 1m = 39.27pulgadas, y 1pie = 12pulgadas
metros = float(input("Ingrese la cantidad de metros:"))

metros_pulgada = round(metros * 39.27, 2)
pulgada_pie = round(metros_pulgada / 12, 2)

print(f"{metros} metros son {metros_pulgada} pulgadas y {pulgada_pie} pies")