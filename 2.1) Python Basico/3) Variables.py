#Variables: información cambiante, tipicamente introducida por el usuario o que sea el resultado de cálculos anteriores

nombre = input("Hola, introduzca tu nombre: ")
print("Tu nombre es", nombre)

num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa otro numero entero: "))
num3 = num1 + num2
print("La suma de estos numeros es", num3)

#Ejercicios
#3.1. Pregunta al usuario su nombre y su apellido y escribe "Hola, Sr." seguido de su apellido y luego de su nombre (por ejemplo, "Hola, Sr. Cabanes, Nacho").
name = input("Escriba su nombre: ")
surname = input("Escriba su apellido: ")
print("Hola, Sr/a.", name, surname)

#3.2. Pide dos números al usuario y muestra su producto.
num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))
print("El resultado es ", num1 * num2)

#3.3. Pide al usuario tres números y escribe el resultado de (a+b)*c y a*c+b*c.
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero entero: "))
c = int(input("Ingrese otro numero entero: "))
print("El resultado 1 es ", (a+b)*c)
print("El resultado 2 es ", a*c+b*c)