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