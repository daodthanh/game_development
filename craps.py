# craps.py
from random import *

roll = list(range(0,13))

for i in range(1,13):
  roll[i] = set()

for i in range(1,7):
  for j in range(1,7):
    k = i + j
    roll[k].add((i,j))


winner = roll[7] | roll[11]
loser = roll[2] | roll[3] | roll[12]

while True:
  die1 = randrange(1,7)
  die2 = randrange(1,7)

  val = (die1, die2)
  print("Shooter rolls: ", val)

  if val in winner:
    print("The shooter wins!")
    break
  elif val in loser:
    print("The shooter loses!")
    break