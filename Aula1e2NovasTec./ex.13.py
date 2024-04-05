def calcular_fatorial(n):
    if n < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    elif n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

try:
    numero = int(input("Digite um número inteiro não negativo: "))
    resultado = calcular_fatorial(numero)
    print(f"{numero}! = {resultado}")
except ValueError:
    print("Entrada inválida. Digite um número inteiro não negativo.")
