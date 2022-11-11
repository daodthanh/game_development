# nim1.py
# Display the game
import random

print("Welcome to the game of Nim version !")
# Input the number of sticks
stick_num = int(input("Please input the number of sticks: "))

# Show all sticks
for i in range(stick_num):
  print("| ", end=" ")
  print()
# Rules of game
print("Take 1-3 sticks each time, who take the last one will win!")
# Player move
gameover = False
while not gameover:
  legal = False
  while not legal: 
    player_move = int(input("Please take your sticks: "))
    # Check player move is legal or not
    if player_move < 1 or player_move > 3:
      legal = False
      print("Your move is illegal. Move again! ")
    else:
      legal = True

  if stick_num > player_move:
    stick_num = stick_num - player_move
  else:
    stick_num = 0

  # Check game over? stick number = 0

  if stick_num == 0:
    gameover = True
    print("Congratulation! You won!")
    break
  else:
    for i in range(stick_num):
      print("| ", end=" ")
    print()

  # computer move
  computer_move = random.randint(1,3)
  print("Computer move: ", computer_move)
  # Check gam eover 
  if stick_num > computer_move:
    stick_num = stick_num - computer_move
  else:
    stick_num = 0

  # Check game over? stick number = 0

  if stick_num == 0:
    gameover = True
    print("Computer won! You lost!")
    break
  else:

    for i in range(stick_num):
      print("| ", end=" ")
    print()