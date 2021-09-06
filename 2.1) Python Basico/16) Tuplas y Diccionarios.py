#Tuplas: son inmutables, no se pueden cambiar y son mas rapidas para procesar

datos = (5, 6, 7, 8, 9)
#datos.append(15)
#datos.append(20)

print("Datos entre 0 y 2")
print(datos[0])
print(datos[2])

print("Todos los datos")
for i in range (0, len(datos)):
   print(datos[i])

print("Todos los datos al reves")
for i in range (4, -1, -1):
   print(datos[i])

#Diccionario: son datos a los que se accede, no por posición, sino por clave
libro1 = {
   "autor": "Stephen King",
   "titulo": "It",
   "paginas": 1100   
}

print(libro1)
print(libro1["autor"])


#Ejercicios
#15.1. Pide al usuario un número entero del 1 al 7 y escribe el nombre del día de la semana correspondiente (1=lunes, 7=domingo), usando una tupla
# Ejemplo de tuplas
# Versión simple
 
nombresDias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo")
numeroDia = int(input("Dime el número de día (1 al 7): "))
print("Su nombre es", nombresDias[ numeroDia-1 ] )

#15.2. Pide al usuario un número entero del 1 al 12 y escribe el nombre del mes correspondiente (1=enero, 12=diciembre), usando una tupla
# Ejemplo de tuplas
# Versión con control de errores, con "try"
 
try:
    nombresMeses = ("enero", "febrero", "marzo", "abril",
        "mayo", "junio", "julio", "agosto",
        "septiembre", "octubre", "noviembre", "diciembre")
    numeroMes = int(input("Dime el número de mes (1 al 12): "))
    print("Su nombre es", nombresMeses[ numeroMes-1 ] )
 
except:
    print("Número de mes incorrecto")

#15.3. Pide al usuario el nombre de un mes y responde cuántos días tiene (suponiendo un año no bisiesto), usando un diccionario
dias = {
    "enero": 31,
    "febrero": 28, 
    "marzo": 31, 
    "abril": 30,
    "mayo": 31, 
    "junio": 30, 
    "julio": 31, 
    "agosto": 31,
    "septiembre" : 30, 
    "octubre": 31, 
    "noviembre": 30, 
    "diciembre": 31
}
nombreMes = input("Dime el nombre del mes: ")
print("Tiene", dias[nombreMes], "dias" )