foods = ["bananas", "grapes", "apples", "oranges", "lemons"]

#print(dir(foods))

foods.append("cheese")
foods.append("milk")

for food in foods:
    #if food == "cheese":
    #    print("hay que comprar eso")
    #if food == "milk":
    #    break
    #if food == "apples":
    #    continue
    print(food)

#############################################################################

for number in range(1, 8):
    print(number)

for letter in "Hello":
    print(letter)

#############################################################################

count = 3

while count <= 10:
    print(count)
    count = count + 1