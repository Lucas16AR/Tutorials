nombre = "Santi"
edad = 21
persona_masculina = True
persona_femenina = False

if nombre == "Lucas":
    print("Verdadero")
elif nombre == "Gaston":
    print("Bienvenido Gaston")
else:
    print("Falso")
    if nombre == "Santi":
        print("Hola Santi")

if edad >= 21:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#and
if persona_masculina == True and persona_femenina == False:
    print("Una de las dos condiciones se cumple")
    print("Se cumplen las dos condiciones")
else:
    print("No se cumplen las condiciones")