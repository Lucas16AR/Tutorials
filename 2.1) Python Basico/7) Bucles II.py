for n in range(1, 10):
   print(n)

for n in range(10, 20):
   print(n)

for n in range(10, 20, 3):
   print(n)

for n in range(20, 10, -1):
   print(n)


#Ejercicios
#7.1. Crea un programa que pida al usuario que introduzca su nombre y un número entero, y escriba su nombre en pantalla tantas veces como indique ese número entero
nombre = input("Ingrese su nombre: ")
numero = int(input("Cantidad de veces que se repetira el nombre: "))
for i in range(0, numero):
   print(nombre)


#7.2. Pide al usuario un número entero (por ejemplo, 5) y muestra la tabla de multiplicar de ese número (desde "5 x 1 = 5" hasta "5 x 10 = 50")
num1 = int(input("Ingrese un numero entero: "))
for i in range(1, 11):
   print(num1, "x", i, "=", num1*i)


#7.3. Pide al usuario un número entero (por ejemplo, 58) y responde todos los múltiplos de 7 que haya entre el número 1 y ese número (incluido)
num2 = int(input("Ingrese un numero entero: "))
print("Los múltiplos de 7 hasta ese número son: ")
for i in range(1, num2+1):
   if i % 7 == 0:
      print(i)