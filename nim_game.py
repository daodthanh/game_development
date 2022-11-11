# nim_game.py
def rules():
  print("Choose one row each time")
  print("You can take any sticks >= 1")
  print("Who take the last stick will win")

def display_state(val):
  for j in range(0,3):
    print (j+1, ": ", end="") 
    for i in range(0,val[j]):
      print ("| ",end="")
    print("")

def prompt (move):
  row = input ("Your move: which row? ")
  # Prompt for row & # read it
  sticks = input (" how many sticks?") # Prompt for # sticks & read # Convert row to integer and decrement to be from 0 to 2.
  move[0] = int(row)-1 # Assign to the list[0]
  move[1] = int(sticks) # Assign value to list[1]

def legal_move(move, state):
  row = move[0] # Which row was requested? 
  sticks = move[1] # How many sticks 
  if row<0 or row>2: # Legal number of rows?
    return False # No 
  if sticks<=0 or sticks>val[row]: # Legal number of # sticks?
    return False # No 
  return True # Both were ok, so the # move is OK.

def make_move(move, state):
  row = move[0] 
  sticks = move[1]
  # Subtract move[1] sticks from # those that are in row # move[0].
  # Place the new number of sticks in the state list 
  # if state[row] >sticks
  state[row] = state[row]-sticks

def game_over(val):
  if sum(val) == 0:
    return True
  else:
    return False


val = [5, 7, 9] # the game state: 5, 7, and 9 sticks 
done = False # Is the game over?

user_move = [-1, -1] # A move is a row and a number of # sticks.

print ("The game of Nim.") 
rules() # Print the rules for the game 
while not done: # Run until the game is over 
  display_state(val) # Show the game board 
  prompt(user_move) # Ask user for their move 
  ok = legal_move (user_move, val) # Was the playerꞌs move # OK?

  while not ok:
    print ("This move is not legal.") 
    display_state(val) 
    prompt(user_move) # Ask user for their move 
    ok = legal_move (user_move, val) 
  make_move (user_move,val) # Make it 
  if game_over(val):

    print("You win!") 
    break; 
  print ("State after your move is ") # display it. 
  display_state(val)