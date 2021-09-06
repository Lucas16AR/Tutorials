print("Hola Mundo 1")
print("Hola Mundo 2")
print("Hola Mundo 3")

#Soy un comentario

"""
Texto que no se a interpretara
Texto que no se a interpretara
Texto que no se a interpretara
"""

#Variables
texto = "Repaso con Victor de Python"
nombre = "Lucas Galdame"
altura = "17 cm"
year = 2021

print(f"{texto} - {nombre} - {altura} - {year}") #Concatenación con f
print(texto + " - " + nombre + " - " + altura + " - " + str(year)) #Concatenación con +

#Entrada
sitioweb = input("Cual es tu pagina web?: ")
print("El sitio web es: " + sitioweb)

#Condiciones
altura = int(input("Cual es tu altura?: "))

if altura >= 180:
   print("Eres alto")
else:
   print("Eres bajo")

#Funciones
var_altura = int(input("Cual es tu altura?: "))

def mostraraltura(altura):
   resultado = ""

   if altura >= 180:
      resultado = "Eres alto"
   else:
      resultado = "Eres bajo"
   return resultado #nos permite extraer informacion de una funcion para luego mostrarla y asi tener dentro de la funcion la logica

print(mostraraltura(var_altura))

#Listas: permite guardar una serie de variables dentro de una misma
personas = ["Lucas", "Delfina", "Lucila"]
print(personas[2])

for persona in personas:
   print("-" + persona)
#For vendria siendo un bucle, que repeti una serie de instrucciones hasta que se cumplan las condiciones