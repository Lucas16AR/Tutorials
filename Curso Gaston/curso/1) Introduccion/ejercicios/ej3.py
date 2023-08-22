#Funciones

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2

def multiplicar(num1, num2):
    return num1 * num2

#resultado = sumar(1,2)
#print(resultado)

def calculadora():
    menu = int(input("""
[1] Suma
[2] Resta
[3] Division
[4] Multiplicacion
[5] Salir
>>> """))
    if menu == 1:
        num1 = int(input("Ingrese un numero para sumar: "))
        num2 = int(input("Ingrese otro numero para sumar: "))
        resultado = sumar(num1, num2)
        print(f"El resultado es {resultado}")
    elif menu == 2:
        num1 = int(input("Ingrese un numero para restar: "))
        num2 = int(input("Ingrese otro numero para restar: "))
        resultado = restar(num1, num2)
        print(f"El resultado es {resultado}")
    elif menu == 3:
        num1 = int(input("Ingrese un numero para dividir: "))
        num2 = int(input("Ingrese otro numero para dividir: "))
        resultado = dividir(num1, num2)
        print(f"El resultado es {resultado}")
    elif menu == 4:
        num1 = int(input("Ingrese un numero para multiplicar: "))
        num2 = int(input("Ingrese otro numero para multiplicar: "))
        resultado = multiplicar(num1, num2)
        print(f"El resultado es {resultado}")
    elif menu == 5:
        print("Ha salido del programa")
        exit()    
    else:
        print("Opcion invalida")

while True:
    calculadora()