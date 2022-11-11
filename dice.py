import random
import time

def dice():
  player = random.randint(1,6)
  print("You rolled " + str(player))

  ai = random.randint(1,6)
  print("Computer is rolling... ")
  time.sleep(3)
  print("The compute has rolled a " + str(ai))

  if player > ai:
    print("Yon won")

  if player == ai:
    print("Tie")

  if player < ai:
    print("You lost")

  # print("Quit? Y/N")
  is_quit = input("Quit? Y/N: ").upper()

  if is_quit == 'Y':
    exit()

  if is_quit == 'N':
     pass
  else: 
    print("I don't understand that")


while True:
  print("Press return to roll you dice")
  roll = input()
  dice()
