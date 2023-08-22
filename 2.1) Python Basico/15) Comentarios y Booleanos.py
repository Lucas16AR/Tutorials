#Este es un comentario que python no tomara para ejecutar
#Por Lucas Galdame
#Se usan para detalles no evidentes o importantes

#Ejercicios
#14.1. Pide al usuario dos números enteros, y da el valor True a una variable booleana llamada "ambosPares" en caso de que las dos sean pares, o el valor False en caso contrario. El programa debe comenzar con un comentario que diga de qué trata y otro que diga tu nombre.
n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro número: "))
ambosPares = (n1 % 2 == 0) and (n2 % 2 == 0)
print("Ambos pares?", ambosPares)