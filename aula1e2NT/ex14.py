numero = int(input("Digite um número inteiro não negativo: "))
resultado = 1

for count in range(1, numero + 1):
    resultado *= count

print(f"O fatorial de {numero} é {resultado}")
