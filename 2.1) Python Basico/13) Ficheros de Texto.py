#Ficheros: 3 pasos
#Abrir fichero
#Leer o escribir
#Cerrar fichero

#Modos habituales:
# W = escritura (write)
# R = lectura (read)
# A = añadir (append)

fichero = open("ej1.txt", "w")
fichero.write("1\n2\n")
fichero.write("3")
fichero.write("4\n")
fichero.write("5\n")
fichero.write("6")
fichero.write("7")
fichero.close()

fichero = open("ej2.txt", "w")
for i in range(1, 11):
   fichero.write("linea "+ str(i) + "\n")
fichero.close()

fichero = open("ej2.txt", "r")
lineas = fichero.readlines()
fichero.close()
print(lineas)

fichero = open("ej3.txt", "w")
lineas = ["Uno\n", "Dos\n", "Tres\n"]
fichero.writelines(lineas)
fichero.close()

fichero = open("ej3.txt", "a")
lineas = ["Cuatro\n", "Cinco\n", "Seis\n"]
fichero.writelines(lineas)
fichero.close()


#Ejercicios
#12.1. Pide al usuario 3 frases y guárdalas en un fichero "frases.txt"
lineas = []
for i in range (0, 3):
   frase = input("Escriba una frase: ")
   lineas.append(frase + "\n")

fichero = open("ej4.txt", "w")
fichero.writelines(lineas)
fichero.close

#12.2. Añade una cuarta frase al fichero anterior
fichero = open("ej4.txt", "w")
fichero.write(input("Escribe otra frase mas: ") + "\n")
fichero.close

#12.3. Muestra el contenido de "frases.txt", precediendo cada línea con un número correlativo
fichero = open("ej4.txt", "r")
lineas = fichero.readlines()
fichero.close()
 
for i in range(0, len(lineas) ):
    print(str(i+1), ":", lineas[i].rstrip())