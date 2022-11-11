import pygame
import sys
import os 

WORLD_X = 960
WORLD_Y = 720
FPS = 40
ANI = 4

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

clock = pygame.time.Clock()
pygame.init()

world = pygame.display.set_mode([WORLD_X, WORLD_Y])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

main = True

while main:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        try:
          sys.exit()
        finally:
          main = False
    if event.type == pygame.KEYDOWN:
        if event.key == ord('q'):
          pygame.quit()
          try:
            sys.exit()
          finally:
            main = False

world.blit(backdrop, backdropbox)
pygame.display.flip()
clock.tick(fps)