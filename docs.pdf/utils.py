import os

def limpar_tela():
    """
    Limpa o terminal de execução para manter a interface do jogo limpa.
    Funciona tanto em Windows ('nt') quanto em Linux/Mac ('posix').
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def aguardar_enter(mensagem="\nPressione [ENTER] para continuar..."):
    """
    Função para receber um "enter" (Quando queremos que o usuário confirme que quer passar de algo)
    """
    while True:
        entrada = input(mensagem)
        if entrada == "":
            break 
        else:
            print("[ERRO] Entrada inválida. Por favor, prima apenas a tecla [ENTER].")
