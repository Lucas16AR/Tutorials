#tuplas son inmutables, no se pueden modificar
#Las tuplas deben contener multiples elementos, pero si queremos definir un elemento o un conjunto de elementos
#se puede poner como x = (1,), con una coma que especifica que hay un conjunto de elementos multiples  

x = (1, 2, 3)
#print(type(x)) #veo si es de tipo tupla

y = tuple((1, 2, 3))
#print(y) #muestra la tupla

z = ('a', 'b', 'c', 'd', 'e')
print(z[0]) #muestra el elemento de esa posicion