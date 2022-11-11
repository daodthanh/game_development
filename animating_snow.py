# animating_snow.py
import pygame
import math
import random

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
PI = math.pi

pygame.init()
pygame.display.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Thanh's game")

done = False

snow_list = []

for i in range(50):
  x = random.randrange(0,600)
  y = random.randrange(0,600)
  snow_list.append([x, y])
clock = pygame.time.Clock()


while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        print("User asked to quit.")
        done = True
    elif event.type == pygame.KEYDOWN:
        print("User pressed a key.")
    elif event.type == pygame.KEYUP:
        print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("User pressed a mouse button")

  screen.fill(BLACK)
  # pygame.draw.rect(screen, GREEN,[50,50,100,100])
  # for i in range(50):
  #   x = random.randrange(0, 400)
  #   y = random.randrange(0, 400)
  #   pygame.draw.circle(screen, WHITE, [x, y], 2)

  for i in range(len(snow_list)):
    pygame.draw.circle(screen, WHITE, snow_list[i], 2)
    snow_list[i][1] += random.random() * 3

    if snow_list[i][1] > 600:
      snow_list[i][1] = random.randrange(-50, -10)
      snow_list[i][0] = random.randrange(0,600)

  pygame.display.flip()
  clock.tick(60)
  # 
pygame.quit()