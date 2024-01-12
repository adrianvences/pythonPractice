import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


usersHand = []

computersHand = []


def blackJack():
  usersHand = random.sample(cards,2) 
  computersHand = random.sample(cards,2) 
  print(f'Your hand : {usersHand}')
  # print(computersHand)
  print(f'computersHand : {computersHand[0]}')

  usersScore = sum(usersHand)
  # print(usersScore)
  computersScore = sum(computersHand)
  # print(computersScore)
  
  if usersScore == 21 and computersScore == 21:
    print('Draw. Both have drawn black jack!')
  if computersScore == 21:
    print('Computer has won! BlackJack!')
  elif computersScore > 21:
      print("computer has lost")
  if usersScore == 21:
    print('User has BlackJack!')
  elif usersScore > 21:
      print("user has lost")
  # if usersScore and computersScore == 21:
  #   print('Draw. Both have drawn black jack!')

  drawCard = True
  while drawCard == True :
      newCard = input('Do you want another card? Type "Y" for yes or "N"for no : ')
      if newCard == 'y':
        usersHand.append(random.choice(cards))
      else:
        drawCard = False
      print (usersHand)
  
  while computersScore < 16:
    computersHand.append(random.choice(cards))
  computersScore = sum(computersHand)
  print(computersHand)

blackJack()

