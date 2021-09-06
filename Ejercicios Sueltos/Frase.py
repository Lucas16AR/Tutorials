frase = input("Escribi una frase toda en minuscula: ")
cantidad = 0

for caracter in frase:
    if caracter == "a":
        cantidad = cantidad + 1
print("Cantidad de 'a' en la frase: ", cantidad)