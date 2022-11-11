# rock_paper_scissor.py
import random

r = 0
p = 1
s = 2
keep_playing = True
while keep_playing = True:
  computer_choice = random.randint(0,2) # 0 => rock, 1=> paper, 2 => scissor
  player_choice = int(input("Your choice (0=>rock, 1=>paper, 2=>scissor): "))
  print("Computer choice (0=>rock, 1=>paper, 2=>scissor): ", computer_choice)
  if player_choice == computer_choice:
    print("Draw!")
  elif player_choice == r:
    if computer_choice == p:
      print("You lost!")
    else:
      print("You won!")
  elif player_choice == p:
    if computer_choice == s:
      print("You lost!")
    else:
      print("You won!")
  else:
    if computer_choice == r:
      print("You lost!")
    else:
      print("You won!")
  print("Do you want to play again (Y/N) ? ")
  answer = input()
  if answer == "Y":
    kee
