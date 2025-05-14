import pygame
import random

from LinkedList import LinkedList
from Snake import Snake

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with LinkedList")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 10

# Direcciones
directions = {
    "UP": (0, -CELL_SIZE),
    "DOWN": (0, CELL_SIZE),
    "LEFT": (-CELL_SIZE, 0),
    "RIGHT": (CELL_SIZE, 0)
}

# Snake como LinkedList
snake = LinkedList()
snake.add(Snake(100, 100))  # Posición inicial

current_direction = "RIGHT"


# Comida
def spawn_food():
    return (random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)


food = spawn_food()

# Función principal
running = True
while running:
    clock.tick(FPS)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and current_direction != "DOWN":
        current_direction = "UP"
    if keys[pygame.K_DOWN] and current_direction != "UP":
        current_direction = "DOWN"
    if keys[pygame.K_LEFT] and current_direction != "RIGHT":
        current_direction = "LEFT"
    if keys[pygame.K_RIGHT] and current_direction != "LEFT":
        current_direction = "RIGHT"

    # Mover la serpiente
    head_x = snake.tail.x
    head_y = snake.tail.y
    move_x, move_y = directions[current_direction]
    new_head = Snake(head_x + move_x, head_y + move_y)
    # new_head in snake or
    # Comprobar colisiones
    if (snake.contains(new_head.x, new_head.y) or new_head.x < 0 or new_head.x >= WIDTH or
            new_head.y < 0 or new_head.y >= HEIGHT):
        print("Game Over!")
        running = False
        break

    snake.add(new_head)

    # Comer comida
    if new_head.x == food[0] and new_head.y == food[1]:
        food = spawn_food()
    else:
        snake.pop()

    # Dibujar
    screen.fill(BLACK)

    current = snake.head

    while current is not None:
        pygame.draw.rect(screen, GREEN, (current.x, current.y, CELL_SIZE, CELL_SIZE))
        current = current.next

    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    pygame.display.update()

pygame.quit()