# menu.py

def exibir_menu_principal():
    """
    Exibe o menu principal e retorna a opção escolhida pelo usuário.
    """
    while True:
        print("\n=== BATALHA NAVAL - GPTECH GAMES ===")
        print("1. Nova partida")
        print("2. Ver estatisticas")
        print("3. Assistir replay da ultima partida")
        print("4. Creditos")
        print("5. Sair")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao in ['1', '2', '3', '4', '5']:
            return opcao  
        else:
            print("\n[ERRO] Opção inválida! Por favor, escolha um número de 1 a 5.")

def selecionar_modo_jogo():
    """
    Exibe o menu de seleção de modo de jogo e retorna a opção escolhida.
    """
    while True:
        print("\nSelecione o modo de jogo:")
        print("[1] Jogador vs Computador")
        print("[2] Dois Jogadores")
        print("[0] Voltar ao menu")
        
        opcao = input("Escolha uma opcao: ")
        
        if opcao in ['0', '1', '2']:
            return opcao
        else:
            print("\n[ERRO] Opção inválida! Escolha 0, 1 ou 2.")

