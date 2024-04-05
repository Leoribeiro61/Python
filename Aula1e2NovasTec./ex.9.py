def tabuada():
    while True:
        print("\nMenu:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Divisão")
        print("4. Multiplicação")
        print("5. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 5:
            break
        
        a = int(input("Insira um número: "))
        b = int(input("Insira outro número: "))
        
        if opcao == 1:
            print("Resultado da adição:", a + b)
        elif opcao == 2:
            print("Resultado da subtração:", a - b)
        elif opcao == 3:
            print("Resultado da divisão:", a / b if b != 0 else "Divisão por zero não é permitida")
        elif opcao == 4:
            print("Resultado da multiplicação:", a * b)

tabuada()