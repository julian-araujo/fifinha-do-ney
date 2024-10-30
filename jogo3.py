import pygame
import random
import sys

# Inicializar o pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 600, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Corrida de Carros contra Caminhões")

# Cores
PRETO = (0, 0, 0)

# Carregar imagens
estrada = pygame.image.load('estrada.png').convert()
carro_azul = pygame.image.load('carro_azul.png').convert_alpha()
carro_verde = pygame.image.load('carro_verde.png').convert_alpha()
caminhao_img = pygame.image.load('caminhao.png').convert_alpha()

# Configurações dos jogadores (carros)
jogador1_x, jogador1_y = LARGURA // 4 - carro_azul.get_width() // 2, ALTURA - carro_azul.get_height() - 10
jogador2_x, jogador2_y = 3 * LARGURA // 4 - carro_verde.get_width() // 2, ALTURA - carro_verde.get_height() - 10
velocidade_jogador = 5

# Configurações dos caminhões (obstáculos)
caminhoes = []
velocidade_caminhao = 5
intervalo_caminhao = 1500  # 1.5 segundos

# Configuração de pontuação
pontuacao1 = 0
pontuacao2 = 0
fonte = pygame.font.Font(None, 36)

# Movimento da estrada
posicao_estrada = 0
velocidade_estrada = 5

# Relógio e temporizador
relogio = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, intervalo_caminhao)

# Função principal do jogo
def jogo():
    global jogador1_x, jogador1_y, jogador2_x, jogador2_y, pontuacao1, pontuacao2, posicao_estrada

    rodando = True
    while rodando:
        # Movimento da estrada
        posicao_estrada += velocidade_estrada
        if posicao_estrada >= ALTURA:
            posicao_estrada = 0

        # Desenhar fundo da estrada
        TELA.blit(estrada, (0, posicao_estrada - ALTURA))
        TELA.blit(estrada, (0, posicao_estrada))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.USEREVENT:
                x_aleatorio = random.choice([LARGURA // 4 - caminhao_img.get_width() // 2, 3 * LARGURA // 4 - caminhao_img.get_width() // 2])
                caminhoes.append(pygame.Rect(x_aleatorio, -caminhao_img.get_height(), caminhao_img.get_width(), caminhao_img.get_height()))

        # Movimentos dos jogadores
        teclas = pygame.key.get_pressed()
        # Controles do jogador 1 (setas)
        if teclas[pygame.K_LEFT] and jogador1_x > 0:
            jogador1_x -= velocidade_jogador
        if teclas[pygame.K_RIGHT] and jogador1_x < LARGURA // 2 - carro_azul.get_width():
            jogador1_x += velocidade_jogador

        # Controles do jogador 2 (WASD)
        if teclas[pygame.K_a] and jogador2_x > LARGURA // 2:
            jogador2_x -= velocidade_jogador
        if teclas[pygame.K_d] and jogador2_x < LARGURA - carro_verde.get_width():
            jogador2_x += velocidade_jogador

        # Movimentos dos caminhões
        for caminhao in caminhoes[:]:
            caminhao.y += velocidade_caminhao
            if caminhao.colliderect((jogador1_x, jogador1_y, carro_azul.get_width(), carro_azul.get_height())):
                print("Jogador 1 bateu! Fim de jogo!")
                rodando = False
            if caminhao.colliderect((jogador2_x, jogador2_y, carro_verde.get_width(), carro_verde.get_height())):
                print("Jogador 2 bateu! Fim de jogo!")
                rodando = False
            if caminhao.y > ALTURA:
                caminhoes.remove(caminhao)
                if caminhao.x < LARGURA // 2:
                    pontuacao1 += 1
                else:
                    pontuacao2 += 1

        # Desenhar jogadores e caminhões
        TELA.blit(carro_azul, (jogador1_x, jogador1_y))
        TELA.blit(carro_verde, (jogador2_x, jogador2_y))
        for caminhao in caminhoes:
            TELA.blit(caminhao_img, caminhao)

        # Desenhar pontuação
        texto_pontuacao1 = fonte.render(f"Jogador 1: {pontuacao1}", True, PRETO)
        texto_pontuacao2 = fonte.render(f"Jogador 2: {pontuacao2}", True, PRETO)
        TELA.blit(texto_pontuacao1, (10, 10))
        TELA.blit(texto_pontuacao2, (LARGURA - texto_pontuacao2.get_width() - 10, 10))

        # Atualizar a tela e o relógio
        pygame.display.flip()
        relogio.tick(30)

# Executar o jogo
if __name__ == "__main__":
    jogo()
