import pygame
import random
import sys

# Inicializar o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Desviar de Obstáculos")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurações do jogador
jogador_largura, jogador_altura = 50, 50
jogador_x, jogador_y = LARGURA // 2, ALTURA - jogador_altura - 10
velocidade_jogador = 20

# Configurações dos obstáculos
obstaculo_largura, obstaculo_altura = 50, 50
obstaculos = []
velocidade_obstaculo = 10
intervalo_obstaculo = 2000  # 2 segundos

# Configuração de pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)

# Relógio e temporizador
relogio = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, intervalo_obstaculo)

# Função para desenhar o jogador
def desenhar_jogador(x, y):
    pygame.draw.rect(TELA, AZUL, (x, y, jogador_largura, jogador_altura))

# Função para desenhar os obstáculos
def desenhar_obstaculos(obstaculos):
    for obstaculo in obstaculos:
        pygame.draw.rect(TELA, VERMELHO, obstaculo)

# Função principal do jogo
def jogo():
    global jogador_x, jogador_y, pontuacao

    rodando = True
    while rodando:
        TELA.fill(BRANCO)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.USEREVENT:
                x_aleatorio = random.randint(0, LARGURA - obstaculo_largura)
                obstaculos.append(pygame.Rect(x_aleatorio, 0, obstaculo_largura, obstaculo_altura))

        # Movimentos do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador_x > 0:
            jogador_x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_largura:
            jogador_x += velocidade_jogador

        # Movimentos dos obstáculos
        for obstaculo in obstaculos[:]:
            obstaculo.y += velocidade_obstaculo
            if obstaculo.colliderect((jogador_x, jogador_y, jogador_largura, jogador_altura)):
                print("Fim de jogo!")
                rodando = False
            if obstaculo.y > ALTURA:
                obstaculos.remove(obstaculo)
                pontuacao += 1

        # Desenhar jogador e obstáculos
        desenhar_jogador(jogador_x, jogador_y)
        desenhar_obstaculos(obstaculos)

        # Desenhar pontuação
        texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, PRETO)
        TELA.blit(texto_pontuacao, (10, 10))

        # Atualizar a tela e o relógio
        pygame.display.flip()
        relogio.tick(30)

# Executar o jogo
if __name__ == "__main__":
    jogo()