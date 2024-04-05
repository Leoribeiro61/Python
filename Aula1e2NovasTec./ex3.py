def par_ou_impar():
    numero = int(input("Insira um número inteiro: "))
    if numero % 2 == 0:
        print("O número", numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")

par_ou_impar()