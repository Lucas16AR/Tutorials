tabla_a_calcular = int(input("Ingrese la tabla que desea a calcular: "))

num = 1
for i in range(10):
    print(f"{tabla_a_calcular} x {num} = {tabla_a_calcular * num}")
    num = num + 1


tabla_a_calcular = int(input("Ingrese la tabla que desea a calcular: "))
hasta_donde = int(input(f"Hasta que numero desea calcular la tabla de {tabla_a_calcular}: "))
for i in range(hasta_donde):
    print(f"{tabla_a_calcular} x {i+1} = {tabla_a_calcular * (i+1)}")


while tabla_a_calcular > 10:
    print("Hola")
    tabla_a_calcular = tabla_a_calcular - 1