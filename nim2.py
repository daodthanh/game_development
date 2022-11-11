
import random

stick_num = 21

def setup():
  print("Welcome to the game of Nim version !")
  # Input the number of sticks
  stick_num = int(input("Please input the number of sticks: "))

def display_game():
  # Show all sticks
  print("Stick num: ", stick_num)
  for i in range(stick_num):
    print("| ", end=" ")
  print()

def show_rules():
  #show rules
  print("Take 1-3 sticks each time, who take the last one will win!")

def move():
  move = int(input("Take your sticks: "))
  return move

def check_legal(move):
  legal = True
  if move < 1 or move > 3:
    legal = False
  else:
    legal = True
  return legal

def update_game_state(move):
    global stick_num
    # print("Before update stick num", stick_num)
    if stick_num > move:
      stick_num = stick_num - move
    else:
      stick_num = 0

def check_game_over():

  return stick_num == 0

def play():
  game_over = False
  while not game_over:
    # Player move
    legal = False
    while not legal:
      player_move = move()     
      legal = check_legal(player_move)
      if not legal:
        print("Your move is illegal. Move again! ")
    update_game_state(player_move)
    game_over = check_game_over()
    if game_over:
      print("Congratulation! You won!")
      break
    else:
      display_game()

    # Computer move
    computer_move = random.randint(1,3)
    print("Computer move: ", computer_move)
    update_game_state(computer_move)
    game_over = check_game_over()
    if game_over:
      print("Sorry! You lost!")
      break
    else:
      display_game()

setup()
display_game()
show_rules()
play()