datos = [5, 6, 7, 8, 9]
datos.append(15)
datos.append(20)

print("Datos entre 0 y 2")
print(datos[0])
print(datos[2])

print("Todos los datos")
for i in range (0, len(datos)):
   print(datos[i])

print("Todos los datos al reves")
for i in range (5, -1, -1):
   print(datos[i])

datos = []
datos.append(3)
datos[0] = 2
print(len(datos))
print(datos[0])

for i in range (0, 6):
   datos.append(int(input("Introduzca un numero: ")))

for i in range (5, -1, -1):
   print(datos[i])


#Ejercicios
#8.1. Crea un array con los números 10, 20, 30, 40, 50 y luego muestra los que hay en las posiciones impares (primero, tercero y quinto: 10, 30 y 50)
datos = [10, 20, 30, 40, 50]
print("Datos impares")
print(datos[0])
print(datos[2])
print(datos[4])

#8.2. Pide al usuario 10 números y luego muestra los que son pares
datos = []
for i in range (1, 11):
   dato = int(input("Introduzca un numero: "))
   datos.append(dato)
print("Los numeros pares son")
for p in datos:
   if p % 2 == 0:
      print(p)