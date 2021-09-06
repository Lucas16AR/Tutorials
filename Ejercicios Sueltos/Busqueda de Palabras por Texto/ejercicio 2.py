archivo = "D:/Ejercicios Python/Busqueda de Palabras por Texto/Ejercicio 2.txt"
palabraBuscar = "Guido"
repetidas = 0

file = open(archivo)
lines = file.readlines()

for line in lines:
    palabras = line.split(' ')
    for palabra in palabras:
        if(palabra==palabraBuscar):
            repetidas = repetidas + 1

print('La palabra {} tiene {} repeticiones en el archivo {}'.format(palabraBuscar,repetidas,archivo))
