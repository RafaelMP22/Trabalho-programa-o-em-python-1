import time
import utils
import menu
import tabuleiro
import navios
import jogador
import computador
import estatisticas
import replay

def processar_tiro(nome_atirador, linha, coluna, matriz_alvo, frota_alvo):
    """
    Executa o tiro na matriz, atualiza a frota alvo e retorna se houve acerto.
    Também grava a jogada no replay.
    """
    acertou = False
    resultado_texto = ""

    if matriz_alvo[linha][coluna] == '-':
        matriz_alvo[linha][coluna] = 'O'
        print("\n>>> Água! Nenhum navio atingido.")
        resultado_texto = "Agua"

    elif matriz_alvo[linha][coluna] == 'N':
        matriz_alvo[linha][coluna] = 'X'
        acertou = True
        
        navio_afundado = False
        for navio in frota_alvo:
            if (linha, coluna) in navio:
                navio.remove((linha, coluna)) 
                
                if len(navio) == 0:
                    navio_afundado = True
                    frota_alvo.remove(navio) 
                break 

        if navio_afundado:
            print("\n>>> NAVIO AFUNDADO! Você destruiu uma embarcação inimiga!")
            resultado_texto = "Navio afundado"
        else:
            print("\n>>> ACERTO! Você atingiu um navio inimigo.")
            resultado_texto = "Acerto"

    replay.registrar_jogada(nome_atirador, linha, coluna, resultado_texto)
    
    return acertou

#Função principal:
def jogar_partida(modo):
    """
    Controla o fluxo principal do jogo (turnos, tiros, vitória).
    modo '1' = PvE (Jogador vs Computador)
    modo '2' = PvP (Dois Jogadores)
    """

    #Preparação
    utils.limpar_tela() #limpa a tela
    
    #Cria os tabuleiros
    matriz_j1 = tabuleiro.criar_tabuleiro()
    matriz_j2 = tabuleiro.criar_tabuleiro()
    
    
    tamanhos_frota = [4, 2, 2, 2]
    
    frota_j1 = navios.posicionar_navios(matriz_j1, tamanhos_frota)
    frota_j2 = navios.posicionar_navios(matriz_j2, tamanhos_frota)
    

    print("\nComandante (Jogador 1), esta é a posição da sua frota:")
    tabuleiro.imprimir_tabuleiro(matriz_j1, ocultar=False)
    utils.aguardar_enter("\nPressione [ENTER] para iniciar o combate...")
    
    
    turno = 1 
    jogadas_totais = 0
    acertos_j1 = 0 
    tempo_inicio = time.time() #Para o RF07
    
    #Limpa o replay da última partida
    replay.limpar_replay()

    #Loop principal
    while True:
        utils.limpar_tela()
        jogadas_totais += 1
        
        #Turno do Jogador 1
        if turno == 1:
            print(f"=== TURNO DO JOGADOR 1 (Jogada {jogadas_totais}) ===")
            print("Tabuleiro do Inimigo:")
            #ocultar = True para não mostra a posição dos navios
            tabuleiro.imprimir_tabuleiro(matriz_j2, ocultar=True)
            
            #Pede jogada e processa
            linha, coluna = jogador.obter_jogada_valida(matriz_j2)
            acertou = processar_tiro("Jogador 1", linha, coluna, matriz_j2, frota_j2)
            
            if acertou:
                acertos_j1 += 1
                
            utils.aguardar_enter("\nPressione [ENTER] para passar o turno...")
            turno = 2   #muda o turno
            
            #Verifica se o jogador ganhou
            if len(frota_j2) == 0:
                vencedor = "Jogador 1"
                break 
                
        #Turno 2 (Player 2 ou máquina)
        else:
            if modo == '1':     #Modo PvE
                
                nome_adv = "Computador"
                print(f"=== TURNO DO {nome_adv} ===")
                linha, coluna = computador.gerar_jogada_computador(matriz_j1)
                time.sleep(1)
            else:
                #Modo PvP
                nome_adv = "Jogador 2"
                print(f"=== TURNO DO {nome_adv} (Jogada {jogadas_totais}) ===")
                print("Tabuleiro do Inimigo (J1):")
                tabuleiro.imprimir_tabuleiro(matriz_j1, ocultar=True)
                linha, coluna = jogador.obter_jogada_valida(matriz_j1)

            processar_tiro(nome_adv, linha, coluna, matriz_j1, frota_j1)
            utils.aguardar_enter("\nPressione [ENTER] para passar o turno...")
            turno = 1 #Muda o turno novamente
            
            if len(frota_j1) == 0:
                vencedor = nome_adv
                break

    #Fim de jogo (Quando a função sai do loop principal)
    utils.limpar_tela()
    tempo_fim = time.time()
    minutos = int((tempo_fim - tempo_inicio) // 60)
    segundos = int((tempo_fim - tempo_inicio) % 60)
    
    print("\n" + "="*30)
    print("FIM DE JOGO - VITÓRIA!")
    print(f"Vencedor: {vencedor}")
    print(f"Total de jogadas: {jogadas_totais}")
    print(f"Tempo de partida: {minutos:02d}:{segundos:02d}")
    print("="*30 + "\n")
    
    replay.registrar_jogada("SISTEMA", 99, 99, f"VENCEDOR: {vencedor}")
    
    estatisticas.salvar_estatisticas(1, acertos_j1, (jogadas_totais // 2) + (jogadas_totais % 2))
    
    utils.aguardar_enter("\nPressione [ENTER] para voltar ao Menu Principal...")


def main():
    """
    Função principal que gerencia o estado da aplicação e os menus.
    """
    while True:
        utils.limpar_tela()
        opcao_menu = menu.exibir_menu_principal()
        
        if opcao_menu == '1':
            modo_jogo = menu.selecionar_modo_jogo()
            if modo_jogo != '0': 
                jogar_partida(modo_jogo)
                
        elif opcao_menu == '2':
            utils.limpar_tela()
            estatisticas.exibir_estatisticas()
            utils.aguardar_enter("\nPressione [ENTER] para voltar ao menu...")
            
        elif opcao_menu == '3':
            utils.limpar_tela()
            replay.exibir_replay()
            utils.aguardar_enter("\nPressione [ENTER] para voltar ao menu...")
            
        elif opcao_menu == '4':
            utils.limpar_tela()
            print("\n=== CRÉDITOS ===")
            print("Desenvolvido por: Rafael Moreira de Paula")
            print("Disciplina: Programação em Python")
            print("Professor: Guido Pantuza")
            print("================\n")
            utils.aguardar_enter("\nPressione [ENTER] para voltar ao menu...")
            
        elif opcao_menu == '5':
            utils.limpar_tela()
            print("\nObrigado por jogar Batalha Naval! Até à próxima.\n")
            break 


if __name__ == "__main__":
    main()