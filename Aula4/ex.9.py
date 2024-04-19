versao_inicial = [1, 2, 5, 6, 9]
versao_apos_alteracoes = [1, 2, 8, 10]

conjunto_inicial = set(versao_inicial)
conjunto_apos_alteracoes = set(versao_apos_alteracoes)

nao_mudaram = conjunto_inicial & conjunto_apos_alteracoes
print("Elementos que não mudaram:", nao_mudaram)

novos_elementos = conjunto_apos_alteracoes - conjunto_inicial
print("Novos elementos:", novos_elementos)

elementos_removidos = conjunto_inicial - conjunto_apos_alteracoes
print("Elementos que foram removidos:", elementos_removidos)
