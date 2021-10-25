"""
Una empresa quiere hacer una compra de varias piezas de la misma clase a un 
fabricante de refacciones. La empresa dependiendo del monto total de la compra, 
decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede 
de  $5.000.000  COP  la  empresa  tendrá  la  capacidad  de  invertir  de  su  propio 
dinero  un 5 5 % del monto de la compra, pedir presta al banco un 30% y el resto lo 
pagará  solicitando  un  crédito  al  fabricante.  Si  el  monto  total  de  la  compra  no 
excede  de $5.000.000 COP la empresa tendrá capacidad de invertir de su propio 
dinero  un  70%  y  el  restante  30%  lo  pagará  solicitando  crédito  al  fabricante.  El 
fabricante  cobra  por  concepto  de  intereses  un  20%  sobre  la  cantidad  que  se  le 
pague  a  crédito.      Calcule  y  muestre  la  cantidad  a  invertir  de  los  fondos  de  la 
empresa,  la  cantidad  a  pagar  a  crédito,  el  monto  a  pagar  por  intereses  y  si  es 
necesario, la cantidad prestada al banco.
"""

piezas = int(input("Ingrese el numero de piezas: "))
costo_piezas = int(input("Ingrese el costo de las piezas: "))
total = piezas * costo_piezas

# Si el monto total de la compra excede de $5,000,000
if total > 5_000_000:
    inv = total * 0.55
    banco = total * 0.30
    credito_fabricante = total * 0.15

# Si el monto total de la compra no excede de $5,000,000
elif total < 5_000_000:
    inv = total * 0.70
    credito_fabricante = total * 0.30
    banco = 0

interes = credito_fabricante * 0.20

print(f"Siendo que se necesitan {piezas} piezas, y estas valen ${costo_piezas:,}: ")
print(f"La inversion va a ser de ${inv:,}")
print(f"El prestamo del banco va a ser de ${banco:,}")
print(f"El credito a pagar por la compra va a ser de ${credito_fabricante:,}")
print(f"El interes por el credito toma es de ${interes:,}")


