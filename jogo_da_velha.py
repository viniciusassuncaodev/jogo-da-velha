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
    elif opcao == 1:
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