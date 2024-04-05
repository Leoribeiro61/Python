def fibonacci_iterativo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

try:
    n = int(input("Digite um número inteiro maior ou igual a 3: "))
    if n < 3:
        print("Por favor, insira um número maior ou igual a 3.")
    else:
        resultado = fibonacci_iterativo(n)
        print(f"O {n}º termo da série de Fibonacci é {resultado}")
except ValueError:
    print("Por favor, insira um número válido.")

