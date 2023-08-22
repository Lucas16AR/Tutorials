try:
   fichero = open ("ej1.txt", "r")
   
except:
   print("No se ha podido encontrar el archivo")

else:
   lineas = fichero.readlines()
   fichero.close()
   print(lineas)

print("Endgame")


#Ejercicio
#13.1. Pide al usuario el nombre de un fichero. Si el fichero existe, muestra su contenido (pero no como lista, sino las líneas una a una) y si no existe, escribe un mensaje de error adecuado

try:
    frase = input("Escribe el nombre del fichero: ")
    fichero = open(frase, "r")
 
except:
    print("No se pudo acceder al fichero")
 
else:
    lineas = fichero.readlines()
    fichero.close()
 
    for i in range(0, len(lineas) ):
        print( lineas[i].rstrip() )