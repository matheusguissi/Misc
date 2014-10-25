'''
Created on 22/10/2014

@author: matheus
'''

def Imprimir(jogo):
    print()
    for i in range(3):
        print(' ' + str(jogo[3*i]) + " | " + str(jogo[3*i+1]) + " | " + str(jogo[3*i+2]))
        if i != 2:
            print("---+---+---")
        else:
            print()

'''Vitórias:
0,1,2 / 3,4,5 / 6,7,8
0,3,6 / 1,4,7 / 2,5,8
0,4,8 / 2,4,6
'''
            
def Vitoria(jogo, jogadas):
    if jogo[0] == jogo[1] == jogo[2]:
        print("Vitoria do jogador " + jogo[0] + '!')
        return 1
    elif jogo[3] == jogo[4] == jogo[5]:
        print("Vitoria do jogador " + jogo[3] + '!')
        return 1
    elif jogo[6] == jogo[7] == jogo[8]:
        print("Vitoria do jogador " + jogo[6] + '!')
        return 1
    elif jogo[0] == jogo[3] == jogo[6]:
        print("Vitoria do jogador " + jogo[0] + '!')
        return 1
    elif jogo[1] == jogo[4] == jogo[7]:
        print("Vitoria do jogador " + jogo[1] + '!')
        return 1
    elif jogo[2] == jogo[5] == jogo[8]:
        print("Vitoria do jogador " + jogo[2] + '!')
        return 1
    elif jogo[0] == jogo[4] == jogo[8]:
        print("Vitoria do jogador " + jogo[0] + '!')
        return 1
    elif jogo[2] == jogo[4] == jogo[6]:
        print("Vitoria do jogador " + jogo[0] + '!')
        return 1
    elif jogadas == 8:
        print("Deu velha!")
        return 1
    else:
        return 0
        
        
while True:     
    # Inicializando "tabuleiro" do jogo
    jogo = [' '] * 9
    for i in range(9):
        jogo[i] = i
 
    print("Jogo da Velha\n")

    #Decidindo símbolo dos jogadores
    jogador = input("Jogador 1, escolha X ou O para comecar: ").upper() 
    while jogador != "X" and jogador != "O":
        jogador = input("Opcao Invalida, escolha novamente: ").upper()
    if jogador == "X":
        jogador2 = "O"
    else:
        jogador2 = "X"

    #Início do jogo
    Imprimir(jogo)
    for i in range(9):
        #Para alternar a vez dos jogadores, fui verificando se o numero da jogada era par ou impar, assim alternando entre os jogadores
        if i%2 == 0: 
            print("Vez do jogador " + jogador)
            posicao = int(input("Escolha uma posicao: "))
            while posicao != jogo[posicao]:
                posicao = int(input("Opcao Invalida, escolha novamente: "))
            jogo[posicao] = jogador
        else:
            print("Vez do jogador " + jogador2)
            posicao = int(input("Escolha uma posicao: "))
            while posicao != jogo[posicao]:
                posicao = int(input("Opcao Invalida, escolha novamente: "))
            jogo[posicao] = jogador2
        Imprimir(jogo)
        if Vitoria(jogo, i):
            break
    
    escolha = input("\nDeseja jogar novamente (S/N)? ").upper()
    if escolha == 'N':
        break
    else:
        print("\n------------------------------------------\n")
    