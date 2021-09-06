monto = float(input("Monto adeudado: "))

cliente = input("Es cliente? 'SI' para indicar si: ")

if cliente == 'SI':
    descuento = int(input("Porcentanje de descuento: "))
    monto = monto-((descuento/100)*monto)
print("Monto a pagar: $", monto)