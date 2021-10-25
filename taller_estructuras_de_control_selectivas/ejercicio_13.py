# Desarrolle un un programa que reciba la fecha de nacimiento
# de una persona, y como salida, indique el nombre del signo del
# zodiaco correspondiente, ademas de su edad
def zodiaco(DD, MM):
    if (((DD >= 22) and (MM == 11)) or ((DD <=21) and (MM == 12))):
        return("Sagitario")

    if (((DD >= 22) and (MM == 12)) or ((DD <=20) and (MM == 1))):
        return("Capricornio")

    if (((DD >= 21) and (MM == 1)) or ((DD <=19) and (MM == 2))):
        return("Acuario")

    if (((DD >= 20) and (MM == 2)) or ((DD <=19) and (MM == 3))):
        return("Piscis")

    if (((DD >= 21) and (MM == 3)) or ((DD <=20) and (MM == 4))):
        return("Aries")

    if (((DD >= 21) and (MM == 4)) or ((DD <=21) and (MM == 5))):
        return("Tauro")

    if (((DD >= 22) and (MM == 5)) or ((DD <=21) and (MM == 6))):
        return("Geminis")

    if (((DD >= 22) and (MM == 6)) or ((DD <=22) and (MM == 7))):
        return("Cancer")

    if (((DD >= 23) and (MM == 7)) or ((DD <=23) and (MM == 8))):
        return("Leo")

    if (((DD >= 24) and (MM == 8)) or ((DD <=22) and (MM == 9))):
        return("Virgo")

    if (((DD >= 23) and (MM == 9)) or ((DD <=22) and (MM == 10))):
        return("Libra")

    if (((DD >= 23) and (MM == 10)) or ((DD <=21) and (MM == 11))):
        return("Escorpion")

fecha_str = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
fecha = fecha_str.split("/")
fecha_int = []
for elemento in fecha:
    fecha_int.append(int(elemento))
dia = fecha_int[0]
mes = fecha_int[1]
ano = fecha_int[2]
signo = zodiaco(dia, mes)

print(f"Siendo que su fecha de nacimiento es {fecha_str}, su signo zodiacal corresponde a {signo} y tiene {abs(ano - 2021)} años")