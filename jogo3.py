import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 500, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desvio de Obstáculos")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configurações do jogador
jogador_largura, jogador_altura = 50, 50
jogador_x = LARGURA // 2 - jogador_largura // 2
jogador_y = ALTURA - jogador_altura - 10
velocidade_jogador = 15

# Configurações dos obstáculos
obstaculos = []
velocidade_obstaculo = 8
intervalo_obstaculo = 1000  # 1 segundo

# Configuração de pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)

# Relógio e temporizador
relogio = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, intervalo_obstaculo)

# Função principal do jogo
def jogo():
    global jogador_x, pontuacao
    rodando = True
    while rodando:
        TELA.fill(PRETO)

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.USEREVENT:
                # Criar novo obstáculo em posição aleatória
                x_aleatorio = random.randint(0, LARGURA - jogador_largura)
                obstaculos.append(pygame.Rect(x_aleatorio, -jogador_altura, jogador_largura, jogador_altura))

        # Movimento do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador_x > 0:
            jogador_x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_largura:
            jogador_x += velocidade_jogador

        # Movimentos dos obstáculos
        for obstaculo in obstaculos[:]:
            obstaculo.y += velocidade_obstaculo
            if obstaculo.colliderect(pygame.Rect(jogador_x, jogador_y, jogador_largura, jogador_altura)):
                print("Fim de jogo!")
                rodando = False
            if obstaculo.y > ALTURA:
                obstaculos.remove(obstaculo)
                pontuacao += 1

        # Desenhar jogador e obstáculos
        pygame.draw.rect(TELA, AZUL, (jogador_x, jogador_y, jogador_largura, jogador_altura))
        for obstaculo in obstaculos:
            pygame.draw.rect(TELA, VERMELHO, obstaculo)

        # Desenhar pontuação
        texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        TELA.blit(texto_pontuacao, (10, 10))

        # Atualizar a tela e o relógio
        pygame.display.flip()
        relogio.tick(30)

# Executar o jogo
if __name__ == "__main__":
    jogo()
