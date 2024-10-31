import pygame
import sys
import time

# Inicializar Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 600, 700
LINE_WIDTH = 10
SQUARE_SIZE = WIDTH // 3
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Cores
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)

# Configurar a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha com Escolha de Jogador e Replay")
screen.fill(BG_COLOR)

# Tabuleiro
board = [[0 for _ in range(3)] for _ in range(3)]

# Variáveis de jogador e pontuação
PLAYER_X = 1
PLAYER_O = 2
current_player = None
score_X = 0
score_O = 0
moves = []  # Lista para armazenar as jogadas de uma partida
replay_games = []  # Lista para armazenar as partidas concluídas

# Fonte para exibir a pontuação
font = pygame.font.Font(None, 48)
start_font = pygame.font.Font(None, 60)

# Função para desenhar o tabuleiro
def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, WIDTH), LINE_WIDTH)

# Função para desenhar as figuras
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == PLAYER_X:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
            elif board[row][col] == PLAYER_O:
                pygame.draw.circle(screen, CIRCLE_COLOR, 
                                   (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)

# Função para verificar vitória
def check_win(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Função para verificar empate
def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

# Função para exibir a pontuação
def draw_score():
    screen.fill(BG_COLOR, (0, WIDTH, WIDTH, HEIGHT - WIDTH))
    score_text = f"Jogador X: {score_X}   Jogador O: {score_O}"
    text = font.render(score_text, True, TEXT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, WIDTH + 30))

# Função para reiniciar o jogo
def restart():
    global board, moves
    replay_games.append(moves.copy())  # Salva as jogadas da partida anterior para o replay
    moves = []  # Reseta as jogadas para a nova partida
    board = [[0 for _ in range(3)] for _ in range(3)]
    screen.fill(BG_COLOR)
    draw_lines()
    draw_score()

# Função de Replay para ver uma partida anterior
def replay_game(game_moves):
    for move in game_moves:
        row, col, player = move
        board[row][col] = player
        screen.fill(BG_COLOR)
        draw_lines()
        draw_figures()
        pygame.display.update()
        time.sleep(0.5)  # Pausa entre as jogadas
    time.sleep(1)  # Pausa no final do replay
    restart()  # Reseta o jogo para o próximo

# Função para exibir a tela de escolha de jogador
def show_start_screen():
    global current_player
    
    screen.fill(BG_COLOR)
    title_text = "Jogo da Velha"
    prompt_text = "Escolha seu símbolo:"

    title = start_font.render(title_text, True, TEXT_COLOR)
    prompt = font.render(prompt_text, True, TEXT_COLOR)
    
    x_choice = font.render("X", True, CROSS_COLOR)
    o_choice = font.render("O", True, CIRCLE_COLOR)

    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 120))
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 - 20))
    
    screen.blit(x_choice, (WIDTH // 2 - 60, HEIGHT // 2 + 40))
    screen.blit(o_choice, (WIDTH // 2 + 20, HEIGHT // 2 + 40))
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                # Verifica se o jogador escolheu X
                if WIDTH // 2 - 60 < mouseX < WIDTH // 2 - 20 and HEIGHT // 2 + 40 < mouseY < HEIGHT // 2 + 90:
                    current_player = PLAYER_X
                    waiting = False
                # Verifica se o jogador escolheu O
                elif WIDTH // 2 + 20 < mouseX < WIDTH // 2 + 60 and HEIGHT // 2 + 40 < mouseY < HEIGHT // 2 + 90:
                    current_player = PLAYER_O
                    waiting = False

# Exibe a tela de escolha de jogador
show_start_screen()

draw_lines()
draw_score()

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and replay_games:
                replay_game(replay_games[-1])  # Reproduz a última partida salva
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            # Impedir cliques na área de pontuação
            if mouseY > WIDTH:
                continue

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = current_player
                moves.append((clicked_row, clicked_col, current_player))  # Armazena a jogada atual
                if check_win(current_player):
                    if current_player == PLAYER_X:
                        score_X += 1
                    else:
                        score_O += 1
                    print(f"Jogador {'X' if current_player == PLAYER_X else 'O'} venceu!")
                    restart()
                elif check_draw():
                    print("Empate!")
                    restart()
                else:
                    # Troca o jogador atual após cada jogada
                    current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

                draw_figures()
                draw_score()

    pygame.display.update()
