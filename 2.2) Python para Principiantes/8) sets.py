#set se utiliza mas para cuando tenemos un conjunto de datos sin organizar

colors = {"red", "blue", "green"}

print(type(colors))

print("red" in colors)
print("white" in colors)

colors.add("violet")
colors.remove("red")
print(colors)

colors.clear()
print(colors)

del colors #borra todo
print(colors)