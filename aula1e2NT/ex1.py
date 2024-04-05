def operacoes_com_numeros():
    a = int(input("Insira o primeiro número inteiro: "))
    b = int(input("Insira o segundo número inteiro: "))

    soma = a + b
    produto = a * b
    diferenca = abs(a - b)
    divisao = a / b if b != 0 else "Divisão por zero não é permitida"

    print("Soma:", soma)
    print("Produto:", produto)
    print("Diferença:", diferenca)
    print("Divisão:", divisao)

operacoes_com_numeros()
