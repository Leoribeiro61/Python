# Dada a lista
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

# a. 
maior_elemento = max(lista)
print(f"O maior elemento da lista é: {maior_elemento}")

# b. 
menor_elemento = min(lista)
print(f"O menor elemento da lista é: {menor_elemento}")

# c. 
numeros_pares = [num for num in lista if num % 2 == 0]
print(f"Números pares na lista: {numeros_pares}")

# d. 
primeiro_elemento = lista[0]
ocorrencias_primeiro = lista.count(primeiro_elemento)
print(f"O primeiro elemento ({primeiro_elemento}) aparece {ocorrencias_primeiro} vezes na lista")

# e. 
media_elementos = sum(lista) / len(lista)
print(f"A média dos elementos da lista é: {media_elementos:.2f}")

# f.
soma_negativos = sum(num for num in lista if num < 0)
print(f"A soma dos elementos de valor negativo é: {soma_negativos}")
