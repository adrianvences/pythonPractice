from art import logo,vs
import random
from gameData import data

print(logo)

score = 0
game_should_continue = True
account_B = random.choice(data)

def formatData(account) :
  """takes account data and returns printable data"""
  account_name = account['name']
  account_description = account['description']
  account_country = account['country']
  return(f'{account_name} , a {account_description} , from {account_country}')

# working on while loop

while game_should_continue:
  #generate random data
  account_A = account_B
  account_B = random.choice(data)
  while account_A == account_B :
    account_B = random.choice(data)

  def check_answer(guess,a_followers,b_followers):
    """takes user guess and follower counts and returns if they got it right. """
    if a_followers > b_followers:
      return guess == 'a'
    else:
      return guess == 'b'

  print(f'Compare A : {formatData(account_A)}')
  print(vs)
  print(f'Against B : {formatData(account_B)}')
  # format account data into readable format // ended up turning into function

  # ask who has more followers
  guess = input('Who has more followers? Type "A" or "B" : ').lower()

  # check if user is correct.
  a_follower_count  = account_A['follower_count']
  b_follower_count  = account_B['follower_count']
  is_correct = check_answer(guess,a_follower_count,b_follower_count)

  print(logo)
  if is_correct:
    score += 1
    print(f"You're correct! Current Score : {score}")

  else:
    game_should_continue = False
    print(f"Sorry thats wrong. Finally score: {score}")

  ## use follower count of each account
  ## use if statement to check if user is correct
