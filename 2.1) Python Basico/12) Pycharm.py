#11.1. Usando IDLE o PyCharm, crea un programa que te pregunte un número y
#escriba la palabra "Hola" tantas veces como indique ese número.
cantidad = int(input("¿Cuántas veces quieres que te salude? "))
for i in range(0, cantidad):
    print("Hola")


#11.2. Usando IDLE o PyCharm, crea un programa que te pida un número y te responda
#si es primo (sólo divisible entre 1 y entre él mismo) o no lo es.
numero = int(input("Dime el número que quieras ver si es primo: "))
divisores = 0
for i in range(1, numero+1):
    if numero % i == 0:
        divisores += 1
 
if divisores == 2:
    print("Es primo")
else:
    print("No es primo")