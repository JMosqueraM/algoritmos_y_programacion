while True:
    datos = input("")
    dato = datos.split(" ")
    X_str = dato[0]
    M_str = dato[1]
    X = int(X_str)
    M = int(M_str)
    if (X == 0) and (M == 0):
        break
    elif ((X > 0) and (X <= 3)) == False: 
        break
    elif ((M >= 10) and (M <= (2**32) - 1)) == False: 
        break
    else:
        E = X * M
    print(E)
