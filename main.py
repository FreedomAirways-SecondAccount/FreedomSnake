import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((400, 300))
background = (0, 0, 255)

snake = [(20,20), (21, 20), (22, 20)]

SIZE = 10

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

pygame.display.set_caption('Freedom Snake')
while True:
      draw()
      for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   