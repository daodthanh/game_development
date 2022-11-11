import pygame
import math

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
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5

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
  pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
  pygame.draw.rect(screen, RED, [rect_x+10, rect_y+10, 30, 30])
  rect_x += rect_change_x
  rect_y += rect_change_y
  if rect_x > 750 or rect_x < 0:
    rect_change_x *= -1
  if rect_y > 550 or rect_y < 0:
    rect_change_y *= -1

  pygame.display.flip()
  clock.tick(60)
  # 
pygame.quit()