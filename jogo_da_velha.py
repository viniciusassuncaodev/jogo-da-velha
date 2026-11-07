# jogo da velha no terminal - coding(prof.martins), 2ª Avaliação (UNINASSAU)
# Integrantes: Marcus Vinicius de Assunção Bomfim, Italo Gabriel Santos Oliveira, João Victor Souza de Assis 

# tabuleiro 3x3 (matriz): cada lista de dentro é uma linha 
tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

#nomes dos jogadores (se deixar vazio, usa um nome padrão)
nome_x = input("Nome do jogador X: ")
if nome_x == "":
    nome_x ="jogador X"
nome_o = input("Nome do jogador O: ")
if nome_o == "":
    nome_o = "jogador O"

#contadores de sessão e controle do menu 
camp_jogados = 0    # campeonatos concluídos
camp_venc_x = 0     # campeonatos vencidos pelo X
camp_venc_o = 0     # campeonatos vencidos pelo O
vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0
sair = False

# menu principal: repete até o jogador escolher Sair
while sair == False:
    print("")
    print("========== JOGO DA VELHA ==========")
    print("1 - Partida avulsa")
    print("2 - Campeonato melhor de 3")
    print("3 - Campeonato melhor de 5")
    print("4 - Ver regras")
    print("5 - Ver placar")
    print("6 - Sair")

    # validação: compara o texto digitado com "1" até "6",
    # assim letra, vazio ou número fora da lista não dá erro
    opcao = 0
    valida = False
    while valida == False:
        entrada = input("Escolha uma opção (1 a 6): ")
        for n in range(1, 7):
            if entrada == str(n):
                valida = True
                opcao = n
        if valida == False:
            print("Entrada inválida! Digite um número de 1 a 6.")
    if opcao == 6:
        print("Obrigado por jogar!")
        sair = True
    elif opcao == 1 or opcao == 2 or opcao == 3:
        # meta de vitórias: 1 = partida avulsa, 2 = melhor de 3, 3 = melhor de 5
        if opcao == 2:
            meta = 2
        elif opcao == 3:
            meta = 3
        else:
            meta = 1
        camp_x = 0          # vitórias de X neste campeonato
        camp_o = 0          # vitórias de O neste campeonato
        continuar = True    # vira False quando a partida avulsa ou o campeonato acabar
        while continuar == True:
            vez_x = True        # booleano: True = vez do X, False = vez do O
            fim = False         # vira True quando a partida acabar
            resultado = ""      # texto com o resultado, mostrado no fim da partida
            # limpa o tabuleiro: i percorre as linhas e j percorre as colunas
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = " "
            while fim == False:
                # mostra o tabuleiro: i percorre as linhas e j percorre as colunas
                print("")
                print("     1   2   3")
                for i in range(3):
                    print(str(i + 1) + "   ", end="")
                    for j in range(3):
                        print(" " + tabuleiro[i][j] + " ", end="")
                        if j < 2:
                            print("|", end="")
                    print("")
                    if i < 2:
                        print("    ---+---+---")
                # define de quem é a vez
                if vez_x == True:
                    simbolo = "X"
                    print("Vez de " + nome_x + " (X)")
                else:
                    simbolo = "O"
                    print("Vez de " + nome_o + " (O)")
                # lê a jogada: repete até a linha, a coluna e a casa estarem corretas
                jogada_ok = False
                while jogada_ok == False:
                    linha = 0
                    valida = False
                    while valida == False:
                        entrada = input("Linha (1 a 3): ")
                        for n in range(1, 4):
                            if entrada == str(n):
                                valida = True
                                linha = n - 1
                        if valida == False:
                            print("Entrada inválida! Digite um número de 1 a 3.")
                    coluna = 0
                    valida = False
                    while valida == False:
                        entrada = input("Coluna (1 a 3): ")
                        for n in range(1, 4):
                            if entrada == str(n):
                                valida = True
                                coluna = n - 1
                        if valida == False:
                            print("Entrada inválida! Digite um número de 1 a 3.")
                    if tabuleiro[linha][coluna] != " ":
                        print("Casa já ocupada! Escolha outra casa.")
                    else:
                        jogada_ok = True
                # marca a jogada na matriz
                tabuleiro[linha][coluna] = simbolo
                # verifica vitória: o for repete o mesmo teste para cada índice i (0, 1 e 2)
                venceu = False
                diagonal_principal = 0
                diagonal_secundaria = 0
                for i in range(3):
                    if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
                        venceu = True
                    if tabuleiro[0][i] == simbolo and tabuleiro[1][i] == simbolo and tabuleiro[2][i] == simbolo:
                        venceu = True
                    if tabuleiro[i][i] == simbolo:
                        diagonal_principal = diagonal_principal + 1
                    if tabuleiro[i][2 - i] == simbolo:
                        diagonal_secundaria = diagonal_secundaria + 1
                if diagonal_principal == 3 or diagonal_secundaria == 3:
                    venceu = True
                # conta as casas vazias
                vazias = 0
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] == " ":
                            vazias = vazias + 1
                # decide o resultado da rodada: vitória, empate ou continua
                if venceu == True:
                    resultado = "Fim de jogo! " + simbolo + " venceu!"
                    fim = True
                    total_partidas = total_partidas + 1
                    if simbolo == "X":
                        vitorias_x = vitorias_x + 1
                        camp_x = camp_x + 1
                    else:
                        vitorias_o = vitorias_o + 1
                        camp_o = camp_o + 1
                elif vazias == 0:
                    resultado = "Deu empate!"
                    fim = True
                    total_partidas = total_partidas + 1
                    empates = empates + 1
                else:
                    vez_x = not vez_x
            # partida terminou: mostra o tabuleiro final e o resultado
            print("")
            print("     1   2   3")
            for i in range(3):
                print(str(i + 1) + "   ", end="")
                for j in range(3):
                    print(" " + tabuleiro[i][j] + " ", end="")
                    if j < 2:
                        print("|", end="")
                print("")
                if i < 2:
                    print("    ---+---+---")
            print(resultado)
            # o que acontece depois da partida
            if opcao == 1:
                # jogar novamente? valida comparando o texto com "1" e "2"
                print("")
                print("1 - Jogar novamente")
                print("2 - Voltar ao menu")
                valida = False
                while valida == False:
                    entrada = input("Escolha (1 ou 2): ")
                    for n in range(1, 3):
                        if entrada == str(n):
                            valida = True
                            if n == 2:
                                continuar = False
                    if valida == False:
                        print("Entrada inválida! Digite 1 ou 2.")
            else:
                # campeonato: mostra o parcial e verifica se alguém chegou à meta
                print("Campeonato: " + nome_x + " " + str(camp_x) + " x " + str(camp_o) + " " + nome_o)
                if camp_x == meta:
                    print("CAMPEÃO: " + nome_x + "!")
                    camp_jogados = camp_jogados + 1
                    camp_venc_x = camp_venc_x + 1
                    continuar = False
                elif camp_o == meta:
                    print("CAMPEÃO: " + nome_o + "!")
                    camp_jogados = camp_jogados + 1
                    camp_venc_o = camp_venc_o + 1
                    continuar = False
    elif opcao == 4:

        print("")
        print("REGRAS:")
        print("- O tabuleiro tem 3 linhas e 3 colunas.")
        print("- Os jogadores se alternam marcando X ou O em uma casa vazia.")
        print("- Para jogar, informe o número da linha e da coluna (1 a 3).")
        print("- Vence quem completar uma linha, coluna ou diagonal.")
        print("- Se o tabuleiro encher sem vencedor, é empate.")

    elif opcao == 5:
        print("")
        print("PLACAR E ESTATÍSTICAS DA SESSÃO:")
        print("Vitórias de " + nome_x + " (X): " + str(vitorias_x))
        print("Vitórias de " + nome_o + " (O): " + str(vitorias_o))
        print("Empates: " + str(empates))
        print("Total de partidas: " + str(total_partidas))
        if total_partidas > 0:
            print("Aproveitamento de " + nome_x + ": " + str(int(vitorias_x * 100 / total_partidas)) + "%")
            print("Aproveitamento de " + nome_o + ": " + str(int(vitorias_o * 100 / total_partidas)) + "%")
        print("Campeonatos concluídos: " + str(camp_jogados))
        print("Campeonatos vencidos por " + nome_x + ": " + str(camp_venc_x))
        print("Campeonatos vencidos por " + nome_o + ": " + str(camp_venc_o))