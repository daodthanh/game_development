# shoot_the_fruits.py
from random import randint 
apple = Actor("orange")

def draw():
  screen.clear() 
  apple.draw()

def place_apple():
  apple.x = randint(10, 800) 
  apple.y = randint(10, 600)

def on_mouse_down(pos):
  if apple.collidepoint(pos):
    print("Good shot!") 
    place_apple() 
  else:
    print("You missed!") 
    quit()

place_apple()