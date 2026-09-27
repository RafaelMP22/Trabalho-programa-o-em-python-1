import os

def limpar_replay():
    """
    Função que apaga o replay da partida anterior para salvar o atual.
    """
    if not os.path.exists("data"):
        os.makedirs("data")
        
    with open("data/replay.txt", "w") as arquivo:
        pass # Apenas abre em 'w' e fecha


def registrar_jogada(jogador, linha, coluna, resultado):
    """
    Função que registra as informações da partida.
    """
    if not os.path.exists("data"):
        os.makedirs("data")
        
    with open("data/replay.txt", "a") as arquivo:
        arquivo.write(f"{jogador};{linha};{coluna};{resultado}\n")


def exibir_replay():
    """
    Função que irá receber os dados da partida e printar de maneira formatada
    """
    letras = "ABCDEFGHIJ"

    try:
        with open("data/replay.txt", "r") as arquivo:
            dados_lidos = arquivo.readlines()
            
            total = len(dados_lidos)
            if total == 0:
                print("\nA última partida não teve jogadas registradas.")
                return

            print("\n=== REPRODUZINDO REPLAY ===")
            
            for indice, linha_texto in enumerate(dados_lidos):
                dados = linha_texto.strip().split(';')
                
                jogador = dados[0]
                linha_bruta = int(dados[1])
                coluna_bruta = int(dados[2])
                resultado = dados[3]
                
                numero_jogada = indice + 1
                
                if jogador == "SISTEMA":
                    print(f"\n*** FIM DA PARTIDA - {resultado} ***")
                
                else:
                    linha_tela = linha_bruta + 1 
                    coluna_tela = letras[coluna_bruta] 
                    coordenada = f"{coluna_tela}{linha_tela}"
                    
                    print(f"Jogada {numero_jogada:02d}/{(total - 1):02d} - {jogador} - {coordenada} - {resultado}")
                
                # Interatividade para avançar ou sair
                if numero_jogada < total:
                    while True:
                        comando = input("[ENTER] Proxima jogada [Q] Sair do replay: ").upper().strip()
                        if comando == "" or comando == "Q":
                            break 
                        else:
                            print("[ERRO] Comando inválido. Pressione apenas ENTER ou a letra Q.")
                    
                    if comando == "Q":
                        print("Saindo do replay...")
                        break 
                        
            print("=== FIM DO REPLAY ===\n")
            
    except FileNotFoundError:
        print("\n[ERRO] Nenhuma partida jogada. Impossível exibir replay.\n")
