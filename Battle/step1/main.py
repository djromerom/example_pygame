import pygame
import sys
from settings import WIDTH, HEIGHT, WHITE
from player import Player

# Inicializar
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My RPG")
clock = pygame.time.Clock()

# Fondo
background = pygame.image.load('assets/background.png').convert()

# Crear jugador
player = Player(100, 100)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Bucle principal
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar
    all_sprites.update()

    # Dibujar
    screen.blit(background, (0, 0))  # Fondo
    all_sprites.draw(screen)          # Jugador
    pygame.display.flip()

pygame.quit()
sys.exit()