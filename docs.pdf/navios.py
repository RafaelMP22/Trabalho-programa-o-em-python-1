import random
#Usaremos o random para podermos alocar os navios de maneira automática e aleatória 

def posicionar_navios(tabuleiro, frota):
    '''
    Posiciona os navios de maneira automática e aleatória, a variavel frota é uma lista 
    com o tamanho dos navios que serão posicionados.
    '''

    coordenadas_frota = []
    for tamanho in frota:
        colocado = False        #Variavel de controle

        while not colocado:

            orientacao = random.choice(["H", "V"])  #Escolhe a orientação dos navios de forma aleatória
            coluna_inicial = random.randint(0, 9)
            linha_inicial = random.randint(0, 9)

            if(orientacao=="H"):
                if((coluna_inicial + tamanho) > 10):
                    pass
                else:
                    espaco_livre = True
                    for i in range(tamanho):
                        if (tabuleiro[linha_inicial][coluna_inicial + i] != '-'):   #confere se o espaço está livre
                            espaco_livre = False
                            break

                    if espaco_livre:
                        navio_atual = []
                        for i in range(tamanho):
                            tabuleiro[linha_inicial][coluna_inicial + i] = 'N'
                            navio_atual.append((linha_inicial, coluna_inicial + i)) 
                        coordenadas_frota.append(navio_atual) 
                        colocado = True

            if(orientacao=="V"):
                if((linha_inicial + tamanho) > 10):
                    pass
                else:
                    espaco_livre = True
                    for i in range(tamanho):
                        if (tabuleiro[linha_inicial + i][coluna_inicial] != '-'):
                            espaco_livre = False
                            break

                    if espaco_livre:
                        navio_atual = []
                        for i in range(tamanho):
                            tabuleiro[linha_inicial + i][coluna_inicial] = 'N'
                            navio_atual.append((linha_inicial + i, coluna_inicial))
                        coordenadas_frota.append(navio_atual)
                        colocado = True
    return coordenadas_frota



