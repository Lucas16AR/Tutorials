def saludar():
    print("Hola que tal")

def saludar_persona(persona = "Alejandro"):
    print(f"Hola que tal {persona}")

saludar()
saludar_persona("Lucas")

def saludo():
    print("Bienvenido")

saludo()

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2

def multiplicar(num1, num2):
    return num1 * num2

resultado = sumar(1,2)
print(resultado)

resultado = restar(10,7)
print(resultado)

resultado = dividir(16,4)
print(resultado)

resultado = multiplicar(5,5)
print(resultado)