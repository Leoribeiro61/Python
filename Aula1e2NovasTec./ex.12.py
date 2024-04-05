def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

try:
    n = int(input("Digite um número inteiro positivo: "))
    if n <= 0:
        print("Por favor, digite um número positivo maior que zero.")
    else:
        print(f"Os {n} primeiros números primos são:")
        print_first_n_primes(n)
except ValueError:
    print("Entrada inválida. Digite um número inteiro positivo.")
