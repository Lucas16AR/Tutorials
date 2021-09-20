tupla = ("lucas", 21, ["san rafael", "mendoza"])
print(tupla)
print(len(tupla)) #longitud de la lista

#para modificar la tupla, se debe convertir en una lista, 
#modificar esa lista, y convertirla en tupla de nuevo

tupla = list(tupla) #tupla a lista
tupla.append(200)
tupla = tuple(tupla) #lista a tupla
print(tupla)

set = {21, 24, 23, 14, 21, 21, 29} #no repite datos
print(set)