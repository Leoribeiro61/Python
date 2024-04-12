def verifica_parenteses(expressao):
    pilha = []

    for caractere in expressao:
        if caractere == "(":
            pilha.append(caractere) 
        elif caractere == ")":
            if not pilha:
                return False  
            pilha.pop()  
    return len(pilha) == 0

expressao_usuario = input("Digite uma expressão com parênteses: ")

if verifica_parenteses(expressao_usuario):
    print("Os parênteses estão corretos!")
else:
    print("Os parênteses estão incorretos!")

