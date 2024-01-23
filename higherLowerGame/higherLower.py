from art import logo, vs
from gameData import data
import random

print(logo)

# create two variables for comparison
# compareA = ''
# compareB = ''
gameContinue = True
# make a random function that pulls a random dict our of array
def randomPuller():
  return (random.choice(data))

# randomPuller()

# make a function that compares A and B 
# while gameContinue == True:
def compare():
  compareA = randomPuller()
  compareB = randomPuller()
  print(f"{compareA['name']}, a {compareA['description']} , from {compareA['country']}")
  print(vs)
  print(f"{compareB['name']}, a {compareB['description']} , from {compareB['country']}")

  answer = input('who has more followers? Type A or B. :  ')

  


compare()

# 'name': 'Selena Gomez',
#         'follower_count': 174,
#         'description': 'Musician and actress',
#         'country': 'United States'