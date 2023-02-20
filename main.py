import pygame, sys
from pygame.locals import QUIT

SIZE = 10
WIDTH = 40
HEIGHT = 30

pygame.init()
size = (WIDTH * SIZE, HEIGHT * SIZE)
screen = pygame.display.set_mode(size)
background = (0, 0, 255)

snake = [(20, 20), (21, 20), (22, 20)]


def game_to_screen(x, y):
    return x * SIZE, y * SIZE


def draw():
    screen.fill(background)
    for part in snake:
        x, y = part
        (screen_x, screen_y) = game_to_screen(x, y)
        color = (4, 235, 102)
        rect = ((screen_x, screen_y), (SIZE, SIZE))
        pygame.draw.rect(screen, color, rect)
    pygame.display.update()


step = (1, 0)


def move():
    x, y = snake[0]
    dx, dy = step
    new_x = (x + dx + WIDTH) % WIDTH
    new_y = (y + dy + HEIGHT) % HEIGHT
    snake.insert(0, (new_x, new_y))
    snake.pop()


clock = pygame.time.Clock()

pygame.display.set_caption('Freedom Snake')
while True:
    move()
    draw()
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
