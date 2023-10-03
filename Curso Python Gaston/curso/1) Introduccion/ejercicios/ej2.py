name = str(input("Ingrese su nombre: "))
age = int(input("Ingrese su edad: "))

if age >= 18 and age <= 65:
    print("Acceso permitido")
else:
    print("Acceso denegado")

gender = str(input("Ingrese su sexo como M o F: "))

genderM = True
genderF = True

if gender == genderM:
    print("Bienvenido Caballero")
elif gender == genderF:
    print("Bienvenida Dama")

#hace la primer parte, pero no hace la parte del saludo

#mejor solucion

age2 = int(input("Ingrese su edad: "))
if age2 >= 18 and age2 <= 65:
    print("Acceso permitido")
else:
    print("Acceso denegado")
    exit()

masculino = False
gender2 = int(input("""
Ingrese su genero:
[1] Masculino
[2] Femenino
>>> """))
if gender2 == 1:
    masculino = True
elif gender2 == 2:
    masculino = False
else:
    print("Opcion no valida")
    exit()

if age2 >= 18 and age2 <= 65:
    if masculino:
        print("Bienvenido caballero")
        print(f"Su edad es de {age2} años")
    else:
        print("Bienvenida dama")
        print(f"Su edad es de {age2} años")
else:
    print("Acceso denegado")