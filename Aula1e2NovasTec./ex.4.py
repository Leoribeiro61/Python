def separar_digitos(numero):
    numero_str = str(numero)

    for digito in numero_str:
        print(digito, end="   ")

numero_usuario = int(input("Insira um número de cinco dígitos: "))

if 10000 <= numero_usuario < 100000:
    print("Dígitos separados por três espaços:")
    separar_digitos(numero_usuario)
else:
    print("Por favor, insira um número de cinco dígitos.")

