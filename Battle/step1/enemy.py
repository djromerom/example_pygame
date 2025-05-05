import pygame
import random
from settings import WIDTH, HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/enemy.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = random.randint(2, 4)  # Velocidad aleatoria
        self.direction = random.choice(['horizontal', 'vertical'])

    def update(self):
        if self.direction == 'horizontal':
            self.rect.x += self.speed
            if self.rect.right >= WIDTH or self.rect.left <= 0:
                self.speed = -self.speed  # Cambia dirección
        else:
            self.rect.y += self.speed
            if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
                self.speed = -self.speed