def inicializa_tabuleiro():
    """Inicializa o tabuleiro vazio."""
    return [[0, 0, 0] for _ in range(3)]

def exibe_tabuleiro(tabuleiro):
    """Exibe o tabuleiro na tela."""
    for linha in tabuleiro:
        print(" ".join(str(valor) if valor != 0 else "_" for valor in linha))
    print()

def verifica_vitoria(tabuleiro, jogador):
    """Verifica se o jogador venceu a partida."""
    for linha in tabuleiro:
        if all(valor == jogador for valor in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def main():
    tabuleiro = inicializa_tabuleiro()
    jogadores = ["X", "O"]
    jogador_atual = 0
    jogadas = 0

    while True:
        exibe_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogadores[jogador_atual]}, escolha a linha (1 a 3): ")) - 1
        coluna = int(input(f"Escolha a coluna (1 a 3): ")) - 1

        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = jogadores[jogador_atual]
            jogadas += 1
            if verifica_vitoria(tabuleiro, jogadores[jogador_atual]):
                exibe_tabuleiro(tabuleiro)
                print(f"Jogador {jogadores[jogador_atual]} venceu!")
                break
            elif jogadas == 9:
                exibe_tabuleiro(tabuleiro)
                print("Empate!")
                break
            jogador_atual = 1 - jogador_atual
        else:
            print("Posição já ocupada. Escolha outra.")

if __name__ == "__main__":
    main()
