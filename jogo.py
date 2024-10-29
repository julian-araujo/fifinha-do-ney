import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura = 1900
altura = 900
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("car link")

# Cores3
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Configurações do jogador
jogador= []
tamanho_jogador = 50
velocidade_jogador = 100
posicao_jogador = [largura // 2, altura - 2 * tamanho_jogador]

# Lista de obstáculos
obstaculos = []
obstaculo_largura = 50
obstaculo_altura = 50
velocidade_obstaculo = 15

# Variáveis do jogo

clock = pygame.time.Clock()
score = 0
gerar_obstaculo_tempo = 0 

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controle do jogador

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and posicao_jogador[0] > 0:
        posicao_jogador[0] -= 5
    if keys[pygame.K_RIGHT] and posicao_jogador[0] < largura - tamanho_jogador:
        posicao_jogador[0] += 5

    # Gera novos obstáculos
    gera        (obstaculo[1] < posicao_jogador[1] < obstaculo[1] + obstaculo_altura or
                 obstaculo[1] < posicao_jogador[1] + tamanho_jogador < obstaculo[1] + obstaculo_altura):
            print("Game Over! Você colidiu.")
            running = False

    # Limpa obstáculos fora da tela
    obstaculos = [obstaculo for obstaculo in obstaculos if obstaculo[1] < altura]

    # Atualiza a tela
    screen.fill(branco)
    pygame.draw.rect(screen, preto, (posicao_jogador[0], posicao_jogador[1], tamanho_jogador, tamanho_jogador))
    for obstaculo in obstaculos:
        pygame.draw.rect(screen, vermelho, (obstaculo[0], obstaculo[1], obstaculo_largura, obstaculo_altura))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()r_obstaculo_tempo += 1
if gerar_obstaculo_tempo >= 20:  # Altere este valor para gerar obstáculos mais rapidamente
        obstaculo_x = random.randint(0, largura - obstaculo_largura)
        obstaculos.append([obstaculo_x, 0])
        gerar_obstaculo_tempo = 0

    # Move os obstáculos
for obstaculo in obstaculos:
        obstaculo[1] += velocidade_obstaculo  
for obstaculo in obstaculos:
         if (obstaculo[0] < posicao_jogador[0] < obstaculo[0] + obstaculo_largura or
                obstaculo[0] < posicao_jogador[0] + tamanho_jogador < obstaculo[0] + obstaculo_largura) and \
        