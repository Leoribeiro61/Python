def verificar_primo(numero):
    if numero <= 1:
        return False  

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  

    return True  
numero_usuario = int(input("Insira um número inteiro positivo: "))

if verificar_primo(numero_usuario):
    print(f"{numero_usuario} é um número primo.")
else:
    print(f"{numero_usuario} não é um número primo.")
