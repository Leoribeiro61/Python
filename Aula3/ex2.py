
palavra_secreta = input("Digite a palavra secreta: ").strip().lower()

letras_acertadas = ["_" for letra in palavra_secreta]

chances = 7

forca = [
    "  +---+",
    "  |   |",
    "      |",
    "      |",
    "      |",
    "      |",
    "========="
]


while True:
    for linha in forca[:7 - chances]:
        print(linha)

    print(" ".join(letras_acertadas))

    chute = input("Qual letra? ").strip().lower()

    if chute in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if chute == letra:
                letras_acertadas[i] = chute
    else:
        chances -= 1
        print(f"Errou! Você tem {chances} chances restantes.")

    if "_" not in letras_acertadas:
        print(f"Parabéns, você ganhou! A palavra era: {palavra_secreta}")
        break
    elif chances == 0:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")
        break
