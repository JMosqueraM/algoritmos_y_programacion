# Segun la tabla de deportes a realizar segun la temperatura
# dada en grados farenheit, desarrolle un algoritmo que permita
# conocer el deporte que se pueda realizar segun la temperatura

temp = int(input("Ingrese la temperatura en grados farenheit: "))
deporte = ""

if temp > 85:
    deporte = "Natacion"
elif (temp > 70) and (temp <= 85):
    deporte = "Tenis"
elif (temp > 32) and (temp <= 70):
    deporte = "Golf"
elif (temp > 10) and (temp <=32):
    deporte = "Esquí"
else:
    deporte = "Marcha"

print(f"Ya que la temperatura es de {temp}°F, se puede practicar {deporte}")