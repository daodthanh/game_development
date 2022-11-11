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

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        print("User asked to quit.")
        done = True
    elif event.type == pygame.KEYDOWN:
        print("User pressed a key.")
    elif event.type == pygame.KEYUP:
        pygame.draw.rect(screen, GREEN,[50,50,100,100])
        print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("User pressed a mouse button")

  screen.fill(WHITE)
  pygame.draw.rect(screen, GREEN,[50,50,100,100])
  pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
  y_offset = 0 
  while y_offset < 100:

    pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5) 
    y_offset = y_offset + 10

  for i in range(200):
    radians_x = i / 20 
    radians_y = i / 6

    x = int(75 * math.sin(radians_x)) + 200 
    y = int(75 * math.cos(radians_y)) + 200

    pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

  for x_offset in range(30, 300, 30):
    pygame.draw.line(screen,BLACK,[x_offset,100],[x_offset-10,90],2) 
    pygame.draw.line(screen,BLACK,[x_offset,90],[x_offset-10,100],2)
  
  pygame.draw.rect(screen,BLACK,[100,100,250,200],2)
  pygame.draw.arc(screen, GREEN, [100,100,250,200], PI/2, PI, 2) 
  pygame.draw.arc(screen, BLACK, [100,100,250,200], 0, PI/2, 2) 
  pygame.draw.arc(screen, RED, [100,100,250,200],3*PI/2, 2*PI, 2) 
  pygame.draw.arc(screen, BLUE, [100,100,250,200], PI, 3*PI/2, 2)
  pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)

  # Select the font to use, size, bold, italics
  font = pygame.font.SysFont('Calibri', 25, True, False)

  # Render the text. "True" means anti-aliased text. 
  # Black is the color. This creates an image of the 
  # letters, but does not put it on the screen
  text = font.render("My Text", True, BLACK)
  # Put the image of the text on the screen at 250x250 
  screen.blit(text, [250, 250])

  pygame.display.flip()
  clock.tick(60)

pygame.quit()