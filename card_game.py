# card_game.py
import random

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2','3','4','5','6','7','8','9','10','Jack','Quen', 'King')

NCARDS = 8

def get_card(deck_list_in):
  this_card = deck_list_in.pop()
  return this_card

def shuffle(deck_list_in):
  deck_list_out = deck_list_in.copy()
  random.shuffle(deck_list_out)
  return deck_list_out

print('Welcome to Higher or Lower. ')
print('You have to choose whether the next card to be shown will be higher or lower than the current card')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

starting_deck_list = []
for suit in  SUIT_TUPLE:
  for this_value, rank in enumerate(RANK_TUPLE):
    card_dict = {'rank': rank, 'suit': suit, 'value': this_value + 1}
    starting_deck_list.append(card_dict)

score = 50
while True:
  print()
  game_deck_list = shuffle(starting_deck_list)
  current_card_dict = get_card(game_deck_list)
  current_card_rank = current_card_dict['rank']
  current_card_value = current_card_dict['value']
  current_card_suit = current_card_dict['suit']
  print('Starting card is: ', current_card_rank + ' of ' + current_card_suit)
  print()

  for card_number in range(0, NCARDS):
    answer = input('Will the next card be higher or lower than the ' + 
                  current_card_rank + ' of ' + current_card_suit + '? (enter h or l): ')
    answer = answer.casefold()
    next_card_dict = get_card(game_deck_list)
    next_card_rank = next_card_dict['rank']
    next_card_value = next_card_dict['value']
    next_card_suit = next_card_dict['suit']
    print('Next card is: ', next_card_rank + ' of ' + next_card_suit)

    if answer == 'h':
        if next_card_value > current_card_value:
            print('You got it right, it was higher')
            score = score + 20
        else:
            print('Sorry, it was not higher')
    elif answer == 'l':
        if next_card_value < current_card_value:
            score = score + 20
            print('You got it right it was lower')
        else:
            print("Sorry, it was not lower")
    print('Your score is: ', score)
    print()
    current_card_rank = next_card_rank
    current_card_value = next_card_value

  go_again = input('To play again, press Enter, or "q" to quit: ')
  if go_again == 'q':
      break

print('OK bye')

