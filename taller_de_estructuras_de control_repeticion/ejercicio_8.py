# Escribe un programa que siga leyendo la contraseña hasta que sea valida.
# Por cada intento errado, muestre el mensaje "Senha inválida". Cuando la
# contraseña es correcta, muestre el mensaje "Acesso Permitido", y finalice
# el programa. La contraseña correcta es INT 2002

password = 2002
attempt = 0
while attempt != password:
    attempt = int(input(""))
    if attempt == password:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")