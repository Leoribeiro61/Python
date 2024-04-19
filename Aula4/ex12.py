pet1 = {
    'nome': 'Bolinha',
    'tipo': 'Cachorro',
    'dono': 'João'
}

pet2 = {
    'nome': 'Miau',
    'tipo': 'Gato',
    'dono': 'Maria'
}

pet3 = {
    'nome': 'Polly',
    'tipo': 'Papagaio',
    'dono': 'Carlos'
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"Nome do animal: {pet['nome']}")
    print(f"Tipo do animal: {pet['tipo']}")
    print(f"Dono do animal: {pet['dono']}\n")
