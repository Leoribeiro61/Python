def calcular_quadrado_soma_impares(n):
    soma_impares = 0
    impar = 1

    for _ in range(n):
        soma_impares += impar
        impar += 2

    return soma_impares ** 2

try:
    n = int(input("Digite um número natural: "))
    if n < 0:
        print("Por favor, insira um número não negativo.")
    else:
        resultado = calcular_quadrado_soma_impares(n)
        print(f"O quadrado de {n} usando a soma de ímpares é {resultado}")
except ValueError:
    print("Por favor, insira um número válido.")
