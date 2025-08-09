# ask the user to make a choice
# if the choice is not valid
#   print error
# ask computer to make a choice
# print choices with emoji
# determine the winner
# ask user to continue playing
# if not
# terminate

import random

emoji={'r': '🪨','p':'📃','s': '✂️'}
choices=('r','p','s')

while True:
  u=input('choose r/p/s : ').lower()

  if u not in choices:
    print("Wrong choice.Please try again.")
    continue

  c=random.choice(choices)

  print(f'you chose {emoji[u]}')
  print(f'computer chose {emoji[c]}')

  if u == c:
    print('Tie!')
  elif (u == 'p' and c == 's') or (u == 'r' and c=='p') or (u=='s' and c=='r'):
    print("Computer won ✨")
  else:
    print("you won 🌟")    

  should_continue=input("do you want to continue(y/n): ").lower()
  if should_continue =='n':
    print("Thanks for playing.")
    break

