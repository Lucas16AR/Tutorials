name1 = 'Lucas'
frase1 = 'Lucas dijo hola'
frase2 = 'Universidad de Mendoza'

name2 = str(input("Dime como te llamas: "))
inicial = name2[0]
tercera = name2[2]
longitud = len(name2)
print(longitud)
print(name2.upper())
print(name2.lower())
print(inicial)
print(name2[0:3])
print(name2[-1])
print(name2[::-1])
print(name2[3:1:-1])

frase3 = 'Hola,'
frase4 = ' ¿que tal?'
frase5 = frase3 + frase4
print(frase5)


#Ejercicio
#9.1. Pregunta su nombre al usuario y responde:
#Su inicial
#La cantidad de letras
#La última letra
#Su nombre en mayúsculas
#Su nombre al revés
#La cantidad de vocales que contiene

nombre = str(input("Dime como te llamas: "))
print("La inicial es", nombre[0])
print("La longitud es de", len(nombre), "letras")
print("La ultima letra es", nombre[-1])
print("En mayuscula es", nombre.upper())
print("El nombre al reves es", nombre[::-1])

CantidadDeVocales = 0
for letra in nombre.upper():
   if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
      CantidadDeVocales += 1
 
print("La cantidad de vocales es de", CantidadDeVocales)