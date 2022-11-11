# nim3.py

import random

row_num = 0
sticks_list = []

def setup():
  global row_num, sticks_list
  print("Welcome to the game of Nim version !")
  # Input the number of sticks
  row_num = int(input("Please input the number of stick rows: "))
  sticks_list = []
  for i in range(row_num):
    sticks = int(input(f"The sticks of row {i+1}: "))
    sticks_list.append(sticks)

def display_game():
  # Show all sticks
  print("Show sticks ")
  # print(row_num, sticks_list)
  for i in range(len(sticks_list)):
    print(f"Row {i+1}: ", end=" ")
    for j in range(sticks_list[i]):
      print("| ", end=" ")
    print()

def show_rules():
  #show rules
  print("Each time you can choose only 1 row: take all sticks or less, who take the last one will win!")

def move():
  row = int(input("Choose your row: "))
  sticks = int(input("Take your sticks: "))
  return (row, sticks)

def check_legal(move):
  row_index = move[0] - 1
  if row_index < 0 or row_index >= len(sticks_list):
    return False
  if move[1] < 1 or move[1] > sticks_list[row_index]:
    return False
  return True

def update_game_state(move):
    row_index = move[0]-1 # Offset for python list index
    if sticks_list[row_index] > move[1]:
      sticks_list[row_index] -= move[1]
    else:
      sticks_list.pop(row_index)

def game_over():
   return len(sticks_list) == 0

def play():
  while not game_over():
    # Player move
    legal = False
    while not legal:
      player_move = move()     
      legal = check_legal(player_move)
      if not legal:
        print("Your move is illegal. Move again! ")
    update_game_state(player_move)

    if game_over():
      print("Congratulation! You won!")
      break
    else:
      display_game()

    # Computer move
    # print("sticks list: ", sticks_list)
    chosen_row = random.randint(1,len(sticks_list))
    # print("computer row: ", chosen_row)
    chosen_sticks = random.randint(1,sticks_list[chosen_row-1])
    computer_move = (chosen_row, chosen_sticks)
    print("Computer move: ", computer_move)
    update_game_state(computer_move)
   
    if game_over():
      print("Sorry! You lost!")
      break
    else:
      display_game()

setup()
display_game()
show_rules()
play()