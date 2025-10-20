# Jogo da Velha em Python usando matriz

def criar_tabuleiro():
    # Cria uma matriz 3x3 com espaços vazios
    return [[" " for _ in range(3)] for _ in range(3)]

def exibir_tabuleiro(tab):
    print("\n  0   1   2")
    for i, linha in enumerate(tab):
        print(i, " | ".join(linha))
        if i < 2:
            print("  ---------")

def verificar_vitoria(tab, jogador):
    # Verifica linhas
    for linha in tab:
        if all(cel == jogador for cel in linha):
            return True
    # Verifica colunas
    for c in range(3):
        if all(tab[l][c] == jogador for l in range(3)):
            return True
    # Verifica diagonais
    if all(tab[i][i] == jogador for i in range(3)):
        return True
    if all(tab[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def verificar_empate(tab):
    return all(cel != " " for linha in tab for cel in linha)

def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        try:
            linha = int(input("Escolha a linha (0-2): "))
            coluna = int(input("Escolha a coluna (0-2): "))
        except ValueError:
            print("Entrada inválida! Use números de 0 a 2.")
            continue

        if (0 <= linha <= 2) and (0 <= coluna <= 2):
            if tabuleiro[linha][coluna] == " ":
                tabuleiro[linha][coluna] = jogador_atual
                # Verifica vitória
                if verificar_vitoria(tabuleiro, jogador_atual):
                    exibir_tabuleiro(tabuleiro)
                    print(f"Parabéns! Jogador {jogador_atual} venceu!")
                    break
                # Verifica empate
                if verificar_empate(tabuleiro):
                    exibir_tabuleiro(tabuleiro)
                    print("Empate!")
                    break
                # Troca de jogador
                jogador_atual = "O" if jogador_atual == "X" else "X"
            else:
                print("Posição já ocupada. Tente novamente.")
        else:
            print("Posição inválida! Use números entre 0 e 2.")

if __name__ == "__main__":
    jogo_da_velha()
