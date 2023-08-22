def hello(name):
    print("Hello " + name)

hello("Delfina")
hello("Lucila")
hello("Yamila")

###################################################################

def add(n1, n2):
    return n1 + n2

print(add(10, 20))
print(add(203, 432))

print(len("hello"))

###################################################################

#lambda sirve como una funcion, pero no tiene nombre
add = lambda n3, n4: n3 + n4

print(add(60, 100))