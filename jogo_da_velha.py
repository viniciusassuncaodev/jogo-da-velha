# ============================================================
# JOGO DA VELHA NO TERMINAL - Coding (2ª Avaliação) - UNINASSAU
# Usa apenas: variáveis, operadores, if/elif/else, while, for,
# range(), matriz (lista de listas), print(), input(), int(),
# float() e str().
# ============================================================

# ----- Tabuleiro 3x3 declarado por extenso (matriz) -----
tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

# ----- Variáveis da sessão (placar acumulado e estatísticas) -----
nome_x = input("Nome do jogador X: ")
if nome_x == "":
    nome_x = "Jogador X"
nome_o = input("Nome do jogador O: ")
if nome_o == "":
    nome_o = "Jogador O"

vitorias_x = 0          # vitórias do jogador X
vitorias_o = 0          # vitórias do jogador O
empates = 0             # empates
total_partidas = 0      # contador de partidas da sessão
sequencia_x = 0         # sequência atual de vitórias seguidas de X
sequencia_o = 0         # sequência atual de vitórias seguidas de O
maior_sequencia_x = 0   # maior sequência de X na sessão
maior_sequencia_o = 0   # maior sequência de O na sessão
campeonatos_x = 0       # campeonatos (melhor de N) ganhos por X
campeonatos_o = 0       # campeonatos (melhor de N) ganhos por O

sair = False

# ===================== MENU PRINCIPAL (while) =====================
while sair == False:
    print("")
    print("========== JOGO DA VELHA ==========")
    print("1 - Partida avulsa")
    print("2 - Campeonato melhor de 3")
    print("3 - Campeonato melhor de 5")
    print("4 - Ver regras")
    print("5 - Ver placar")
    print("6 - Sair")

    # Validação do menu: compara o texto digitado com cada opção válida
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

    # ---------- Regras ----------
    if opcao == 4:
        print("")
        print("REGRAS:")
        print("- O tabuleiro tem 3 linhas e 3 colunas.")
        print("- Os jogadores se alternam marcando X ou O em uma casa vazia.")
        print("- Para jogar, informe o número da linha e da coluna (1 a 3).")
        print("- Vence quem completar uma linha, coluna ou diagonal.")
        print("- Se o tabuleiro encher sem vencedor, é empate.")
        print("- Campeonato: vence a série quem fizer a maioria das vitórias")
        print("  (2 em melhor de 3, 3 em melhor de 5). Empates não contam.")

    # ---------- Placar ----------
    elif opcao == 5:
        print("")
        print("PLACAR ACUMULADO")
        print(nome_x + " (X): " + str(vitorias_x) + " vitória(s)")
        print(nome_o + " (O): " + str(vitorias_o) + " vitória(s)")
        print("Empates: " + str(empates))
        print("Campeonatos: " + nome_x + " " + str(campeonatos_x) + " x " + str(campeonatos_o) + " " + nome_o)

    # ---------- Sair (mostra estatísticas da sessão) ----------
    elif opcao == 6:
        print("")
        print("======= ESTATÍSTICAS DA SESSÃO =======")
        print("Total de partidas: " + str(total_partidas))
        print(nome_x + " (X): " + str(vitorias_x) + " vitória(s)")
        print(nome_o + " (O): " + str(vitorias_o) + " vitória(s)")
        print("Empates: " + str(empates))
        if total_partidas > 0:
            # porcentagem como número real, com 1 casa decimal (sem round)
            pct_x = vitorias_x * 100 / total_partidas
            pct_o = vitorias_o * 100 / total_partidas
            pct_x = int(pct_x * 10) / 10
            pct_o = int(pct_o * 10) / 10
            print("Porcentagem de vitórias de " + nome_x + ": " + str(pct_x) + "%")
            print("Porcentagem de vitórias de " + nome_o + ": " + str(pct_o) + "%")
        else:
            print("Nenhuma partida jogada ainda.")
        print("Maior sequência de vitórias de " + nome_x + ": " + str(maior_sequencia_x))
        print("Maior sequência de vitórias de " + nome_o + ": " + str(maior_sequencia_o))
        print("Obrigado por jogar!")
        sair = True

    # ---------- Jogar (opções 1, 2 e 3) ----------
    else:
        # meta = vitórias necessárias para ganhar a série (desafio "melhor de N")
        meta = 0
        if opcao == 2:
            meta = 2
        elif opcao == 3:
            meta = 3
        serie_x = 0
        serie_o = 0
        continuar = True

        while continuar == True:
            # Limpa a matriz com for aninhado (reinício da partida)
            for i in range(3):
                for j in range(3):
                    tabuleiro[i][j] = " "

            # Quem começa alterna a cada partida (operador % e booleano)
            vez_x = (total_partidas % 2 == 0)
            fim = False
            venceu = False

            print("")
            print("----- NOVA PARTIDA -----")

            # ============ Sequência de jogadas (while) ============
            while fim == False:
                # Exibe o tabuleiro com for aninhado e números de linhas/colunas
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

                if vez_x == True:
                    simbolo = "X"
                    nome_atual = nome_x
                else:
                    simbolo = "O"
                    nome_atual = nome_o
                print("")
                print("Vez de " + nome_atual + " (" + simbolo + ")")

                # ---- Leitura da jogada com validação ----
                jogada_ok = False
                while jogada_ok == False:
                    # lê a linha
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
                    # lê a coluna
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
                    # confere se a casa está livre
                    if tabuleiro[linha][coluna] != " ":
                        print("Casa já ocupada! Escolha outra casa.")
                    else:
                        jogada_ok = True

                tabuleiro[linha][coluna] = simbolo

                # ---- Verificação de vitória com laços (for) ----
                venceu = False
                for i in range(3):
                    cont_linha = 0
                    cont_coluna = 0
                    for j in range(3):
                        if tabuleiro[i][j] == simbolo:
                            cont_linha = cont_linha + 1      # percorre a linha i
                        if tabuleiro[j][i] == simbolo:
                            cont_coluna = cont_coluna + 1    # percorre a coluna i
                    if cont_linha == 3 or cont_coluna == 3:
                        venceu = True
                # diagonais: um único laço percorre as duas
                diag_principal = 0
                diag_secundaria = 0
                for i in range(3):
                    if tabuleiro[i][i] == simbolo:
                        diag_principal = diag_principal + 1
                    if tabuleiro[i][2 - i] == simbolo:
                        diag_secundaria = diag_secundaria + 1
                if diag_principal == 3 or diag_secundaria == 3:
                    venceu = True

                # ---- Contagem de casas vazias (for aninhado) ----
                vazias = 0
                for i in range(3):
                    for j in range(3):
                        if tabuleiro[i][j] == " ":
                            vazias = vazias + 1

                # ---- Resultado da jogada ----
                if venceu == True:
                    fim = True
                elif vazias == 0 and not venceu:
                    fim = True
                else:
                    vez_x = not vez_x   # passa a vez

            # ============ Fim da partida: mostra tabuleiro final ============
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
            print("")

            total_partidas = total_partidas + 1

            if venceu == True:
                print("Fim de jogo! " + nome_atual + " (" + simbolo + ") venceu!")
                if simbolo == "X":
                    vitorias_x = vitorias_x + 1
                    serie_x = serie_x + 1
                    sequencia_x = sequencia_x + 1
                    sequencia_o = 0
                    if sequencia_x > maior_sequencia_x:
                        maior_sequencia_x = sequencia_x
                else:
                    vitorias_o = vitorias_o + 1
                    serie_o = serie_o + 1
                    sequencia_o = sequencia_o + 1
                    sequencia_x = 0
                    if sequencia_o > maior_sequencia_o:
                        maior_sequencia_o = sequencia_o
            else:
                print("Fim de jogo! Deu empate!")
                empates = empates + 1
                sequencia_x = 0
                sequencia_o = 0

            # Placar acumulado ao final de cada partida
            print("")
            print("PLACAR: " + nome_x + " " + str(vitorias_x) + " x " + str(vitorias_o) + " " + nome_o + " | Empates: " + str(empates))

            # ---- Controle da série / jogar novamente ----
            if meta == 0:
                # partida avulsa: pergunta se quer jogar novamente
                valida = False
                while valida == False:
                    entrada = input("Jogar novamente? (1 - Sim, 2 - Não): ")
                    if entrada == "1":
                        valida = True
                    elif entrada == "2":
                        valida = True
                        continuar = False
                    else:
                        print("Entrada inválida! Digite 1 ou 2.")
            else:
                print("SÉRIE (melhor de " + str(meta * 2 - 1) + "): " + nome_x + " " + str(serie_x) + " x " + str(serie_o) + " " + nome_o)
                if serie_x == meta:
                    print("CAMPEÃO DA SÉRIE: " + nome_x + "!")
                    campeonatos_x = campeonatos_x + 1
                    continuar = False
                elif serie_o == meta:
                    print("CAMPEÃO DA SÉRIE: " + nome_o + "!")
                    campeonatos_o = campeonatos_o + 1
                    continuar = False