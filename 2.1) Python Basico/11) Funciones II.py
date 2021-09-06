def max(num1, num2):
   if num1 > num2:
      return num1
   else:
      return num2

print("El maximo de 5 y 12")
print(max(5,12))

print("El maximo de 25 y 12")
print(max(25,12))

#Ejercicios
#10.1. Crea una función que reciba 3 números y devuelva su suma
def suma (n1, n2, n3):
   return n1 + n2 + n3

print("La suma de 10, 20 y 30 es", suma(10,20,30))


#10.2. Crea una función que reciba una cadena de texto y una letra, y devuelva la cantidad de veces que la letra aparece dentro de la cadena
def cant(texto, letra):
   cantidad = 0
   for l in texto:
      if l == letra:
         cantidad += 1
   return cantidad

print('Veces que "buenas noches" contiene una "a": ',
   cant("buenas noches", "a"))


#10.3. Crea un procedimiento que escriba una línea formada por 2 letras, repetidas varias veces. Por ejemplo, para "-", "=" y 3, escribiría "-=-=-="
def repetir(letra1, letra2, veces):
    for i in range(0, veces):
        print(letra1, end="")
        print(letra2, end="")
 
repetir("-", "=", 3)