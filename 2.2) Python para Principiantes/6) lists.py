demo_list = [1, 'hello', 3.14, True, [1, 2, 3, 4]]
colors = ['red', 'yellow', 'blue']

numbers_list = list((1, 2, 3, 4))
print(type(numbers_list))

r = list(range(1, 51))
print(r)
print(len(demo_list)) #imprime la longitud de la lista
print(colors[-2]) #saber que elemento esta en esa posicion
print('blue' in colors) #imprime si un elemento esta en esa lista o no

colors[1] = 'green' #cambio el elemento de esa lista
print(colors)

colors.append('violet') #agrega un elemento a la lista
colors.append(('white', 'yellow')) #agrega dos elementos a la lista, pero lo hace en forma de tupla, ya que de uno no se puede
print(colors)

colors.extend(['white', 'black']) #agrega los elementos a la lista, pero sin el parentesis
print(colors)

colors.insert(1, 'light blue') #agrega un elemento en una posicion de la lista
print(colors)

colors.pop() #remueve el ultimo elemento o el de una posicion determinada
print(colors)

colors.remove('blue') #remueve un elemento
print(colors)

colors.clear() #deja la lista vacia
print(colors)

colors.sort() #ordena los elementos
print(colors)
colors.sort(reverse = True) #ordena los elementos al reves
print(colors)

print(colors.index('blue')) #nos indica el indice de un elemento

print(colors.count('blue')) #nos indica cuantas veces hay un elemento