# guess_number.py
# Version 1
'''
secret_number = 8
player_guess = int(input("Please input your guess: "))
if player_guess == secret_number:
 print("You win!")
else:
  print("You lose")
  '''

# Version 2
'''
secret_number = 8
max_guesses = 3
guess_count = 0
while (guess_count < max_guesses):
  player_guess = int(input("Please input your guess from 1 to 10: "))
  guess_count += 1
  if (player_guess == secret_number):
    print("Congratulation! You guess correctly!")
    exit()
  else:
    print("You guess wrong! Please guess again!")
    print("Your remained guess: ", max_guesses - guess_count)

print("You lost!")
'''

#Version 3
import random
secret_number = random.randint(1,10)
max_guesses = 4
guess_count = 0
while (guess_count < max_guesses):
  try:
    player_guess = int(input("Please input your guess(1-10): "))
    guess_count += 1
    if (player_guess == secret_number):      
      break
    elif player_guess < secret_number:
        print("You guess number is less than the secret number ")
    else: 
        print("You guess number is greater than the secret number ")      
    print("Your remained guess: ", max_guesses - guess_count)
  except:
    print("Sorry, your guest must be an integer")

if (player_guess == secret_number):   
  print("Congratulation! You guess correctly!")
else:
  print("You lost!")

# import random
# secret_number = random.randint(1,10)
# max_guesses = 4
# guess_count = 0
# while (guess_count < max_guesses):
  
#     player_guess = input("Please input your guess(1-10): ")

#     if player_guess.isnumeric():
#       player_guess = int(player_guess)
#       guess_count += 1
#       if (player_guess == secret_number):      
#         break
#       elif player_guess < secret_number:
#           print("You guess number is less than the secret number ")
#       else: 
#           print("You guess number is greater than the secret number ")      
#       print("Your remained guess: ", max_guesses - guess_count)
#     else: 
#       print("Sorry, your guest must be an integer")
#   # except:
#   #   print("Sorry, your guest must be an integer")

# if (player_guess == secret_number):   
#   print("Congratulation! You guess correctly!")
# else:
#   print("You lost!")




