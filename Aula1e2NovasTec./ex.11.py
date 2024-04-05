import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for divisor in range(3, int(math.sqrt(n)) + 1, 2):
        if n % divisor == 0:
            return False

    return True

numero = int(input("Digite um número: "))

if is_prime(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
