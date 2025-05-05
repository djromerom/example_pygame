import pygame
from settings import PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.load_images()
        self.direction = 'down'
        self.frame_index = 0
        self.image = self.animations[self.direction][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = PLAYER_SPEED
        self.max_health = 100
        self.current_health = self.max_health
        self.health_bar_length = 100
        self.health_ratio = self.max_health / self.health_bar_length
        self.animation_timer = 0

    def load_images(self):
        self.animations = {
            'down': [pygame.image.load('assets/player/player.png').convert_alpha(),
                     pygame.image.load('assets/player/player.png').convert_alpha()],
            'left': [pygame.image.load('assets/player/player_left.png').convert_alpha(),
                     pygame.image.load('assets/player/player_left.png').convert_alpha()],
            'right': [pygame.image.load('assets/player/player_right.png').convert_alpha(),
                      pygame.image.load('assets/player/player_right.png').convert_alpha()],
            'up': [pygame.image.load('assets/player/player_up.png').convert_alpha(),
                   pygame.image.load('assets/player/player_up.png').convert_alpha()]
        }

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = 'left'
            moving = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = 'right'
            moving = True
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.direction = 'up'
            moving = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.direction = 'down'
            moving = True

        if moving:
            self.animate()
        else:
            self.frame_index = 0
            self.image = self.animations[self.direction][self.frame_index]

    def animate(self):
        # Actualizar animación cada ciertos milisegundos
        now = pygame.time.get_ticks()
        if now - self.animation_timer > 200:  # Cada 200 ms cambia frame
            self.animation_timer = now
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.direction])
            self.image = self.animations[self.direction][self.frame_index]

    def update(self):
        self.handle_keys()

    def take_damage(self, amount):
        self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0

    def draw_health_bar(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (10, 10, self.health_bar_length, 20))  # Barra vacía roja
        pygame.draw.rect(surface, (0, 255, 0), (10, 10, self.current_health / self.health_ratio, 20))  # Barra verde