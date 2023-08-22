dato = int(input("Dime un numero: "))
if dato > 0:
   print("Es positivo")
else:
   print("Es negativo o 0")
print("El numero que ingreso es", dato)


#Ejercicios
#4.1. Pide al usuario un número entero y responde si es par o impar (pista: es par si el resto de la división entre 2 es 0).
num1 = int(input("Introduce un numero entero: "))
if num1 % 2 == 0:
   print("Es un numero par")
else:
   print("Es un numero impar")


#4.2. Pide un número real y responde si es positivo, negativo o cero (pista: deberás enlazar dos "if").
num2 = float(input("Introduce un numero real: "))
if num2 > 0:
   print("Es un numero positivo")
else:
   if num2 < 0:
      print("Es un numero negativo")
   else:
      print("Es 0")


#4.3. Pide dos números enteros y muestra en pantalla su división (o el mensaje de aviso "no se puede dividir entre cero" si el segundo es cero).
num3 = int(input("Ingrese un numero entero: "))
num4 = int(input("Ingrese otro numero entero: "))
if num4 != 0:
   print("El resultado es", num3//num4)
else:
   print("No se puede dividir por 0")