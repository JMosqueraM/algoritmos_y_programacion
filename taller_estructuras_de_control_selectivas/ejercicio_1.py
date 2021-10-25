# Un hombre desea saber cuánto dinero se generará por concepto de intereses sobre la cantidad que tiene en
# inversión en el banco. El decidirá reinvertir los intereses siempre y cuando éstos excedan a $100.000 COP
# y en ese caso, desea saber cuánto dinero tendrá finalmente en su cuenta.

deposito = float(input("Ingrese la cantidad depositada al banco: "))
tasa_interes = float(input("Ingrese la tasa de interes: "))
ganancia = deposito * tasa_interes

if ganancia > 100_000:
    print(f"Las ganancias por concepto de la tasa de interes ({tasa_interes}%) sobre la cantidad inicial depositada (${deposito:,}) supera los $100,000. Debido a lo anterior podra reinvertir estas ganancias en su cuenta, por lo que tendra en su cuenta un acumulado de ${ganancia:,}")

else:
    print(f"Las ganancias por concepto de la tasa de interes ({tasa_interes}%) sobre la cantidad inicial depositada (${deposito:,}) NO supera los $100,000. Debido a lo anterior NO podra reinvertir las ganancias (${ganancia:,}) en su cuenta, por lo que tendra en su cuenta un acumulado de ${deposito:,}")
  