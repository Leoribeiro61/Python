L1 = [1, 2, 6, 8]
L2 = [3, 6, 8, 9]

conjunto_1 = set(L1)
conjunto_2 = set(L2)

print("Valores comuns às duas listas:", conjunto_1 & conjunto_2)

print("Valores que só existem na primeira:", conjunto_1 - conjunto_2)

print("Valores que só existem na segunda:", conjunto_2 - conjunto_1)

print("Elementos não repetidos nas duas listas:", conjunto_1 ^ conjunto_2)

print("Primeira lista, sem os elementos repetidos na segunda:", conjunto_1 - conjunto_2)
