# Jogo da Velha no Terminal

Trabalho da 2ª avaliação da disciplina **Coding**, do curso de Tecnologia da **UNINASSAU**.
Professor: Tiago Martins Ribeiro.

## Integrantes

| Integrante | Responsabilidades |
|---|---|
| Marcus Vinicius de Assunção Bomfim | Matriz e variáveis, menu principal, exibição do tabuleiro, leitura e validação da jogada |
| Italo Gabriel Santos Oliveira | Vez dos jogadores, verificação de vitória, detecção de empate |
| João Victor Sousa de Assis | Placar, reinício da matriz, jogar novamente, campeonato, estatísticas e README |

## Sobre o jogo

Jogo da Velha (3x3) para **dois jogadores humanos**, feito em Python e executado no terminal.
O tabuleiro é uma matriz (lista de listas), percorrida com laços `for` aninhados.

## Funcionalidades

- **Menu principal** com validação da opção digitada (1 a 6).
- **Partida avulsa** entre dois jogadores, com nomes personalizados (ou nomes padrão se ficar vazio).
- **Exibição do tabuleiro** com números de linha e coluna.
- **Validação da jogada:** linha de 1 a 3, coluna de 1 a 3 e casa ainda vazia.
- **Verificação de vitória** por linhas, colunas e diagonais, com laços `for`.
- **Detecção de empate** contando as casas vazias com `for` aninhado.
- **Placar acumulado** de vitórias do X, vitórias do O, empates e total de partidas.
- **Reinício automático do tabuleiro** no começo de cada partida.
- **Regras** do jogo disponíveis no menu.

### Desafios escolhidos

- **Campeonato melhor de 3 ou 5:** as partidas se repetem até um jogador chegar ao número de vitórias necessário (2 na melhor de 3 e 3 na melhor de 5).
- **Estatísticas da sessão:** resumo das partidas jogadas desde que o programa foi aberto.

## Como executar

1. Tenha o Python 3 instalado.
2. No terminal, dentro da pasta do projeto, rode:
   ```
   python jogo_da_velha.py
   ```
3. Digite o nome dos jogadores X e O (ou deixe vazio para usar o nome padrão).
4. No menu, digite o número da opção desejada (1 a 6).
5. Durante a partida, informe a linha e a coluna (1 a 3) da casa escolhida.

## Menu

| Opção | O que faz |
|---|---|
| 1 | Partida avulsa |
| 2 | Campeonato melhor de 3 |
| 3 | Campeonato melhor de 5 |
| 4 | Ver regras |
| 5 | Ver placar |
| 6 | Sair |

## Regras do jogo

- O tabuleiro tem 3 linhas e 3 colunas.
- Os jogadores se alternam marcando X ou O em uma casa vazia.
- Vence quem completar uma linha, coluna ou diagonal.
- Se o tabuleiro encher sem vencedor, é empate.

## Regras do professor respeitadas

- Tabuleiro como matriz (lista de listas) declarada por extenso e acessada por `tabuleiro[i][j]`.
- Exibição, reinício e contagem de casas vazias com `for` aninhado.
- Verificação de vitória com laços `for`, sem um `if` para cada combinação.
- Validação de entrada sem `try/except`: o texto digitado é comparado com cada opção válida usando `for` e `str()`, e o `while` repete até ser válido.
- Sem funções criadas por nós, dicionários, tuplas, conjuntos, listas fora da matriz, métodos de lista ou texto, `import` nem classes.

## Entrega

- Código: este repositório.
- Relatório em PDF: [adicionar link ou nome do arquivo]
- Vídeo (3 a 10 minutos): [adicionar link]