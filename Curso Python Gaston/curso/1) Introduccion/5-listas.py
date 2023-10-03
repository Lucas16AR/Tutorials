nombres = ["Lucas", "Gaston", "Santiago", "Douglas", "Bruno"]
edades = [21, 22, 22, 21, 20]
numeros = [19, 23]
apellidos = [
    ["Galdame", "Villegas"],
    ["Fenske", "Moyano"],
    ["Arenas", "Romero"]
]

print(nombres)

nombres.append("Daniel") #agregar
print(nombres)

nombres.pop() #quitar
print(nombres)

nombres.remove("Bruno") #elimina un elemento especifico
print(nombres)

cantidad_elementos = len(nombres) #longitud
print(cantidad_elementos)

print(nombres[0]) #indice
print(nombres[-1]) #indice
print(nombres[0:3]) #indice

print(apellidos) #imprime lista
print(apellidos[0]) #imprime elemento especifico
print(apellidos[0][1]) #imprime un elemento mas especifico

print(max(edades)) #elemento mas grande
print(min(edades)) #elemento mas chico
print(sorted(edades)) #elementos ordenados

edades.reverse() #elemento dados vuelta
print(edades)

edades.extend(numeros) #agrega una lista a otra lista
print(edades)

for N in nombres:
    print(N)