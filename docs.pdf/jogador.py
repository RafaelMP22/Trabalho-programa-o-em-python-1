
def obter_jogada_valida(tabuleiro):
    """
    Função que recebe e faz o tratamento de erro da jogada do jogador.
    """

    letras = ["A","B","C","D","E","F","G","H","I","J"]
   
    while True:
        colunas_letras = {
            "A" : 0,
            "B" : 1,
            "C" : 2,
            "D" : 3,
            "E" : 4,
            "F" : 5,
            "G" : 6,
            "H" : 7,
            "I" : 8,
            "J" : 9,
        }

        jogada = input("Informe qual posição deseja atacar (Ex: A1, J10, etc): ").upper().strip()
        if len(jogada) > 3 or len(jogada) < 2:
            print("Jogada inválida. Tente novamente.")
            pass
        else:
            if jogada[0] not in letras:
                print("Jogada inválida. Tente novamente.")
                continue
            if not jogada[1:].isnumeric():
                print("Jogada inválida. Tente novamente.")
                continue

            else:
                coluna = jogada[0]
                linha = int(jogada[1:])
                if linha < 1 or linha > 10:
                    print("Jogada inválida. Tente novamente.")
                    continue
                linha -= 1
                coluna = colunas_letras[coluna]

                if tabuleiro[linha][coluna] == "O" or tabuleiro[linha][coluna] == "X":
                    print("ERRO: Você já atirou nesta posição! Tente outra coordenada.")
                    continue
                
                return linha, coluna
                    

