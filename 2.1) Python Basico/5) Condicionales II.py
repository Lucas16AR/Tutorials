dia = int(input("Introduzca el dia de la semana del 1 al 7: "))

if dia == 1:
   print("Lunes")
elif dia == 2:
   print("Martes")
elif dia == 3:
   print("Miercoles")
elif dia == 4:
   print("Jueves")
elif dia == 5:
   print("Viernes")
elif dia == 6:
   print("Sabado")
elif dia == 7:
   print("Domingo")
else:
   print("No ha elegido el numero correcto")


#Ejercicios
#5.1. Pide un número real y responde si es positivo, negativo o cero, empleando elif
num1 = float(input("Introduzca un numero real: "))

if num1 > 0:
   print("El numero es positivo")
elif num1 < 0:
   print("El numero es negativo")
else:
   print("El numero el 0")


#5.2. Pide al usuario un numero entero del 1 al 12 y escribe el nombre del mes correspondiente (1=enero, 12=diciembre)
num2 = int(input("Introduzca un numero entero del 1 al 12: "))
if num2 == 1:
   print("Enero")
elif num2 == 2:
   print("Febrero")
elif num2 == 3:
   print("Marzo")
elif num2 == 4:
   print("Abril")
elif num2 == 5:
   print("Mayo")
elif num2 == 6:
   print("Junio")
elif num2 == 7:
   print("Julio")
elif num2 == 8:
   print("Agosto")
elif num2 == 9:
   print("Septiembre")
elif num2 == 10:
   print("Octubre")
elif num2 == 11:
   print("Noviembre")
elif num2 == 12:
   print("Diciembre")      
else:
   print("El numero elegido no representa ningun mes")