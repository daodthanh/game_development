# guess2.py
import random

secret_number = random.randint(1,10)

player_guess = int(input("Your guess the dice(1-6): "))
if player_guess == secret_number:
  print("You won!")
else:
  print("You lost!")
  print("The secret number is ", secret_number)

