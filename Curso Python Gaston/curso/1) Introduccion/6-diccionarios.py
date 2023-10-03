#variable = {"clave": "valor",}

ingles = {"hello": "hola", "day": "dia"}
print(ingles)

print(ingles["day"]) #muestra el valor de la clave(key)

ingles["hello"] = "salut" #cambia el valor de la clave
print(ingles)
print(ingles["hello"])

ingles["night"] = "noche" #agrega una nueva llave con su valor al diccionario
print(ingles)

del(ingles["night"]) #borra una clave con su valor
print(ingles)

for palabra in ingles: #muestra las claves
    print(palabra)

for clave in ingles: #muestra los valores
    print(ingles[clave])

for clave in ingles: #muestra claves y valores
    print(f"{clave} : {ingles[clave]}")

for clave, valor in ingles.items(): #muestra claves y valores
    print(clave, valor)

producto = {
    "id": 2,
    "nombre": "heladera",
    "precio": 2000,
    "stock": 20
}
print(producto)