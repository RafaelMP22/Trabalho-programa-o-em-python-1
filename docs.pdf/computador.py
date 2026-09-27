import random

def gerar_jogada_computador(tabuleiro):
    """
    Função que irá gerar uma jogada válida do computador.
    """
    
    while True:
        coluna = random.randint(0, 9)
        linha = random.randint(0, 9)
        if(tabuleiro[linha][coluna] == "-" or tabuleiro[linha][coluna] == "N"):
            return linha, coluna