import os

def carregar_estatisticas():
    """
    Lê o arquivo de estatísticas. Se não existir, retorna zeros.
    """

    try:
        with open("data/estatisticas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            partidas = int(linhas[0])
            acertos = int(linhas[1])
            tiros = int(linhas[2])
            return partidas, acertos, tiros
        
    except (FileNotFoundError, IndexError, ValueError):
        return 0, 0, 0


def salvar_estatisticas(nova_partida, novos_acertos, novos_tiros):
    """
    Soma os novos dados aos existentes e salva no arquivo.
    """
    partidas_antigas, acertos_antigos, tiros_antigos = carregar_estatisticas()

    total_partidas = nova_partida + partidas_antigas
    total_acertos = novos_acertos + acertos_antigos
    total_tiros = novos_tiros + tiros_antigos

    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/estatisticas.txt", "w") as arquivo:
        arquivo.write(str(total_partidas)+"\n")
        arquivo.write(str(total_acertos)+"\n")
        arquivo.write(str(total_tiros)+"\n")


def exibir_estatisticas():
    """
    Lê e formata a exibição dos dados.
    """
    partidas, acertos, tiros = carregar_estatisticas()
    
    
    if tiros > 0:
        aproveitamento = (acertos / tiros) * 100
    else:
        aproveitamento = 0.0

    print("=== ESTATÍSTICAS ===")
    print(f"Partidas jogadas: {partidas}")
    print(f"Total de tiros: {tiros}")
    print(f"Total de acertos: {acertos}")
    print(f"Aproveitamento: {aproveitamento:.2f}%")
    print("====================")