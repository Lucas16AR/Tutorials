print("Ingresara dos numeros que deben ser enteros")
dividiendo = int(input("Dividiendo: "))
divisor = int(input("Divisor: "))
while divisor == 0:
   divisor = int(input("Divisor (no 0): "))
print("El resultado es", dividiendo/divisor)

suma = 0
num1 = float(input("Ingrese un numero: "))
while num1 != 0:
   suma = suma + num1
   num1 = float(input("Ingrese otro numero: "))
print("La suma es", suma)


#Ejercicios
#6.1. Crea un programa que pida al usuario que introduzca la suma de 135 y 768. Deberá repetirse hasta que introduzca el resultado correcto
suma = int(input("Cuanto es 135+768: "))
while suma != 903:
   suma = int(input("No! Debera ingresar de vuelta: "))
print("Numero es el correcto")


#6.2. Pide un código y una contraseña al usuario. No se le dejará proseguir hasta que el código sea 1234 y la clave sea 5000
codigo = input("Ingrese un codigo de ingreso: ")
contra = input("Ingrese una contraseña de acceso: ")
while not (codigo == "1234" and contra == "5000"):
   print("Acceso incorrecto");
   codigo = input("Ingrese un codigo de ingreso: ")
   contra = input("Ingrese una contraseña de acceso: ")
print("Acceso correcto")