sandwich_orders = ["Atum", "Frango", "Vegetariano", "Queijo grelhado", "Pastrami"]

finished_sandwiches = []

for pedido in sandwich_orders:
    print(f"Preparei seu sanduíche de {pedido}.")
    finished_sandwiches.append(pedido)

print("\nSanduíches prontos:")
for sanduiche_pronto in finished_sandwiches:
    print(sanduiche_pronto)
