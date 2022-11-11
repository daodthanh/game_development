# guess_number_1.py
choice = 7 
print ("Pick-a-number is a simple guessing game. The") 
print ("computer will select a number between 1 and 10")
print ("and you are expected to guess what it is.") 
print ("When the program displays 'Please guess") 
print ("a number between 1 and 10: ' you type in") 
print ("your guess followed by the <enter> key. Your ") 
print ("guess must be an integer in the range 1 to 10.") 
print ("The computer will tell you if you win or lose.")
print ("Please guess a number between 1 and 10: ") 
playerchoice = int(input())

if choice == playerchoice:

  print ("You win!") 
else:

  print ("Sorry, you lose.")