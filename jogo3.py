import pygame
import random
import sys
# Inicializar o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Desviar de Caminhões")

# Cores
BRANCO = (255, 255, 255)

# Carregar imagens
try:
    estrada = pygame.image.load('estrada.png').convert()
    carro_jogador = pygame.image.load('carro_jogador.png').convert_alpha()
    caminhao_img = pygame.image.load('caminhao.png').convert_alpha()
except pygame.error as e:
    print(f"Erro ao carregar uma das imagens: {e}")
    sys.exit()

# Configurações do jogador
jogador_largura, jogador_altura = carro_jogador.get_width(), carro_jogador.get_height()
jogador_x, jogador_y = LARGURA // 2 - jogador_largura // 2, ALTURA - jogador_altura - 10
velocidade_jogador = 5

# Configurações dos caminhões (obstáculos)
caminhoes = []
velocidade_caminhao = 5
intervalo_caminhao = 1500  # 1.5 segundos

# Configuração de pontuação
pontuacao = 0
fonte = pygame.font.Font(None, 36)

# Movimento da estrada
posicao_estrada = 0
velocidade_estrada = 5

# Relógio e temporizador
relogio = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, intervalo_caminhao)

# Função para desenhar o jogador
def desenhar_jogador(x, y):
    TELA.blit(carro_jogador, (x, y))

# Função para desenhar os caminhões
def desenhar_caminhoes(caminhoes):
    for caminhao in caminhoes:
        TELA.blit(caminhao_img, caminhao)

# Função principal do jogo
def jogo():
    global jogador_x, pontuacao, posicao_estrada

    rodando = True
    while rodando:
        # Movimento da estrada
        posicao_estrada += velocidade_estrada
        if posicao_estrada >= ALTURA:
            posicao_estrada = 0

        # Desenhar fundo da estrada (simulando movimento contínuo)
        TELA.blit(estrada, (0, posicao_estrada - ALTURA))
        TELA.blit(estrada, (0, posicao_estrada))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.USEREVENT:
                x_aleatorio = random.randint(0, LARGURA - caminhao_img.get_width())
                caminhoes.append(pygame.Rect(x_aleatorio, -caminhao_img.get_height(), caminhao_img.get_width(), caminhao_img.get_height()))

        # Movimentos do jogador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jogador_x > 0:
            jogador_x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_largura:
            jogador_x += velocidade_jogador

        # Movimentos dos caminhões
        for caminhao in caminhoes[:]:
            caminhao.y += velocidade_caminhao
            if caminhao.colliderect((jogador_x, jogador_y, jogador_largura, jogador_altura)):
                print("Fim de jogo!")
                rodando = False
            if caminhao.y > ALTURA:
                caminhoes.remove(caminhao)
                pontuacao += 1

        # Desenhar jogador e caminhões
        desenhar_jogador(jogador_x, jogador_y)
        desenhar_caminhoes(caminhoes)

        # Desenhar pontuação
        texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        TELA.blit(texto_pontuacao, (10, 10))

        # Atualizar a tela e o relógio
        pygame.display.flip()
        relogio.tick(30)

# Executar o jogo
if __name__ == "__main__":
    jogo()
