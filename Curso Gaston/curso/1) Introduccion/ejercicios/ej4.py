#listas por comprension

pares = []
for i in range(100):
    if i % 2 == 0:
        pares.append(i)
print(pares)

pares = [i for i in range(100) if i % 2 == 0]
print(pares)