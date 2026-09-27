def criar_tabuleiro():
    '''
    Essa função gera uma matriz 10x10, com os mesmos caracteres que representam espaços sem
    navios
    '''
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append("-")
        tabuleiro.append(linha)

    return tabuleiro

tabuleiro = criar_tabuleiro()


def imprimir_tabuleiro(tabuleiro, ocultar=False):
    """
    Imprime o tabuleiro. Se ocultar=True, esconde os navios ('N').
    """
    print("   A B C D E F G H I J")
    for i in range(10):
        numero_linha = f"{i + 1:<2}"
        
        linha_tela = []
        for celula in tabuleiro[i]:
            if ocultar and celula == 'N':
                linha_tela.append('-')
            else:
                linha_tela.append(celula) 
                
        linha_formatada = " ".join(linha_tela)
        print(f"{numero_linha} {linha_formatada}")
    

