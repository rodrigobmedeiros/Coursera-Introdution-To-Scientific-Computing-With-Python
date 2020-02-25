#NIM Game
#Developed by: Rodrigo Bernardo Medeiros
#Date: 17/02/2020
#Code to play NIM Game - It's not possible win from machine


def partida():

    print('Bem-vindo ao jogo do NIM! Escolha:')
    print()
    print('1 - para jogar uma partida isolada')
    codigo = int(input('2 - para jogar um campeonato '))
    print()
    partida = 1
    vitoriacomputador = 0
    vitoriahumano = 0
    
    if codigo ==1:

        jogo()

    else:

        while partida<=3:
            print('*** Rodada',partida,'***')
            print()
            resultado = jogo()

            if resultado:
                vitoriahumano = vitoriahumano + 1

            else:
                vitoriacomputador = vitoriacomputador + 1
            partida = partida + 1

            
        print('**** Final do campeonato! ****')
        print()

        print('Placar: Você', vitoriahumano, 'X', vitoriacomputador, 'Computador')
            
        

def jogo():
    
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    jogagahumana = 0
    joagadacomputador = 0
    n_retiradas = 0
    iscomputer = False
    
    if m>n:

        return 'O limite de peças por jogada deve ser menor ou igual a quantidade de peças'
    
    #primeira jogada
    if n%(m+1)==0:
        print('Você começa!')
        print()
        n_retiradas = usuario_escolhe_jogada(n,m)
        iscomputer = True
        
    else:

        n_retiradas = computador_escolhe_jogada(n,m)
        iscomputer = False

    n_atual = n-n_retiradas
    andamentojogo(n_atual,iscomputer)

    while n_atual >0:

        if iscomputer:

            n_retiradas = computador_escolhe_jogada(n_atual,m)
            n_atual = n_atual-n_retiradas
            iscomputer = False
            andamentojogo(n_atual,iscomputer)
            
        else:
            n_retiradas = usuario_escolhe_jogada(n_atual,m)
            n_atual = n_atual - n_retiradas
            iscomputer = True
            andamentojogo(n_atual,iscomputer)


    return iscomputer
    #Se iscomputer for verdadeiro o usuário ganhou senão o computador ganhou



def andamentojogo(n,iscomputer):

    if n>0:

        if n ==1:
            print('Agora resta uma peça no tabuleiro')

        else:
            print('Agora restam', n, 'peças no tabuleiro.')
        print()
        
    else:

        if iscomputer:
            print('Fim de jogo! Você ganhou!')
            print()

        else:
            print('Fim de jogo! O computador ganhou!')
            print()
        


def computador_escolhe_jogada(n,m):

    multiplo = 1
    jogada = n-(m+1)*multiplo
    multiplo = multiplo + 1
    
    if n<=m:
        jogada = n

    else:

        while jogada>m:
            
            jogada = n-(m+1)*multiplo
            multiplo = multiplo + 1
            
    if jogada == 1:
        print('O computador tirou uma peça')

    else:
        print('O computador tirou', jogada, 'peças.')
    
    
    print()
    return jogada



def usuario_escolhe_jogada(n,m):

    jogada = int(input('Quantas peças você vai tirar? '))
    print()
    iscorrect = False

    while not iscorrect:
        if jogada<=0 or jogada >m:
            print('Oops! Jogada inválida! Tente de novo.')
            print()
            jogada = int(input('Quantas peças você vai tirar? '))
            print()

        else:
            iscorrect = True
            

    if jogada == 1:
        print('Você tirou uma peça')
    else:
        print('Você tirou',jogada,'peças')

    print()
    return jogada


partida()
