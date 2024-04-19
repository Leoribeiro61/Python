L1 = [1, 2, 6, 8]
L2 = [3, 6, 8, 9]

conjunto_1 = set(L1)
conjunto_2 = set(L2)

elementos_nao_repetidos = list(conjunto_1 ^ conjunto_2)
print(f"Elementos não repetidos nas duas listas: {elementos_nao_repetidos}")
